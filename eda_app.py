import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px




#load data but cache it first
@st.cache
def load_data(data):
        df = pd.read_csv(data,encoding_errors='ignore')
        return df




def run_eda_app():


    st.header("Exploratory Data Analysis")
    df = load_data("DSI_kickstarterscrape_dataset.csv")
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()


    s_menu = ['Descriptive','Plots']
    submenu = st.sidebar.selectbox("Submenu",s_menu)
#     another_submenu = st.sidebar.selectbox('Another Menu',categorical_cols)
    if submenu == "Descriptive":
                st.write("HELLO!")
      with st.expander("By Location"):
            st.dataframe(df['location'].value_counts())
            local_menu = df['location'].unique().tolist()
            mylocalBox=st.selectbox('Location box',local_menu)
            loc_df = df[df['location'] ==mylocalBox]
            st.dataframe(loc_df)
            me = px.pie(df[df['location'] ==mylocalBox],names='status', values='pledged')
            st.plotly_chart(me,use_container_width=True)
#             me2 = px.pie(df[df['location'] ==mylocalBox],names='subcategory', values='backers')
#             st.plotly_chart(me2,use_container_width=True)

            fig = px.scatter(df[df['location'] ==mylocalBox], x="goal", y="pledged",
            size="pledged", color="category",
                 hover_name="name", log_x=True, size_max=60)
            st.plotly_chart(fig)


            fig2 = px.sunburst(df[df['location'] ==mylocalBox], path=['status','category', 'subcategory', 'location','name'], values='pledged', color='category')
            st.plotly_chart(fig2)
