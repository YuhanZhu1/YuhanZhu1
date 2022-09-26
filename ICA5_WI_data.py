import pandas as pd
import seaborn as sns
import streamlit as st

#First load the data

data = pd.read_csv('WIdata.csv')
#data.head()

st.title("Welcome to Yuhan's ICA5-web-app")
home = st.sidebar.button("About the data")
if home:
    st.markdown("""
            The data we are analysizing and visulazing is the *Breast Cancer Wisconsin (Diagnostic) Data Set*
            from here kaggle [link](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
            `https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data`)

            We will use `Pandas` to performe IDA and EDA, then using only `Seaborn` to plot them. 
            Let's start
            """)



dis = st.sidebar.button("Distribution Plot")
if dis:
    st.write("Area mean distributation")
    fig1 = sns.displot(data, x="area_mean",hue="diagnosis",element="step")
    st.pyplot(fig1)

joint = st.sidebar.button("Jointplot")

if joint:
    st.write("Area mean vs concavity mean joint plot")
    fig2 = sns.jointplot(data=data,x = "area_mean",y = "concavity_mean",hue="diagnosis")
    st.pyplot(fig2)