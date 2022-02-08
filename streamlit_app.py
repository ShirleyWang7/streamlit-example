from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image


st.title("APP Title")

st.header("APP Name Undecided")


df1 = pd.DataFrame(
    np.random.randint(0,100,(5,5)),
    columns=['a','b','c','d','e'])

st.write(df1)

st.table(df1)

st.line_chart(df1)

st.bar_chart(df1)

input1 = st.button("Please enter your name")

choice1 = st.radio("What is your age?",("under 18","18 to 29", "30 to 40", "above 40"))

#image = Image.open('sunrise.jpg')
#st.image(image, caption = 'figure 1')

col1,col2 = st.columns(2)

with st.container():
    
    st.write("Within Container")
    
    st.area_chart(df1)
    
    st.write("Outside Container")
    
 

gender = st.text_input('Gender')
if not gender:
  st.warning('Please enter a valid gender')
  st.stop()
st.success('Thanks!')

st.help(df1)

st.experimental_show(df1)

df2 = pd.DataFrame(
    np.random.randint(100,500,(5,5)),
    columns=['Col 1','Col 2','Col 3','Col 4','Col 5'])

table1 = st.table(df1)
table1.add_rows(df2)




