
import os,sys
import pandas as pd
import numpy as np
import scipy as sp
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def get_positive_and_negative_dataframe():
	""" this runs everything """
	df = pd.read_csv("data/train.tsv",sep="\t")
	dff = df[(df['Sentiment']==0) | (df.Sentiment==4)]
	return dff
	
	
	