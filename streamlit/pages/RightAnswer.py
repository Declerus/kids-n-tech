import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import random

# Redirect user to quiz if they end up on this page without an answer.
if 'quizSelectedRightAnswer' not in st.session_state:
    switch_page("Quiz")
    st.stop()

config = st.session_state['config']
quizRightAnswerCategory = st.session_state['quizSelectedRightAnswer']['category']
quizRightAnswerCategoryImageNumber = st.session_state['quizSelectedRightAnswer']['imageNumber']

st.image("https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/images/{0}/{1}.png".format(quizRightAnswerCategory, quizRightAnswerCategoryImageNumber))


descriptions = [config['info'][quizRightAnswerCategory]['description0'],
                config['info'][quizRightAnswerCategory]['description1'],
                config['info'][quizRightAnswerCategory]['description2'],
                config['info'][quizRightAnswerCategory]['description3']]
random_description = random.choice(descriptions)

st.markdown(random_description, unsafe_allow_html=True)

next = st.button("Next quiz")
if next:
    del st.session_state['quizData']
    del st.session_state['quizSelectedRightAnswer']
    switch_page("Quiz")
