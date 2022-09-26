import streamlit as st

st.title("note")

st.markdown('''
## neko

ネコはかわいい

## sidebarに表示されるページの順序について

詳細は[公式ドキュメント](https://docs.streamlit.io/library/get-started/multipage-apps#how-pages-are-labeled-and-sorted-in-the-ui)を参照。

### ファイル名の構成要素

以下のような構成でファイル名が記載されると期待されている。

```
{prefix}_{label}.py
```

- prefix: 数値
- separator: `_`, `-`, (space)
- label: prefixを除いた文字列

### 表示順序

1. prefixがあれば、prefix（数値）でソート
2. prefixがなければ、labelでソート
    - label部分に数値があっても、prefixではないのでその値でソートはされない

### 表示ページ名

separatorはスペースに変換れて、labelが表示される。
このとき、prefixは削除される。

```
e.g. [1_sample_1.py] -> [sample 1]
```

先頭に数値を持ってきたい場合には、prefixを付けるか、`_`などのseparatorを追加する。

```
e.g. [_1_sample.py] -> [1 sample]
```

こんな感じ。
''')

# *** sidebar
st.sidebar.title('note')
st.sidebar.markdown("""
メモ
""")
