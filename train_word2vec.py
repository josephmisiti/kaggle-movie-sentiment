import word2vec
import os.path

"""
	This script trains the word2vec and word2cluster algorithms
"""


print("[training word2vec algorithm]")
if not os.path.isfile('data/text8.bin'):
	word2vec.word2vec('data/text8', 'data/text8.bin', size=100, verbose=True)
print("[done]")
	
print("[training word2clusters algorithm]")
if not os.path.isfile('data/text8-clusters.txt'):
	word2vec.word2clusters('data/text8', 'data/text8-clusters.txt', 100, verbose=True)
print("[done]")
