#!/usr/bin/python3
# fake_news_detector.py
#
from time import time

"""
I'm getting the following DeprecationWarning when I import joblib:
/usr/lib64/python3.7/site-packages/sklearn/feature_extraction/dict_vectorizer.py:6: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
	from collections import Mapping
	...
Looks to be a bug in sklearn:
https://github.com/scikit-learn/scikit-learn/issues/11121

Decided to just suppress warnings for now:
https://docs.python.org/3.7/library/warnings.html#temporarily-suppressing-warnings
"""
import warnings
with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=DeprecationWarning)
	from sklearn.externals import joblib

# Paths to pickled classifiers
FAKE_RELIABLE = '../classifiers/clf_pkl/clf_fake_reliable.pkl'
FAKE_RELIABLE_RR = '../classifiers/clf_pkl/clf_fake_reliable_rr.pkl'


class FakeNewsDetector():
	"""
	Prediction module
	"""
	def __init__(self, clf=FAKE_RELIABLE):
		self._loaded_clf = joblib.load(FAKE_RELIABLE)

	def make_prediction(self,text):
		# load the classifiers
		t0 = time()
		predicted = self._loaded_clf.predict([text])
		duration = round(time() - t0, 3)
		#print(f'Given: {text}\nPredicted: {predicted} ({duration}s)')
		return predicted



# if __name__ == '__main__':
	
# 	sample_tweet = "President Trump officially resigned as President of the United States via tweet last night."
# 	sample_tweet2 = "Canadian Prime Minister Justin Trudreau works in Ottawa, Ontario."

# 	fk = FakeNewsDetector()
# 	fk.make_prediction(sample_tweet)
# 	fk.make_prediction(sample_tweet2)

