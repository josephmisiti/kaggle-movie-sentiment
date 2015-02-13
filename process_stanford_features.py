"""
	extacts NLP features using stanford sentiment analysis software:
	
	https://github.com/stanfordnlp/CoreNLP
	
	previously used on Yelp reviews, is going to be adapted for movie reviews
"""

import os
import json
import pprint
import subprocess
import shlex
import tempfile
import pandas as pd
import itertools

try:
	os.mkdir("tempfiles")
except:
	pass

input_file = 'yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review_100.json'

def classify_sentiment(review):
	CMD1 = 'java -cp "*" -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -file %s -output ROOT' % review

	args=shlex.split(CMD1)
	p = subprocess.Popen(args, stdout=subprocess.PIPE)
	out, err = p.communicate()
	
	sentiment = []
	review = []
	
	for i,r in enumerate(out.strip().split("\n")):
		if i % 2 == 0:
			review.append(r)
		else:
			sentiment.append(r)
		
	return review,sentiment


def _load_lines(input_file):
	data = []
	with open(input_file) as f:
		for line in f:
			try:
				data.append(json.loads(line))
			except ValueError:
				pass
	return data

YELP_REVIEWS = _load_lines(input_file)

the_reviews,the_sentiment = [],[]
for review in YELP_REVIEWS:
	with tempfile.NamedTemporaryFile(dir="./tempfiles/",delete=False) as temp:
		temp.write(review['text'])
		temp.flush()
		r,s = classify_sentiment(temp.name)
		the_reviews.append(r)
		the_sentiment.append(s)
		
		assert(len(the_reviews) == len(the_sentiment))
		
		df = pd.DataFrame({
			'sentiment' : list(itertools.chain(*the_sentiment)),
			'review' : list(itertools.chain(*the_reviews)),
		})
		print df.head(100)
		df.to_csv("final.csv",encoding='UTF-8')
		
		







