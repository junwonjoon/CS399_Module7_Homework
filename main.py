import streamlit as st
from math import sqrt
from time import process_time


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

    def similarity(self, w) -> float:
        return self * w

    def __add__(self, w):
        return Word("", [x + y for x, y in zip(self.vector, w.vector)])

    def __sub__(self, w):
        return Word("", [x - y for x, y in zip(self.vector, w.vector)])

    def __mul__(self, w) -> float:
        return sum([x * y for x, y in zip(self.vector, w.vector)])


class Model(list):
    """ Represents a model, a list of words"""
    features = 300

    def __init__(self, inp_file_name: str) -> None:
        super().__init__()
        print(f"Loading model from {inp_file_name} ...")
        t0 = process_time()
        with open(inp_file_name, mode="r", encoding="utf8") as inp_file:
            for line in inp_file:
                sa = line.split(" ")
                self.append(Word(sa[0], [float(x) for x in sa[1:]]))
        print(f"Loaded in {process_time() - t0} secs")

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


from scipy.stats import zscore


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
    Word_class_words = []
    mean_of_similarities = []
    for words in str_list:
        words1 = model.find_word(words)
        if words1 is None:
            return f"Couldn't find the word: {words}"
        words1.normalize()
        Word_class_words.append(words1)
    str_list.clear()

    # comparing similarity to each word:
    for Word in Word_class_words:
        mean = 0
        for other_words in Word_class_words:
            if other_words is not Word:
                mean += Word.similarity(other_words)
        mean_of_similarities.append((Word.text, mean))
    z_score = zscore([i[1] for i in mean_of_similarities])

    copy_mean_of_similarities = mean_of_similarities.copy()
    for i in range(len(mean_of_similarities)):
        if z_score[i] < -0.2 or z_score[i] > 1.3:
            mean_of_similarities.remove(copy_mean_of_similarities[i])
            i -= 1
    return " ".join([i[0] for i in mean_of_similarities])


if __name__ == "__main__":
    print(outlier_finder(["Earth", "apple", "mango", "banana"]))
    print(a_to_b_is_like_c_to("wine", "France", "pasta"))

model = Model("glove_git.txt")

st.set_page_config(
    page_title="Wonjoon's Outlier Finder",
    page_icon="🤖"
)

st.title("Welcome to the outlier finder")

st.header("This is outlier finder")
st.caption("To use outlier finder, enter words in comma seperated list")
outliers = st.text_input('Outlier Finder', 'apple').replace(" ", "")
st.write(outlier_finder(outliers.split(',')))

st.divider()
st.header("This is connection finder")
st.caption("To use connection finder, enter words to each section, then AI will try to answer the last one")
cf1 = st.text_input('', "Berlin", max_chars=15)
st.header("to")
cf2 = st.text_input('', "Germany", max_chars=15)
st.header("is like")
cf3 = st.text_input('', "Paris", max_chars=15)
st.header("to")
st.write(a_to_b_is_like_c_to(cf1, cf2, cf3))
