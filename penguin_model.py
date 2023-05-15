import streamlit as st 
import pandas as pd 
import seaborn as sns 
import numpy as np 
import joblib 

from PIL import Image 

st.sidebar.title('sidebar')

st.title('Streamlit Demo')
st.header('This is a sample header :)')

sbar_button = st.sidebar.button('click me please :)')

if sbar_button:
    st.sidebar.write('I hath been checkedeth')

col1, col2 = st.columns(2)
col1.subheader('col1 subheader')
col2.subheader('col2 subheader')

col21 , col22 , col23 = st.columns([
    3,2,1
])

col21.subheader('test')
col22.subheader('test')
col23.subheader('test')

col21.write('widest column, but the text here should wrap')
col22.write('this is a medium column')
col23.write('itty bitty column')

col2.write('this column has some info')

st.markdown('Markdown **syntax**')

'''
This is a test of the
Markdown Block Text thing I want to

Know about
'''

st.write(
    '<h2 style="text-align:center"> Centered with html</h2>',
    unsafe_allow_html=True
    )

check = st.checkbox('check this out lol')

button_check = st.button('is box checked')

if button_check:
    if check:
        st.write('checked nice teehee')
    else:
        st.write('no check')

animal_options = [
    'Cats','Dogs','Guinea Pigs','Bearded Dragons'
]

fav_animal = st.radio(
    'Which animal is your favorite?',
    animal_options
)

fav_btn = st.button('Submit Animal')

if fav_btn:
    st.write(f'''Your favorite animal is {
        fav_animal
        }???''')
    if fav_animal == 'Cats':
        st.write('meow meow')
    else:
        st.write('bad choice, buck-o')

fav_animal2 = st.selectbox(
    'Favorite Animal?',
    animal_options
    )

fav_btn2 = st.button('Submit Animal again')

if fav_btn2:
    st.write(f'''Your favorite animal is {
        fav_animal2
        }???''')
    if fav_animal2 == 'Cats':
        st.write('meow meow')
    else:
        st.write('bad choice, buck-o')

like_animal = st.multiselect(
    'which animals do you like?',
    animal_options
)
like_btn = st.button('Submit Animals')

if like_btn:
    st.write(like_animal)
    st.write(f'''Your first option was {
        ', '.join(like_animal)
    }''')

num_pets = st.slider(
    'how many pets you got, mama',
    min_value=1,max_value=10,
    value=2,
    step=2
)

in_text = st.text_input(
    'whut ur pet name:',
    value='grog'
)
st.write(f'pet name is {in_text}')

in_num = st.number_input(
    'whot number pbet /"',
    min_value=0.0,step=0.5
)