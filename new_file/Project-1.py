
import streamlit as st
import pandas as pd
import numpy as np


st.title('HOME')

r = st.sidebar.radio('Navigation',['Home','Opration'])
r = st.selectbox('COLORS',["R",'Y','B','Green'],index=2)


if r =='Home':
    st.write('welcome')
    st.balloons()
    st.success('SUCCESSS!!!')
    st.error('Error')
    st.warning('warning')
    st.info('info')
    st.exception('exception')


