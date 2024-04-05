from play import a_to_b_is_like_c_to, outlier_finder
import streamlit as st



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
