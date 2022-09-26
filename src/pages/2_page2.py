import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))
    return df
dataframe = rand_df(c=3, r=10)

st.line_chart(dataframe)
