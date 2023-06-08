import streamlit as st
from streamlit_extras.switch_page_button import switch_page


# Redirect user to quiz if they end up on this page without an answer.
if 'quizSelectedRightAnswer' not in st.session_state:
    switch_page("Quiz")
    st.stop()

config = st.session_state['config']
quizRightAnswerCategory = st.session_state['quizSelectedRightAnswer']['category']
quizRightAnswerCategoryImageNumber = st.session_state['quizSelectedRightAnswer']['imageNumber']

st.image("https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/images/{0}/{1}.png".format(quizRightAnswerCategory, quizRightAnswerCategoryImageNumber))


st.markdown("{0}"
            .format(
                config['info'][quizRightAnswerCategory]['description'])
            )

next = st.button("Next quiz")
if next:
    del st.session_state['quizData']
    del st.session_state['quizSelectedRightAnswer']
    switch_page("Quiz")
