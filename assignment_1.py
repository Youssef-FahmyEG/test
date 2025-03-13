import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

st.set_page_config(layout = "wide", page_title = "Dashboard")
st.sidebar.info("Upload (heart.csv) file")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)

gender = st.sidebar.selectbox("select a gender :" , df["sex"].unique())

tab1 , tab2 , tab3 = st.tabs(["DataFrame" , "Statistical Summary" , "Graphs"])
with tab1 :
    st.header("Dataset Overview")
    st.dataframe(df)
with tab2 :
    st.header("Statistical Summary")
    st.dataframe(df.describe())
with tab3 :
    col1 , col2 = st.columns(2)
    with col1 :
        new_df = df[df["sex"] == gender]
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize = (10, 8))
        sns.heatmap(new_df.corr(), ax = ax , annot = True, cmap = "coolwarm", fmt = ".2f")
        st.pyplot(fig , use_container_width = True)
        
        st.subheader("Age Distribution by Heart Disease")
        st.plotly_chart(px.histogram(new_df, x = "age", color = "target", color_discrete_sequence = ["blue" , "red"]) , use_container_width = True)
    with col2 :
        new_df = df[df["sex"] == gender]
        st.subheader("Heart Disease by Gender")
        st.plotly_chart(px.bar(new_df.groupby("sex")["target"].sum().reset_index(), x = "sex", y = "target", color_discrete_sequence = ["blue"]) , use_container_width = True)
        
        st.subheader("Cholesterol Levels by Heart Disease")
        st.plotly_chart(px.box(new_df, x = "target", y = "chol", color = "target"), use_container_width = True)

        
