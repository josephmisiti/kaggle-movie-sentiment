
import os,sys
import pandas as pd
import numpy as np
import scipy as sp
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import word2vec

def main():
	""" this runs everything """
	df = pd.read_csv("data/train.tsv",sep="\t")
	return df[(df['Sentiment']==0) | (df.Sentiment==4)].head()
	
	
if __name__ == "__main__":
	sys.exit(main())
	