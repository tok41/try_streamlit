import streamlit as st
import pandas as pd
import numpy as np
import scipy
import plotly.graph_objects as go
import plotly.express as px

st.title("Normal Distribution")


# *** sidebar
st.sidebar.title('パラメータ設定')
st.sidebar.markdown("""
## 正規分布のパラメータ

$\mathcal{N}(\mu, \sigma^2)$
""")
param_mu = st.sidebar.slider(label="mean", min_value=-10.0, max_value=10.0, step=0.01, value=0.0)
param_var = st.sidebar.slider(label="var", min_value=0.01, max_value=20.0, step=0.01, value=1.0)
sample_size = st.sidebar.number_input(label="sample_size", min_value=1, step=1, value=100)


# *** main contents
st.markdown("""
## 正規分布の確率密度関数
""")

@st.cache
def norm_pdf(mu, var):
    x = np.linspace(-10., 10., 1000)
    y = scipy.stats.norm(loc=mu, scale=np.sqrt(var)).pdf(x)
    df = pd.DataFrame.from_dict({"x": x, "y": y})
    return df

st.text(f"N(mu={param_mu}, var={param_var})")
df = norm_pdf(mu=param_mu, var=param_var)
st.line_chart(df, x="x", y="y")


st.markdown("""
## 正規分布からサンプル
""")

@st.cache
def norm_rvs(mu, var, n):
    x = scipy.stats.norm(loc=mu, scale=np.sqrt(var)).rvs(n)
    df = pd.DataFrame.from_dict({"x": x})
    return df

df = norm_rvs(mu=param_mu, var=param_var, n=int(sample_size))
fig = px.histogram(df, x="x", nbins=50)
st.plotly_chart(fig)
