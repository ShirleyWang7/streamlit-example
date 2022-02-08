from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import numpy as np



df1 = pd.DataFrame(
    np.random.randint(0,100,(5,5)),
    columns=['a','b','c','d','e'])

st.write(df1)

st.line_chart(df1)

