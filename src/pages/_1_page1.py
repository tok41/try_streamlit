import streamlit as st
import pandas as pd
import numpy as np
import scipy
import plotly.graph_objects as go

st.title("sample page 1")


# *** sidebar
st.sidebar.title('パラメータ設定')
st.sidebar.markdown("""
## ベータ分布のパラメータ

$\mathrm{Beta}(a, b)$
""")
param_a = st.sidebar.slider(label="a", min_value=0.01, max_value=10.0, step=0.01, value=2.0)
param_b = st.sidebar.slider(label="b", min_value=0.01, max_value=10.0, step=0.01, value=2.0)

st.sidebar.markdown("""
## ディリクレ分布のパラメータ

$\mathrm{Dir}( \\mathbf{\\alpha}=[a1, a2, a3] )$
""")

alpha1 = st.sidebar.slider(label="a1", min_value=0.01, max_value=10.0, step=0.01, value=2.0)
alpha2 = st.sidebar.slider(label="a2", min_value=0.01, max_value=10.0, step=0.01, value=2.0)
alpha3 = st.sidebar.slider(label="a3", min_value=0.01, max_value=10.0, step=0.01, value=2.0)


# *** main contents
st.markdown("""
## ベータ分布の確率密度関数
""")

@st.cache
def rand_beta(a=1.0, b=1.0):
    x = np.linspace(0.001, 1.0-0.001, 100)
    y = scipy.stats.beta(a=a, b=b).pdf(x)
    df = pd.DataFrame.from_dict({"x": x, "y": y})
    return df

st.text(f"Beta(a={param_a}, b={param_b})")
df = rand_beta(a=param_a, b=param_b)
st.line_chart(df, x="x", y="y")

# st.dataframe(df)


st.markdown("""
## ディリクレ分布の確率密度関数
""")

@st.cache
def get_dirichlet_pdf(alpha=[2.0, 2.0, 2.0]):
    def get_dirichlet_pdf_point(x, alpha):
        if np.min(x) <= 0:
            return np.nan
        return scipy.stats.dirichlet.pdf(x, alpha)

    N=100
    x1 = np.linspace(0, 1, N)[1:N-1]
    x2 = np.linspace(0, 1, N)[1:N-1]
    xx1, xx2 = np.meshgrid(x1, x2)
    xx3 = 1.0 - (xx1 + xx2)
    l = len(x1)
    res_xx1 = xx1.reshape(l*l)
    res_xx2 = xx2.reshape(l*l)
    res_xx3 = xx3.reshape(l*l)

    pdfs = np.array(
        [
            get_dirichlet_pdf_point([s1,s2,s3], alpha) 
            for (s1, s2, s3) in zip(res_xx1, res_xx2, res_xx3)
        ]
    )
    pdfs = pdfs.reshape(l,l)
    return pdfs, x1, x2

alpha = [alpha1, alpha2, alpha3]
pdfs, x1, x2 = get_dirichlet_pdf(alpha)

st.text(f"Dir(alpha={alpha})")
fig = go.Figure(data=[go.Surface(z=pdfs, x=x1, y=x2)])
#fig.update_layout(title='Dirichlet distribution', autosize=True)
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=-1.5, y=-1.5, z=0.5)
)
fig.update_layout(scene_camera=camera, title="Dirichlet distribution")
st.plotly_chart(fig, use_container_width=True)
