
import streamlit as st
import json

# Init config
if 'config' not in st.session_state:
    with open("config.json", 'r') as file:
        st.session_state['config'] = json.load(file)

config = st.session_state['config']

st.markdown(config['info']['mouse']['description3'],
    unsafe_allow_html=True)
