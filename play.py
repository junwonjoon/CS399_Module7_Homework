"""
    Remove Outliers from a list of words
    Author: Wonjoon Jun
"""
from wv import Model
from scipy.stats import zscore

def a_to_b_is_like_c_to(a: str, b: str, c: str) -> str:
    a = model.find_word(a)
    b = model.find_word(b)
    c = model.find_word(c)
    d = b - a + c
    d.normalize()
    for w in model.find_similar_words(d,10):
        if w.text not in (a.text, b.text, c.text):
            return f"{a.text} to {b.text} is like {c.text} to {w.text}"
model = Model("models/glove_short.txt")
print(a_to_b_is_like_c_to("Berlin", "Germany", "Paris"))
