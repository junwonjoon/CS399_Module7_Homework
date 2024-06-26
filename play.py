"""
    Remove Outliers from a list of words using streamlit UI.
    Author: Wonjoon Jun
"""
from wv import Model
from scipy.stats import zscore
# file_location = "https://git-lfs.github.com/spec/v1 oid sha256:547da2eee78754dc6bac050dd17972f20bdab7db0e106f7daa4d948c7fa3c01e size 259366712"
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
        if z_score[i] < -0.2 or z_score[i] > 1.5:
            mean_of_similarities.remove(copy_mean_of_similarities[i])
    return " ".join([i[0] for i in mean_of_similarities])


if __name__ == "__main__":
    print(outlier_finder(["Earth", "apple", "mango", "banana"]))
    print(a_to_b_is_like_c_to("wine", "France", "pasta"))
