import streamlit as st
st.set_page_config(layout='wide',inital_sidebar_state='expanded')
team_list=['中信兄弟','樂天桃猿','富邦悍將','台鋼雄鷹','統一7-ELEVEn獅', '味全龍']
option = st.sidebar.selectbox( '選擇球隊？',team_list)
