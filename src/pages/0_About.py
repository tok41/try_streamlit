import streamlit as st

st.title("About this app")

st.markdown('''
## このAppについて
これはMultiPageAppを作るためのテストページだよ。

中身はまだない。

## 自己紹介

エンジニアをやっています。

[@toichi_t](https://twitter.com/yoichi_t)
''')

# *** sidebar
st.sidebar.title('About')
st.sidebar.markdown("""
このAppについて
""")
