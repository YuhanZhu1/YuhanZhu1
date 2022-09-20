import streamlit as st
import seaborn as sns
import plotly.express as px


iris = px.data.iris()
plot = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_width', color='species'
,title="Iris Dataset: A 3D Scatter Plot about")

st.plotly_chart(plot, use_container_width=False, sharing="streamlit", title="Iris Dataset: A 3D Scatter Plot about")