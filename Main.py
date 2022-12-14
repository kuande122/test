import streamlit as st  
import xlrd 
import openpyxl
import pandas as pd
import plost
import matplotlib.pyplot as plt
import teams_information
import teams_map
from PIL import Image

st.set_page_config(layout="wide")
st.title('NBA資訊面板系統')

st.sidebar.header('請選擇區域及球隊')
area_list={'Atlantic':['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers','Toronto Raptors'],
           'Central':['Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks'],
           'Southeast':['Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'],
           'Northwest':['Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder','Portland Trail Blazers','Utah Jazz'],
           'Pacific':['Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns','Sacramento Kings'],
           'Southwest':['Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans','San Antonio Spurs']}
option_area = st.sidebar.selectbox('選擇區域？',area_list)
option = st.sidebar.selectbox('選擇球隊？',area_list[option_area])


legend_list={'Boston Celtics':{'Bill Russell','Larry Bird','Paul Pierce'},'Brooklyn Nets':{'Julius Erving','Jason Kidd','Derrick Coleman'},'New York Knicks':{'Walt Frazier','Patrick Ewing','Willis Reed'},
            'Philadelphia 76ers':{'Charles Barkley','Allen Iverson','Wilt Chamberlain'},'Toronto Raptors':{'Kyle Lowry','Chris Bosh','Vince Carter'},'Chicago Bulls':{'Michael Jordan','Dennis Rodman','Scottie Pippen'},
            'Cleveland Cavaliers':{'LeBron James','Kevin Love','Kyrie Irving'},'Detroit Pistons':{'Isiah Thomas','Ben Wallace','Grant Hill'},'Indiana Pacers':{'Reggie Miller','Metta World Peace','Chuck Person'},
            'Milwaukee Bucks':{'Sidney Moncrief','Giannis Antetokounmpo','Glenn Robinson'},'Golden State Warriors':{'Tim Hardaway','Klay thompson','Stephen Curry'},'Los Angeles Clippers':{'Bob McAdoo','Blake Griffin','Elton Brand'},
            'Los Angeles Lakers':{'Magic Johnson',"Shaquille O'Neal",'Kobe Bryant'},'Phoenix Suns':{"Amar'e Stoudemire",'Steve Nash','Shawn Marion'},'Sacramento Kings':{'Chris Webber','Oscar Robertson','Doug Christie'},
            'Dallas Mavericks':{'Dirk Nowitzki','Derek Harper','Rolando Blackman'},'Houston Rockets':{'Hakeem Olajuwon','Moses Malone','Yao Ming'},'Memphis Grizzlies':{'Zach Randolph','Marc Gasol','Mike Miller'},
            'New Orleans Pelicans':{'Pete Maravich','Chris Paul','Anthony Davis'},'San Antonio Spurs':{'Tim Duncan','David Robinson','Manu Ginóbili'},'Atlanta Hawks':{'Bob Pettit','Dikembe Mutombo','Jamal Crawford'},
            'Charlotte Hornets':{'Kemba Walker','Dell Curry','Larry Johnson'},'Miami Heat':{'Alonzo Mourning','Dwyane Wade','Grant Long'},'Washington Wizards':{'Wes Unseld','Elvin Hayes','Earl Monroe'},
            'Denver Nuggets':{'Fat Lever','Dan Issel','David Thompson'},'Minnesota Timberwolves':{'Kevin Garnett','Sam Mitchell','Sam Cassell'},'Oklahoma City Thunder':{'Russell Westbrook','Gary Payton','Kevin Durant'},
            'Portland Trail Blazers':{'Bill Walton','Buck Williams','Clifford Robinson'},'Utah Jazz':{'Karl Malone','Darrell Griffith','John Stockton'},'Orlando Magic':{'Dwight Howard','Darrell Armstrong',"Nick Anderson"}}












teams_information.teams_information(option)
teams_map.teams_map(option)



col1,col2=st.columns((6,4))
with col1:
  st.markdown('### 球隊戰績')
  teams_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=option)
  st.dataframe(teams_data)
with col2: 
  dount_chart_df = pd.read_excel("nbateamsdata(dount_chart).xlsx",sheet_name=option)
  st.markdown('### 年度戰績Donut chart')
  donut_theta = st.selectbox('選擇年度', ('14-15年', '15-16年','16-17年','17-18年','18-19年','19-20年','20-21年','21-22年'))
  plost.donut_chart(
              data=dount_chart_df ,
              theta=donut_theta,
              color='項目',
              legend='bottom',
              use_container_width=True)
data_list={"三分球命中率":"3P%","兩分球命中率":"2P%","罰球命中率":"FT%","投籃命中率":"FG%"}
option1 = st.selectbox('想查看數據？',data_list)
teams_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=option) 
area_data=pd.read_excel("nbateamsdata.xlsx",sheet_name=area_list[option_area]) 
league_data=pd.read_excel("nbateamsdata.xlsx",sheet_name='League Average') 
if option1=='三分球命中率':
  col1,col2=st.columns(2)
  with col1:
   st.dataframe(area_data)         
  with col2:
   plt.style.use("ggplot")
   plt.plot(teams_data.年度,teams_data.三分球命中率 ,'.-' ) 
   plt.plot(league_data.年度,league_data.三分球命中率,'.-' )
   plt.xlabel('Season',fontsize="10")
   plt.title(option+data_list[option1]+'vs League AVG')
   st.pyplot(plt) 

  
  
  
st.markdown('### 2021-22球員戰績')
players_data=pd.read_excel("21-22playersdata.xlsx",sheet_name=option)
st.dataframe(players_data)

st.markdown('### 三大傳奇球星成績')
col1,col2=st.columns(2)
with col1:
   option_legendplayer = st.selectbox('選擇球員？',legend_list[option])
   legendplayer_data = pd.read_excel("teams_legendplayerdata.xlsx",index_col='球員')      
   legendplayer_data=legendplayer_data.loc[option_legendplayer]
   legendplayer_data=legendplayer_data.reset_index(drop=False)
   st.dataframe(legendplayer_data.T)
with col2:
   image = Image.open('legendplayer'+'/'+option_legendplayer+'.jpg')
   st.image(image) 
  
  
  
