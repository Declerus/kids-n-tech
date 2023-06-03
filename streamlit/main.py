import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown(f"Welcome to Tech-N-Quiz")
image = st.image("garcon.png")
image = st.image("fille.png")

start = st.button("Start Quiz")
if start:
    switch_page("Quiz")
