##### Introduction

Experiments with classifying sentiment of movie removes

http://www.kaggle.com/c/sentiment-analysis-on-movie-reviews

##### Installation

To train your word2vec algorthm, execute

```bash
(machinelearning)JOSEPH-MISITI:kaggle-movie-reviews josephmisiti$ python train_word2vec.py
Starting training using file data/text8
Vocab size: 71291
Words in train file: 16718843

```

For more examples of using word2vec, go here and check this iPython notebook out:

http://nbviewer.ipython.org/github/danielfrg/word2vec/blob/master/examples/word2vec.ipynb

##### Build you features

The following command builds paragraph/sentence vectors (water down ones anyways) of each 
movie review.

```
python process_features.py > data/word2vec_pos_neg.csv
```

##### Notebooks

My code for the Kaggle Movie Sentiment

http://nbviewer.ipython.org/github/josephmisiti/kaggle-movie-sentiment/blob/master/NLTK%20Experiments.ipynb

http://nbviewer.ipython.org/github/josephmisiti/kaggle-movie-sentiment/blob/master/Exploration.ipynb