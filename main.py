import streamlit as st
import xlrd 
import openpyxl
import pandas as pd   
from PIL import Image
import Brothers
st.set_page_config(layout='wide')
team_list={'中信兄弟','樂天桃猿','富邦悍將','統一7-ELEVEn獅', '味全龍','台鋼雄鷹'}
#df = pd.read_excel("teamsdata.xlsx",sheet_name=option) 
#st.dataframe(df)
def user():
  option = st.sidebar.selectbox( '選擇球隊？',team_list)
  return option
user=user()
user


