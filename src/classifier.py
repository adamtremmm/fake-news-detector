import os
from random import random
import numpy as np
import pandas as pd

#utilities
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#models
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB


class Classifier():
    """

    Build and evaluate a classifier 
    given a path to data and a single pipeline object:

    >>> from classifier import Classifier
    >>> clf = Classifier(datapath, model_pipeline)
    >>> clf.run()

    or, build and evaluate multiple classifiers given a list of pipeline objects:

    >>> many_pipelines = [lin_svc, bernNB, svm_sgd_linsvc, svm_sgd_tfidf]
    >>> clf = Classifier(datapath,"lots of pipes!",many_pipelines)
    >>> clf.run()

    """
    def __init__(self, infile, pipeline, list_of_pipelines=None):
        self.infile = infile
        self.X_train, self.X_test, self.y_train, self.y_test = [None]*4
        self.model_pipeline = pipeline
        self.pipeline_list = list_of_pipelines
        self.classifier = None
        self.report = None

    def run(self):
        # load data
        self.X_train, self.X_test, self.y_train, self.y_test = self.load_data(self.infile)
        if self.pipeline_list:
            for pipe in self.pipeline_list:
                # train models
                self.classifier = self.train_model_pipe(pipe)
                # evaluate model
                self.performance()
                # pickle?
                print("Want to save this classifier for later? (y/n)")
                x = input()
                if x is 'y':
                    print("Okay, what should we call this classifier?")
                    name = input()
                    self.pickle(name)
                    self.classification_report_csv(name)
        else:
            # train model
            self.classifier = self.train_model()
            # evaluate model
            self.performance()
            # pickle?
            print("Want to save this classifier for later? (y/n)")
            x = input()
            if x is 'y':
                print("Okay, what should we call this classifier?")
                name = input()
                self.pickle(name)
                self.classification_report_csv(name)
        print("Done.")


    def load_data(self,infile, proportion=0.3):
        print("Loading data")
        #if it's FNCorpus, only load a random fraction
        if 'news_cleaned' in infile:
            print("wrangling")
            df = pd.read_csv(infile, skiprows=lambda x: x>0 and random() > 0.01)
        else:
            print("Nice and small")
            df = pd.read_csv(infile)
        #data wrangling
        # create 2 dfs from filtered df
        bindf1 = df[df['type'] == 'fake']
        bindf2 = df[df['type'] == 'reliable']
        # then concat into single df
        df = pd.concat([bindf1, bindf2], ignore_index=True)

        #print categories
        print(df['type'].unique().tolist())
        #train-test-split
        #default proportion for test is 0.3
        return train_test_split(df.content, df.type, test_size=proportion)

    def get_train_head(self):
        return y_train.head()
        
    def get_test_head(self):
        return y_test.head()

    def train_model(self):
        """ Given pipeline object, and returns a classifier """
        # fit model
        print("Training a model...")
        clf = self.model_pipeline.fit(self.X_train, self.y_train)
        return clf

    def train_model_pipe(self, pipeline):
        """ Takes a pipeline object and returns a classifier """
        # fit model
        clf = pipeline.fit(self.X_train, self.y_train)
        return clf

    def performance(self):
        # testing predictions
        print("Checking performance")
        predicted = self.classifier.predict(self.X_test)
        print(f"Prediction accuracy: {np.mean(predicted == self.y_test)}")
        #get report
        report = metrics.classification_report(self.y_test, predicted, target_names=list(self.y_test.unique()), output_dict=True)
        af1 = report['accuracy']
        supp = report['macro avg']['support']
        report['accuracy'] = {'precision':'','recall':'','f1-score':af1,'support':supp}
        self.report = report
        print(self.report)
        print(metrics.confusion_matrix(self.y_test, predicted))

    def pickle(self, name_of_pickle):
        print(f'Pickling {name_of_pickle} classifier.')
        joblib.dump(self.classifier, f'../classifiers/clf_pkl/{name_of_pickle}.pkl')

    def classification_report_csv(self, name):
        df = pd.DataFrame.from_dict(self.report)
        df.T.to_csv(f'../reports/{name}.csv')
        print(f"Saved report as {name}.csv")

    
    

