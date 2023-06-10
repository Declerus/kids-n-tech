import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown(
    """
    <style>
    .stApp {
       background: rgb(34,193,195);
        background: linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(253,187,45,1) 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("# Welcome to Tech-N-Quiz")

st.markdown(
    """
    <div class="center-images">
        <img src="https://github.com/JoseeGagne/kids-n-tech-images/blob/main/images/garcon%20copy.png?raw=true" alt="garcon" width="200">
        <img src="https://github.com/JoseeGagne/kids-n-tech-images/blob/main/images/fille%20copy.png?raw=true" alt="fille" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("***")

start = st.button("Start Quiz")
if start:
    switch_page("Quiz")
