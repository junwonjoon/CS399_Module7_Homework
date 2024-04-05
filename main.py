# from play import a_to_b_is_like_c_to, outlier_finder
import streamlit as st
from typing_extensions import Self
from math import sqrt
from time import process_time
from scipy.stats import zscore


class Word:
    """ Represents a word and its vector"""

    def __init__(self, text: str, vector: list[float]) -> None:
        self.text = text
        self.vector = vector

    def __repr__(self) -> str:
        vector_preview = ', '.join(map(str, self.vector[:2]))
        return f"{self.text} [{vector_preview}, ...]"

    def norm(self) -> float:
        return sqrt(sum([x * x for x in self.vector]))

    def normalize(self) -> None:
        length = self.norm()
        self.vector = [x / length for x in self.vector]

    def similarity(self, w: Self) -> float:
        return self * w

    def __add__(self, w: Self) -> Self:
        return Word("", [x + y for x, y in zip(self.vector, w.vector)])

    def __sub__(self, w: Self) -> Self:
        return Word("", [x - y for x, y in zip(self.vector, w.vector)])

    def __mul__(self, w: Self) -> float:
        return sum([x * y for x, y in zip(self.vector, w.vector)])


class Model(list):
    """ Represents a model, a list of words"""
    features = 300

    def __init__(self, inp_file_name: str) -> None:
        super().__init__()
        print(f"Loading model from {inp_file_name} ...")
        t0 = process_time()
        try:
            with open(inp_file_name, mode="r", encoding="utf8") as inp_file:
                for line in inp_file:
                    sa = line.split(" ")
                    self.append(Word(sa[0], [float(x) for x in sa[1:]]))
            print(f"Loaded in {process_time() - t0} secs")
        except:
            print("Couldn't open file, please try again later")

    def find_word(self, text: str) -> Word | None:
        for w in self:
            if w.text == text:
                return w
        else:
            return None

    def find_similar_words(self, word: Word, n: int = 10) -> list[Word]:
        return sorted(self, key=lambda w: w.similarity(word), reverse=True)[:n]

    def __repr__(self) -> str:
        return f"Model({len(self)} words)"

    def __getitem__(self, text: str) -> Word:
        return self.find_word(text)

    def __contains__(self, text: str) -> bool:
        return self.find_word(text) is not None


model = Model("short_glove.txt")


def a_to_b_is_like_c_to(a: str, b: str, c: str) -> str:
    # let 1 mean Word class
    a1 = model.find_word(a)
    b1 = model.find_word(b)
    c1 = model.find_word(c)
    if a1 is None or b1 is None or c1 is None:
        return f"Couldn't find the word: {a if a1 is None else ''}{b if b1 is None else ''}{c if c1 is None else ''}"
    d = b1 - a1 + c1
    d.normalize()
    for w in model.find_similar_words(d, 10):
        if w.text not in (a1.text, b1.text, c1.text):
            return f"{w.text}"


def outlier_finder(str_list: list) -> str:
    Word_class_words, mean_of_similarities = [], []
    for words in str_list:
        words1 = model.find_word(words)
        if words1 is None:
            return f"Couldn't find the word: {words}"
        words1.normalize()
        Word_class_words.append(words1)
    str_list.clear()
    for Word in Word_class_words:  # comparing similarity to each word:
        mean = 0
        for other_words in [i for i in Word_class_words if i is not Word]:
            mean += Word.similarity(other_words)
        mean_of_similarities.append((Word.text, mean))
    z_score = zscore([i[1] for i in mean_of_similarities])
    print(z_score)
    copy_mean_of_similarities = mean_of_similarities.copy()
    for i in range(len(mean_of_similarities)):
        if z_score[i] < -0.10 or z_score[i] > 1.5:
            mean_of_similarities.remove(copy_mean_of_similarities[i])
    return " ".join([i[0] for i in mean_of_similarities])


st.set_page_config(
    page_title="Wonjoon's Outlier Finder",
    page_icon="🤖"
)

st.title("Welcome to the outlier finder")

st.header("Outlier Finder")
st.caption(
    "To use outlier finder, enter words in comma seperated list, use dashes(-) to represent spaces between the same word")
outliers = st.text_input('Outlier Finder', 'apple, banana, mango, orange, car, bus, cherry').replace(" ", "")
st.subheader("Here are the results after removing the outliers")
outliers = outliers.replace("-", " ")
if len(outliers.split(',')) <= 3:
    st.write("Please enter more than 3 words")
else:
    st.write(outlier_finder(outliers.split(',')))
st.divider()
st.header("This is connection finder")
st.caption("To use connection finder, enter words to each section, then AI will try to answer the last one")
cf1 = st.text_input('This is input for A in a to b is c to d', "man", max_chars=15, label_visibility="hidden")
st.header("to")
cf2 = st.text_input('This is input for B in a to b is c to d', "king", max_chars=15, label_visibility="hidden")
st.header("is like")
cf3 = st.text_input('This is input for C in a to b is c to d', "woman", max_chars=15, label_visibility="hidden")
st.header("to")
st.subheader(a_to_b_is_like_c_to(cf1, cf2, cf3))
