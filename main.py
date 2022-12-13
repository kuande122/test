import streamlit as st
import xlrd 
import pandas as pd   
st.set_page_config(layout='wide')
team_list=['中信兄弟','樂天桃猿','富邦悍將','台鋼雄鷹','統一7-ELEVEn獅', '味全龍']
option = st.sidebar.selectbox( '選擇球隊？',team_list)
df = pd.read_excel("teamsdata.xlsx") 
