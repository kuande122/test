import streamlit as st 
from PIL import Image
def Guardians():  
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Guardians/Guardians.png')
    st.image(image)
  with col2:
    st.write("""## 富邦悍將""")
    st.write("""##### Fubon Guardians""")
    st.write("""##### 擁有者:富邦金控""")
    st.write("""##### 領隊:林華韋""")
    st.write("""##### 總教練:丘昌榮""")
    st.write("""##### 識別色彩:藍色""")
  st.write('俊國建設棒球隊(1989–1992年)→俊國熊(1993–1995年)→興農熊(1996年)→興農牛(1996–2012年)→義大犀牛(2013–2016年)→富邦悍將(2017–至今)')
  col1, col2 = st.columns(2)
  col1.metric("季冠軍🏆", "8  次")
  col2.metric("年度冠軍🏆", "3  次")
  st.write('富邦悍將隊（Fubon Guardians）的前身可追溯至成立於1989年的社會甲組球隊俊國建設棒球隊。俊國棒球隊進軍職棒後更名為俊國熊隊，其後歷經三次轉賣，隊名也陸續更改為興農熊隊、興農牛隊、義大犀牛隊，並曾獲得三次總冠軍。2016年季中，當時擁有義大犀牛隊的義联集團宣佈出售球隊，最後由長期贊助業餘棒運的富邦金控以新台幣3億元買下。該年季後，義大隊奪得隊史首座也是最後一座的總冠軍後，隨即自同年11月01日起改由富邦金控接手經營，並在11月15日正式公佈新隊名為富邦悍將隊。')
  st.write("2022年度歌曲 We Will Win")
  audio_file = open("Guardians/We Will Win.mp3", "rb")
  st.audio(audio_file.read()) 
  st.write("2021年度歌曲 FIGHT ON")
  audio_file = open("Guardians/FIGHT ON.mp3", "rb")
  st.audio(audio_file.read())  
  st.write("嗆司曲 超強一擊")
  audio_file = open("Guardians/超強一擊.mp3", "rb")
  st.audio(audio_file.read()) 
  
  

