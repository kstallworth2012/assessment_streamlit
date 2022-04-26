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
# import plotly.express as px

from eda_app import run_eda_app
from ml_app import run_ml_app



def main():

        st.title("Assessment in Streamlit")
        menu = ["HOME","EDA","ML","ABOUT"]
        choice=st.sidebar.selectbox("Assessment Menu",menu)

        if choice == "HOME":
            st.subheader("Home")
            st.header("Be sure to consider the following:")
                #
#                 st.write("What's the best length of time to run a campaign? 90.96")
            st.metric(label='Best Length of Time',value=90.96,delta=None)
#                 st.write("What's the ideal pledge goal?")
#                 st.write(" What type of projects would be most successful at getting funded? design")
            st.metric(label='Project Most\n Likely Funded',value='Design',delta=None)
#                 st.write("Is there an ideal month/day/time to launch a campaign sunday january 1 4:59 pm or weekend summertime")
            st.metric(label='Ideal Launch Time',value='Sunday january 1, 2012 4:59PM',delta=None)
            successful=df[df['status'].isin(['successful'])].groupby(['status','category','pledged'])['pledged'].mean()
                # successful.sort_values(by=['pledged'])
            st.dataframe(successful)
            avg_cat_funded_success = df[df['status'].isin(['successful'])].groupby(['status','category'])['pledged'].mean()
            avg_goal_funded_success = df[df['status'].isin(['successful'])].groupby(['status','goal'])['pledged'].mean()
                # st.table(avg_goal_funded_success.value_counts())
            avg=avg_goal_funded_success.value_counts()
                # avg_cat_funded_success.plot(kind="pie")
            funded_dates = df['funded date'].value_counts()
            st.dataframe(funded_dates)
                 
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

