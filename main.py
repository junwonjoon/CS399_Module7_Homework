from play import a_to_b_is_like_c_to, outlier_finder
import streamlit as st

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
