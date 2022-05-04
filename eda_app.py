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
    another_submenu = st.sidebar.selectbox('Another Menu',categorical_cols)

