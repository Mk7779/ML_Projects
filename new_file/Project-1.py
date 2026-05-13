
import streamlit as st
import pandas as pd
import numpy as np


st.title('HOME')
st.write('welcome')
st.balloons()
st.success('SUCCESSS!!!')
st.error('Error')
st.warning('warning')
st.info('info')
st.exception('exception')

r = st.sidebar.radio('Navigation',['Home','Opration'])



if r =='Home':
    st.write('welcome')
    st.balloons()
    st.success('SUCCESSS!!!')
    st.error('Error')
    st.warning('warning')
    st.info('info')
    st.exception('exception')
if r=="Operation":
    st.write("This is Option")

