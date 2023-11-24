import pandas as pd
import numpy as np
import streamlit as st
import plotly_express as px

st.set_page_config(page_title="Tips Dashboard",page_icon=None,layout="wide",initial_sidebar_state="expanded")
df =  pd.read_csv("tips.csv")

st.write("Hello world!")

st.sidebar.header("Tips Dashboard")
st.sidebar.image("image2.jpg")
st.sidebar.write("This dashboard is using Waiter's tips data for educational purposes")

st.sidebar.markdown("Made with :heart_eyes: by [Mohammed HSAINI](https://www.linkedin.com/in/mohammed-hsaini-88630b178/)")

st.sidebar.write("Filter The Data:")
cat_filter= st.sidebar.selectbox("Categorical filtering",[None,'sex','smoker','day','time'])
num_filter= st.sidebar.selectbox("Numerical filtering",[None,'total_bill','tip'])
row_filter= st.sidebar.selectbox("Row filtering",[None,'sex','smoker','day','time'])
col_filter= st.sidebar.selectbox("Column filtering",[None,'sex','smoker','day','time'])
##row a
a1,a2,a3,a4 = st.columns(4)

a1.metric("Max.Total bill",df['total_bill'].max())
a2.metric("Max.Total bill",df['tip'].max())
a3.metric("Max.Total bill",df['total_bill'].min())
a4.metric("Max.Total bill",df['tip'].min())

st.subheader("Total bill vs Tips")
fig = px.scatter(df,x='total_bill',
                 y='tip',
                 color=cat_filter,
                 size=num_filter,
                 facet_row=row_filter,
                 facet_col=col_filter)

st.plotly_chart(fig,use_container_width=True)


c1,c2,c3=st.columns((4,3,3))

with c1:
    st.text("Sex VS Total Tips")
    fig = px.bar(df,x='sex',y='total_bill',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
with c2:
    st.text("Smoker/Non Smoker VS Total Tips")
    fig = px.pie(df,names='smoker',values='tip',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
with c3:
    st.text("Days VS Total Tips")
    fig = px.pie(df,names='day',values='tip',color=cat_filter,hole=0.4)
    st.plotly_chart(fig,use_container_width=True)