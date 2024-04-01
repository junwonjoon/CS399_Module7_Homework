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
st.write(a_to_b_is_like_c_to("wine", "France", "pasta"))
