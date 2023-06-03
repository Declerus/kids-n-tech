import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_click_detector import click_detector
import random
from urllib.request import urlopen
import json
import re

random.seed()

# Init config
if 'config' not in st.session_state:
    response = urlopen("https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/config.json")
    st.session_state['config'] = json.loads(response.read())
config = st.session_state['config']

# Init random categories
if 'quizData' not in st.session_state: 
    categories = random.sample(st.session_state['config']['quiz']['categories'], k=4)
    categoriesImageNumber = list(map(lambda x: random.randint(1, config['info'][x]['numberOfImages']), categories))
    st.session_state['quizData'] = {
        "categories": categories,
        "categoriesImageNumber": categoriesImageNumber,
        "rightAnswer": random.randint(0, 3)
    }

quizData = st.session_state['quizData']

if 'quizSelectedImage' not in st.session_state:
    st.session_state['quizSelectedImage'] = ''
quizSelectedImage = st.session_state['quizSelectedImage']

content = '''
    <style>
        [data-clicked="true"] {{
            border: 5px solid green;
        }}
        [data-clicked=""] {{
            border: 5px solid black;
        }}
        
        .image {{
            width: 256px;
            height: 256px;
            object-fit: cover;
        }}
    </style>
    <div>
    <a href='#' id='Image 0'><img data-clicked="{isImage0Clicked}" class="image" src='https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/images/{category1}/{category1ImageNumber}.png'></a>
    <a href='#' id='Image 1'><img data-clicked="{isImage1Clicked}" class="image" src='https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/images/{category2}/{category2ImageNumber}.png'></a>
    <a href='#' id='Image 2'"><img data-clicked="{isImage2Clicked}" class="image" src='https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/images/{category3}/{category3ImageNumber}.png'></a>
    <a href='#' id='Image 3'"><img data-clicked="{isImage3Clicked}" class="image" src='https://raw.githubusercontent.com/JoseeGagne/kids-n-tech-images/main/images/{category4}/{category4ImageNumber}.png'></a>
    </div>
    '''.format(
        category1=quizData['categories'][0],
        category2=quizData['categories'][1],
        category3=quizData['categories'][2],
        category4=quizData['categories'][3],
        category1ImageNumber=quizData['categoriesImageNumber'][0],
        category2ImageNumber=quizData['categoriesImageNumber'][1],
        category3ImageNumber=quizData['categoriesImageNumber'][2],
        category4ImageNumber=quizData['categoriesImageNumber'][3],
        isImage0Clicked="true" if st.session_state.quizSelectedImage == "Image 0" else "", 
        isImage1Clicked="true" if st.session_state.quizSelectedImage == "Image 1" else "", 
        isImage2Clicked="true" if st.session_state.quizSelectedImage == "Image 2" else "",
        isImage3Clicked="true" if st.session_state.quizSelectedImage == "Image 3" else ""
    )

st.markdown("""## Select the {0}.""".format(quizData['categories'][quizData['rightAnswer']]))

click_detector(content, key="quizSelectedImage")

if (quizSelectedImage):
    confirm = st.button("Confirm")  
    selectedAnswer = int(re.search('(\d)', quizSelectedImage).group(1))
    
    if confirm:
        if selectedAnswer == quizData['rightAnswer']:
            st.session_state['quizSelectedRightAnswer'] = {
                "category": quizData['categories'][selectedAnswer],
                "imageNumber": quizData['categoriesImageNumber'][selectedAnswer]
            }
            switch_page("RightAnswer")
        else:
            st.markdown("This is a {0}. Please try again.".format(quizData['categories'][selectedAnswer]))
