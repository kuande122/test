import streamlit as st 
from PIL import Image
def Rakuten():  
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Rakuten/Rakuten.png')
    st.image(image)
  with col2:
    st.write("""## 樂天桃猿""")
    st.write("""##### Rakuten Monkeys""")
    st.write("""##### 擁有者:樂天株式會社""")
    st.write("""##### 領隊:浦韋青""")
    st.write("""##### 總教練:曾豪駒""")
    st.write("""##### 識別色彩:酒紅色""")
  st.write('台北太陽隊、高屏雷公隊(1997-2002年)→第一金剛隊(2003年)→La New熊隊(2004-2010年)→Lamigo桃猿隊(2011-2019年)→樂天桃猿隊(2020-至今)')
  col1, col2 = st.columns(2)
  col1.metric("季冠軍🏆", "14  次")
  col2.metric("年度冠軍🏆", "7  次")
  st.write('2019年07月03日，甫達成季冠軍五連霸的Lamigo桃猿隊於選秀會結束後，突如其來宣佈因不堪連年經營虧損，決定轉賣球隊，也震撼了原先尚在歡慶味全龍隊重返職棒的中華職棒。09月19日，桃猿隊正式宣佈將經營權完全轉售予已在日本職棒擁有東北樂天金鷲隊的日商樂天集團，結束16年職棒經營事業，樂天也向桃猿保證，接手後大高熊育樂股份有限公司（經營桃猿隊）、大桃猿育樂股份有限公司（經營桃園國際棒球場）的球隊相關工作人員都會予以留用。')
  st.write("2022年度歌曲 Rise Up")
  audio_file = open("Rakuten/Rise Up.mp3", "rb")
  st.audio(audio_file.read()) 
  st.write("2021年度歌曲 一起更強")
  audio_file = open("Rakuten/一起更強.mp3", "rb")
  st.audio(audio_file.read())  
  st.write("嗆司曲 超越夢想")
  audio_file = open("Rakuten/超越夢想.mp3", "rb")
  st.audio(audio_file.read()) 





