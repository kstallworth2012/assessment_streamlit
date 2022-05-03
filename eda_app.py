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
    if submenu == "Descriptive":
        st.dataframe(df)

        with st.expander("Data Columns"):
            st.dataframe(df.columns)

        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())

        with st.expander("Category Distribution"):
            st.dataframe(df['category'].value_counts())
            cat_menu = df['category'].unique().tolist()
            myCatBox=st.selectbox('Cat box',cat_menu)

        with st.expander("Sub Category Distribution"):
            st.dataframe(df['subcategory'].value_counts())

        with st.expander("Funded Data Distribution"):
            st.dataframe(df['funded date'].value_counts())


        with st.expander("Backer counts"):
            st.dataframe(df['backers'].value_counts())

        with st.expander("Duration counts"):
            st.dataframe(df['duration'].value_counts())

        with st.expander("Goal counts"):
            st.dataframe(df['goal'].value_counts())

        with st.expander("pledged counts"):
            st.dataframe(df['pledged'].value_counts())
            fig = plt.figure()
            sns.countplot(df['pledged'].value_counts())
            st.pyplot(fig)

        with st.expander("funded percentage counts"):
            st.dataframe(df['funded percentage'].value_counts())


        with st.expander("Info"):
            st.dataframe(df.info())


    elif submenu == "Plots":
        st.subheader('Plots')
                #layouts
        col1,col2 = st.columns([2,1])
        with st.expander("Histogram of Project Duration"):
            duration_hist = sns.displot(x='duration',data=df,kde=True)
            st.pyplot(duration_hist)
        with col1:
            with st.expander('Status counts plot'):
                fig = plt.figure()
                sns.countplot(df['status'])
                st.pyplot(fig)

                status_df = df['status'].value_counts().to_frame()
                status_df = status_df.reset_index()
                status_df.columns = ["Status","Status Counts"]
                st.dataframe(status_df)

                # using plotly_chart
                p1 = px.pie(status_df,names='Status', values='Status Counts')
                st.plotly_chart(p1,use_container_width=True)

        #
        # with st.expander('Dist plot of funded dates'):
        #         # fig2 =  plt.figure()
        #         # sns.countplot(df['funded date'])
        #         # st.pyplot(fig2)


        with col2:
            with st.expander('Status Counts Distribution'):
                st.dataframe(status_df)

            with st.expander("Fund date counts"):
                st.dataframe(df['funded date'].value_counts())

            with st.expander("stuff"):
                # st.dataframe(df['backers'])
                p2 = px.bar(df['backers'])
                st.plotly_chart(p2)

        st.code('''
        import streamlit as st
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from PIL import Image
# import plotly.express as px




#load data but cache it first
@st.cache
def load_data(data):
        df = pd.read_csv(data,encoding_errors='ignore')
        return df




def run_eda_app():


    st.header("Exploratory Data Analysis")
    df = load_data("DSI_kickstarterscrape_dataset.csv")


    s_menu = ['Descriptive','Plots']
    submenu = st.sidebar.selectbox("Submenu",s_menu)

    if submenu == "Descriptive":
        st.dataframe(df)

        with st.expander("Data Columns"):
            st.dataframe(df.columns)

        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe())

        with st.expander("Category Distribution"):
            st.dataframe(df['category'].value_counts())

        with st.expander("Sub Category Distribution"):
            st.dataframe(df['subcategory'].value_counts())

        with st.expander("Funded Data Distribution"):
            st.dataframe(df['funded date'].value_counts())


        with st.expander("Backer counts"):
            st.dataframe(df['backers'].value_counts())

        with st.expander("Duration counts"):
            st.dataframe(df['duration'].value_counts())

        with st.expander("Goal counts"):
            st.dataframe(df['goal'].value_counts())

        with st.expander("pledged counts"):
            st.dataframe(df['pledged'].value_counts())

        with st.expander("funded percentage counts"):
            st.dataframe(df['funded percentage'].value_counts())


        with st.expander("Info"):
            st.dataframe(df.info())


    elif submenu == "Plots":
        st.subheader('Plots')
                #layouts
        col1,col2 = st.columns([2,1])
        # with st.expander("Histogram of Project Duration"):
        #     # duration_hist = sns.displot(x='duration',data=df,kde=True)
        #     # st.pyplot(duration_hist)
        with col1:
            with st.expander('Status counts plot'):
                fig = plt.figure()
                sns.countplot(df['status'])
                st.pyplot(fig)

                status_df = df['status'].value_counts().to_frame()
                status_df = status_df.reset_index()
                status_df.columns = ["Status","Status Counts"]
                st.dataframe(status_df)

                # using plotly_chart
                p1 = px.pie(status_df,names='Status', values='Status Counts')
                st.plotly_chart(p1,use_container_width=True)

        #
        # with st.expander('Dist plot of funded dates'):
        #         # fig2 =  plt.figure()
        #         # sns.countplot(df['funded date'])
        #         # st.pyplot(fig2)


        with col2:
            with st.expander('Status Counts Distribution'):
                st.dataframe(status_df)

            with st.expander("Fund date counts"):
                st.dataframe(df['funded date'].value_counts())

            with st.expander("stuff"):
                # st.dataframe(df['backers'])
                p2 = px.bar(df['backers'])
                st.plotly_chart(p2)
        ''')
