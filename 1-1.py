from nltk.book import *
from __future__ import division
def lexical_diversity(text):
    return len(set(text)) / len(text)
def percentage(count, total):
    return 100 * count / total
if __name__ == '__main__':
    lexical_diversity(text5)
