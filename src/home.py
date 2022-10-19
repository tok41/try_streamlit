import streamlit as st
import pandas as pd
import numpy as np

st.title("Multipage Sample")
st.header('こんにちは 世界')

st.markdown('''
こんにちは！

これはStreamlitMultiPageAppのテストです。
Multipageについては、下記サイトを参照してください。

- https://docs.streamlit.io/library/get-started/multipage-apps
- https://blog.streamlit.io/introducing-multipage-apps/
''')

# *** sidebar
st.sidebar.image('asset/neko.png', use_column_width=True)
