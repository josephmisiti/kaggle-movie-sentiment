"""
	run logistic regression on features.
"""

from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.lda import LDA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


df = pd.read_csv("data/word2vec_pos_neg.csv",header=None)
columns = ["c%s" % i for i in range(len(df.columns))]
df.columns = columns
df =  df.head(500)

#print df

X = df[df.columns[1:2]]
y = pd.factorize(df["c0"])[0]


clf = LogisticRegression()
clf.fit(X, y)
print (clf.intercept_, clf.coef_)