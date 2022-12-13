import streamlit as st
import xlrd 
import openpyxl
import pandas as pd   
st.set_page_config(layout='wide')
team_list=['中信兄弟','樂天桃猿','富邦悍將','統一7-ELEVEn獅', 'Dragons']
option = st.sidebar.selectbox( '選擇球隊？',team_list)
if option:
  df = pd.read_excel("teamsdata.xlsx",sheet_name=team_list) 
  st.dataframe(df)
