
import streamlit as st
import pandas as pd
import numpy as np


st.title('HOME')

r = st.sidebar.radio('Navigation',['Home','Opration'])
sb = st.selectbox('COLORS',["R",'Y','B','G'],index=2)

data = {
'num':[x for x in range(1,11)],
'square':[x**2 for x in range(1,11)],
'twice':[x*2 for x in range(1,11)],
'thrice':[x*3 for x in range(1,11)],
}
if r=='Opration':
    df = pd.DataFrame(data)
    col = st.sidebar.selectbox('Select any number',df.columns)


  
    ax.set_title(f'Plot of {col} vs num')
    ax.set_xlabel('num')
    ax.set_ylabel(col)

    st.pyplot(fig)
if r =='Home':
    st.write('welcome')
    st.balloons()
    st.success('SUCCESSS!!!')
    st.error('Error')
    st.warning('warning')
    st.info('info')
    st.exception('exception')


