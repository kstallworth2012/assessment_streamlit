import streamlit as st
#Must do this first in Streamlit
st.set_page_config(page_title='My Assessment',
page_icon=':smiley',layout='wide',
initial_sidebar_state='collapsed') #initial_sidebar_state='collapsed 'expanded or auto
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px

from eda_app import run_eda_app
from ml_app import run_ml_app



def main():

        st.title("Assessment in Streamlit")
        menu = ["HOME","EDA","ML","ABOUT"]
        choice=st.sidebar.selectbox("Assessment Menu",menu)

        if choice == "HOME":
            st.subheader("Home")
                 
        elif choice == "EDA":
            run_eda_app()

        elif choice == "ML":
            run_ml_app()
            
        elif choice == "ABOUT":
            st.subheader("About")

        else:
            pass





if __name__ == '__main__':
    main()

