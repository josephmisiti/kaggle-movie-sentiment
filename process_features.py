
import os,sys
import word2vec
import numpy as np

np.set_printoptions(precision=4)

from utils import get_positive_and_negative_dataframe

model = word2vec.load('data/text8.bin')

NUM_WORDVEC_FEATURES = 25

def process_features():
	""" """
	df = get_positive_and_negative_dataframe()
	#df = df.head(5)
	for row in df.iterrows():
		klass = row[1]['Sentiment']
		phrase = row[1]['Phrase']
		r = []
		for p in phrase.split(" "):
			try:
				v = model[p.lower()][0:NUM_WORDVEC_FEATURES]
				r.append(v)
			except KeyError,e:
				pass
				
		f = np.matrix(r)
		ff = f.sum(axis=0)
		avg_vector =  ",".join(['%5.5f' % a for a in list(np.array(ff).reshape(-1,))])
		print "%s,%s" %(klass,avg_vector)
	
if __name__ == "__main__":
	sys.exit(process_features())