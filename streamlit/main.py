import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown(f"Welcome to Tech-N-Quiz")

start = st.button("Start Quiz")
if start:
    switch_page("Quiz")