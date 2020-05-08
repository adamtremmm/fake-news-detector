import os
from random import random
import numpy as np
import pandas as pd

#utilities
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#feature extraction
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#models
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB, ComplementNB, MultinomialNB

from classifier import Classifier

#datapaths
FNCSAMPLE = "../../data/news_sample.csv"
FNCFULL = "../../data/data_full/news_cleaned_2018_02_13.csv"

#pipeline objects
# model = BernoulliNB()
# vectorizer = TfidfVectorizer(min_df=5, max_df = 0.8, sublinear_tf=True, ngram_range = (1,2), use_idf=True)

lin_svc = Pipeline([
		    ('vect', TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')),
		    ('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False, tol=1e-3))), 
		    ('classification', LinearSVC(penalty="l2"))
		    ])

bernNB = Pipeline([
		    ('vect', TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')),
		    ('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False, tol=1e-3))), 
		    ('classification', BernoulliNB(alpha=.01))
		    ])

svm_sgd_linsvc = Pipeline([('vect', TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')),
		    ('feature_selection', SelectFromModel(LinearSVC(penalty="l1", dual=False, tol=1e-3))), 
		    ('classification', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None))])

svm_sgd_tfidf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None)),
])

if __name__ == '__main__':
	
	print("Starting up...")

	# build and evaluate a classifier given a single pipeline object
	#clf = Classifier(FNCFULL, bernNB)
	#clf.run()

	# or, build and evaluate multiple classifiers given a list of pipeline objects
	list_of_pipelines = [lin_svc, bernNB, svm_sgd_linsvc, svm_sgd_tfidf]
	# NOTE: if using a list of pipes, then pass a str placeholder
    # to pipeline as dummy parameter
	clf = Classifier(FNCFULL,"pipes",list_of_pipelines)
	clf.run()
