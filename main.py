import streamlit as st
import xlrd 
import openpyxl
import pandas as pd   
from PIL import Image
import Brothers
st.set_page_config(layout='wide')
team_list={'中信兄弟','樂天桃猿','富邦悍將','統一7-ELEVEn獅', '味全龍','台鋼雄鷹'}

def user(option):
  option = st.sidebar.selectbox( '選擇球隊？', option)
  df = pd.read_excel("teamsdata.xlsx",sheet_name=option) 
  st.dataframe(df)
  return option
st.write(user(option))
