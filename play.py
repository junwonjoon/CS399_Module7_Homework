"""
    Remove Outliers from a list of words
    Author: Wonjoon Jun
"""
from wv import Model
from scipy.stats import zscore

# model = Model("models/glove_short.txt")
while True:
    words = input("Please enter a comma separated list of words: ").split(',')


