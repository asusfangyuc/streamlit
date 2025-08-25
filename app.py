# 🌐 Streamlit 與 OpenAI（OpenRouter）
import streamlit as st
from openai import OpenAI        # 使用新版 OpenAI Client（透過 OpenRouter）
# import openai  # 目前未使用，可移除

# 📆 日期與時間
from datetime import datetime
import datetime as dt
import time

# 📊 資料處理
import pandas as pd
import numpy as np

# 📈 視覺化（Matplotlib / Seaborn）
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# 📉 互動式圖表（Plotly / ECharts）
import plotly.express as px
import plotly.graph_objects as go
from streamlit_echarts import st_echarts

# 🔧 Streamlit 擴充（若未用到可後續移除）
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.badges import badge
from streamlit_extras.mention import mention
from streamlit_extras.stoggle import stoggle

# 📰 爬蟲與工具
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import io

# 頁面基本設定
st.set_page_config(page_title="Streamlit", layout="wide")

# CSS 樣式：米色底、墨綠選單、圓角排版、簡約筆記風
st.markdown("""
<style>
/* 🟡 背景與整體字體 */
body, .main, [data-testid="stAppViewContainer"] {
    background-color: #faf5e6 !important;    /* 米色背景 */
    color: #2e2e2e !important;
    font-family: "Helvetica", "微軟正黑體", sans-serif;
}

/* 🟡 全域背景與字體 */
html, body, .stApp, [data-testid="stAppViewContainer"]{
  background-color: var(--milk-bg) !important;
  color:#2e2e2e !important;
  font-family: "Helvetica", "微軟正黑體", sans-serif;
}

/* 🧱 讓 app header 同色，移除陰影；(無法控制雲端白色工具列) */
[data-testid="stHeader"]{
  background: var(--milk-bg) !important;
  box-shadow: none !important;
}

/* 🔝 縮小頂部空白（不同版本都涵蓋） */
.appview-container .main .block-container,
[data-testid="stAppViewContainer"] .main .block-container{
  padding-top: .75rem;
}

/* 📚 側欄 */
[data-testid="stSidebar"]{
  background-color: var(--milk-side) !important;
  border-right: 2px solid var(--milk-border);
  padding-top: 2rem;
  box-shadow: 4px 0 8px rgba(0,0,0,0.04);
  min-width: 300px; max-width: 340px;
  border-radius: 0 20px 20px 0;
}

/* 📘 logo 動畫：淡入 + 輕縮放 */
@keyframes fadeInZoom { 0%{opacity:0;transform:scale(.8);} 100%{opacity:1;transform:scale(1);} }
.animated-logo{ animation: fadeInZoom 1.2s ease-in-out; }

/* 📌 自訂標題樣式 */
.streamlit-heading{
  font-size: 22px !important;
  font-weight: 700;
  color: var(--milk-accent);
  text-align: center;
  margin-bottom: 20px;
}

/* 🔘 按鈕（可依喜好微調） */
.stButton > button{
  background: var(--milk-accent);
  color:#fff; border:none; border-radius:10px;
  padding:.5rem 1rem;
}
.stButton > button:hover{ opacity:.95; transform: translateY(-1px); }

/* 🏷️ Multiselect Tag 樣式（膠囊） */
[data-baseweb="tag"]{
  background:#fff7e1; color:#7a5b2e;
  border:1px solid var(--milk-border);
}

/* 🧾 資料表表頭淡底色（st.dataframe）*/
.stDataFrame div[role="columnheader"]{
  background:#f3eadb !important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    # LOGO + 動畫（保留清爽風格）
    st.markdown("""
    <h1 style='text-align: center;'>
        <img src='https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg'
             width='160' class='animated-logo' style='margin-bottom: 5px;'/>
    </h1>
    """, unsafe_allow_html=True)

    # 文青色選單（奶茶底、墨綠 hover、藍綠 selected）
    page = option_menu(
        menu_title="",
        options=[
            "📘 Streamlit", 
            "🧮 功能介紹", 
            "📊 圖表介紹", 
            "💡 實例應用", 
            "  🕴 GAI 新聞摘要", 
            "  📈 數據分析助手", 
            "🔗 參考資料"
        ],
        icons=[" ", " ", " ", " ", " ", " ", " "],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#faf5e6"
            },
            "icon": {
                "color": "#2e4e3f",  # 墨綠 icon
                "font-size": "16px"
            },
            "nav-link": {
                "font-size": "16px",
                "color": "#3c3c3c",
                "text-align": "left",
                "margin": "6px 0",
                "padding": "0.6rem 1.2rem",
                "border-radius": "10px",
                "--hover-color": "#e2d37e"
            },
            "nav-link-selected": {
                "background-color": "#0f7fa8",  # 靛藍選中
                "color": "white",
                "font-weight": "bold",
                "box-shadow": "inset 0 0 0 1px #d1e0d4"
            }
        }
    )

if page == "📘 Streamlit":
    # ✅ 頁面設定
    st.set_page_config(page_title="Learning Streamlit - Streamlit 教學", layout="centered")

    # ✅ 加入簡單動畫樣式（LOGO 預留）
    st.markdown("""
    <style>
    @keyframes fadeInZoom {
        0% { opacity: 0; transform: scale(0.5); }
        100% { opacity: 1; transform: scale(1); }
    }
    .animated-logo {
        animation: fadeInZoom 1s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)

    # ✅ 頁首文字介紹
    st.markdown("""
    <h1 style='text-align: center;'>🚀 Streamlit 教學</h1>
    <p style='text-align: center;'>透過這個頁面，你將快速掌握 Streamlit 的基本觀念與安裝方式。</p>
    <p style='text-align: center;'>請點選下方分頁開始學習 📘</p>
    """, unsafe_allow_html=True)

    # ✅ 分頁導覽
    tabs = st.tabs(["🗺 Overview", "📘 Streamlit 簡介", "🔧 套件安裝"])

    # 🔹 分頁 1：Overview
    with tabs[0]:
        st.subheader("🗺 Overview - 教學導覽")
        st.markdown("""
        在進入實作前，先了解 **Streamlit 學習地圖**：

        - 🧱 **頁面架構**：學會使用 `st.title()`、`st.markdown()` 設計頁面內容
        - 🎛 **互動元件**：如 `st.button()`、`st.selectbox()` 等 UI 控制項
        - 📈 **資料與圖表呈現**：利用 `pandas`、`matplotlib` 或 `plotly` 顯示資料與可視化
        - ✨ **強化功能**：運用 `streamlit-extras`、`streamlit-echarts` 增加互動性與美觀性

        📌 建議你依照順序閱讀分頁，從「簡介」👉「安裝」👉「實作」。
        """)

    # 🔹 分頁 2：Streamlit 簡介
    with tabs[1]:
        st.subheader("📘 什麼是 Streamlit？")
        st.markdown("""
        Streamlit 是一個能讓你用 **純 Python 語法快速建立 Web 應用程式** 的工具。  
        適用於：資料分析、AI Demo、即時互動式工具製作等。

        ### 🔧 執行方式：
        ```bash
        streamlit run app.py
        ```

        ### 🚀 Streamlit 的優點：
        - 不用寫 HTML / JS，也能做網頁
        - 元件簡單好上手（如 `st.button()`）
        - 支援互動與圖表
        - 快速部署，適合展示 AI / 數據成果

        🌐 [Streamlit 官方展示](https://extras.streamlit.app)
        """)

    # 🔹 分頁 3：套件安裝說明
    with tabs[2]:
        st.subheader("🔧 套件安裝與用途說明")
        st.markdown("""
        以下是我們常用到的套件與對應功能：

        | 套件名稱 | 功能說明 |
        |-----------|-----------|
        | `streamlit` | 建立網頁與 UI 元件（核心套件） |
        | `streamlit-extras` | 額外元件，如徽章、連結、排版輔助等 |
        | `pandas` | 資料整理與表格顯示 |
        | `numpy` | 數值運算、模擬數據 |
        | `matplotlib` | 基本圖表（長條圖、折線圖等） |
        | `seaborn` | 高階統計圖表視覺化 |
        | `openpyxl` | Excel（.xlsx）檔案讀寫 |
        | `streamlit-echarts` | 使用 ECharts 繪製互動圖表 |

        ### 📦 安裝指令（建議一併安裝）：
        ```bash
        pip install streamlit streamlit-extras pandas numpy matplotlib seaborn streamlit-echarts openpyxl
        ```
        """)
elif page == "🧮 功能介紹":
    st.header("🧮 功能介紹")
    chart_data = pd.DataFrame([
    ["超連結按鈕", "link_button()", "導入超連結"],
    ["下載按鈕", "download_button()", "下載檔案功能"],
    ["勾選按鈕", "checkbox()", "勾選按鈕功能"],
    ["下拉式清單", "selectbox()", "下拉式選單"],
    ["單選按鈕", "radio()", "單選按鈕功能"],
    ["多行文字輸入", "text_area()", "輸入多行文字資料"],
    ["單行文字輸入", "text_input()", "輸入單行文字資料"],
    ["數字輸入", "number_input()", "輸入數值型態資料"],
    ["日期輸入", "date_input()", "輸入日期型態資料"],
    ["時間輸入", "time_input()", "輸入時間型態資料"],
    ["填寫表單範例", "form()", "應用各項輸入型態資料，製作表單範例"],
    ["BMI計算器", "slider()", "應用slider與輸入數值型態資料，計算BMI"],
    ["進度條", "progress()", "以進度條顯示資料處理狀態"],
    ["進度流程清單", "status()", "以清單顯示資料處理狀態"],
    ["跳板通知", "toast()", "以跳板通知提醒資料處理狀態"],
    ["使用指南", "expander()", "收納條列式資料"],
    ["Excel檔案上傳", "file_uploader()", "上傳本地端資料"],
    ["顯示統計資料", "df.describe()", "顯示基本統計資料"],
    ["欄位篩選", "multiselect()", "篩選欄位資料"],
    ["日期範圍", "min_date,max_date", "篩選日期資料"],
    ["資料篩選", "selectbox()", "篩選特定資料"],
    ["圖表篩選", "selectbox()", "篩選圖表呈現形式"],
    ], columns=["功能名稱", "示範關鍵字", "功能介紹"])
    # 分類對應功能名稱清單
    section_map = {
    "全部": chart_data["功能名稱"].tolist(),
    "1.按鈕功能": ["超連結按鈕", "下載按鈕"],
    "2.按鈕類型": ["勾選按鈕", "下拉式清單", "單選按鈕"],
    "3.文字、數字與日期輸入": ["多行文字輸入", "單行文字輸入", "數字輸入", "日期輸入", "時間輸入"],
    "4.輸入資料應用案例": ["填寫表單範例", "BMI計算器"],
    "5.流程套件": ["進度條", "進度流程清單", "跳板通知"],
    "6.檔案上傳與應用": ["使用指南", "檔案上傳", "顯示統計資料", "欄位篩選", "日期範圍", "資料篩選", "圖表篩選"]
    }
    # 選分類
    selected_category = st.selectbox("請選擇功能分類", list(section_map.keys()))

    # 篩選對應功能
    filtered_names = section_map[selected_category]
    filtered_data = chart_data[chart_data["功能名稱"].isin(filtered_names)]

    # 顯示資料表
    st.dataframe(filtered_data, use_container_width=True) 
    if "超連結按鈕" in filtered_names:
        st.header("1.按鈕功能")
        st.markdown('#### 超連結按鈕：')
        st.link_button('前往google首頁','https://www.google.com/?hl=zh_TW', type='primary', help='google連結')
        st.link_button('前往youtube首頁','https://www.youtube.com/', disabled=True)
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
st.link_button('前往google首頁','https://www.google.com/?hl=zh_TW', type='primary', help='google連結')
st.link_button('前往youtube首頁','https://www.youtube.com/', disabled=True)""", language="python")
        st.write("")  # 插入一個空行

    if "下載按鈕" in filtered_names:
        st.markdown("#### 下載按鈕：")
        data = {'col1' : [1,2,3,4],'col2' : ['a','b','c','d']}
        my_large_df = pd.DataFrame(data)
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(my_large_df)

        st.download_button(
        label="下載 csv",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv'
        )
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
data = {'col1' : [1,2,3,4],'col2' : ['a','b','c','d']}
my_large_df = pd.DataFrame(data)
def convert_df(df):return df.to_csv(index=False).encode('utf-8')
csv = convert_df(my_large_df)
                    
st.download_button(
label="下載 csv",
data=csv,
file_name='large_df.csv',
mime='text/csv')""", language="python")

    if "下載按鈕" in filtered_names:
        text_contents = "純文字的text"
        st.download_button('下載 text', text_contents)
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
text_contents = "純文字的text"
st.download_button(
'text下載', 
text_contents)""", language="python")

    if "下載按鈕" in filtered_names:
        with open('asus_logo.png', 'rb') as file: #	二進位模式，讀取原始位元資料（✅ 適用於圖片、影片、音訊）
            st.download_button(    
            label="下載 png",
            data=file,
            file_name='asus_logo.png',
            mime='image/png'
            )
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
with open('asus_logo.png', 'rb') as file:
st.download_button(    
label="下載 png",
data=file,
file_name='asus_logo.png',
mime='image/png')""", language="python")
        st.write("")  # 插入一個空行

    if "勾選按鈕" in filtered_names:
        st.title('2.按鈕類型')
        st.markdown('#### 勾選按鈕：')
        apple = st.checkbox('蘋果')
        banana = st.checkbox('香蕉')
        cherry = st.checkbox('櫻桃')
        grape = st.checkbox('葡萄') 
        if apple or banana or cherry or grape: 
            st.success('感謝你的填選')
        with st.expander("🔧 :red[Source Code]"):
                st.code("""
apple = st.checkbox('蘋果')
banana = st.checkbox('香蕉')
cherry = st.checkbox('櫻桃')
grape = st.checkbox('葡萄') 
if apple or banana or cherry or grape: 
    st.success('感謝你的填選')""", language="python")
        st.write("")  # 插入一個空行

    if "下拉式清單" in filtered_names:
        st.markdown('#### 下拉式清單：')
        fruit_option = st.selectbox("請選擇你喜歡的水果:",['蘋果','香蕉','櫻桃','葡萄'])
        st.write('你選擇了:',fruit_option)
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
fruit_option = st.selectbox("請選擇你喜歡的水果:",['蘋果','香蕉','櫻桃','葡萄'])
    st.write('你選擇了:',fruit_option)""", language="python")
        st.write("")  # 插入一個空行

    if "單選按鈕" in filtered_names:
        st.markdown('#### 單選按鈕')
        votes = {
        '狗 :dog:': 0,
        '貓 :cat:': 0,
        '兔子 :rabbit:': 0,
        '鳥 :bird:': 0,
        '熊 :bear:': 0
        }
        animal = st.radio('請選擇一個動物：',('狗 :dog:', '貓 :cat:', '兔子 :rabbit:', '鳥 :bird:', '熊 :bear:'))
        if st.button('投票'):
            votes[animal] += 1
            st.markdown('### 投票結果：')
            for animal, count in votes.items():
                st.markdown(f'{animal}：{count} 票')
            with st.expander("🔧 :red[Source Code]"):
                st.code("""
votes = {
    '狗 :dog:': 0,
    '貓 :cat:': 0,
    '兔子 :rabbit:': 0,
    '鳥 :bird:': 0,
    '熊 :bear:': 0
    }
animal = st.radio('請選擇一個動物：',('狗 :dog:', '貓 :cat:', '兔子 :rabbit:', '鳥 :bird:', '熊 :bear:'))

if st.button('投票'):
    votes[animal] += 1
st.markdown('### 投票結果:')
for animal, count in votes.items():
st.markdown(f'{animal}：{count} 票')""", language="python")
        st.write("")  # 插入一個空行

    if "多行文字輸入" in filtered_names:
        st.title('3.文字、數字與日期輸入')
        st.markdown('#### 多行文字輸入：')
        text=st.text_area("輸入分析文字")
        st.write(f'你輸入了{len(text)}個字')
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
text=st.text_area("輸入分析文字")
st.write(f'你輸入了{len(text)}個字')""", language="python")
        st.write("")  # 插入一個空行

    if "單行文字輸入" in filtered_names:
        st.markdown('#### 單行文字輸入應用：通關密碼')
        password = st.text_input('輸入密碼', max_chars=15, type='password')
        if st.button('密碼確認'): 
            if password == '88888' :st.write('密碼正確')
        else: st.write('密碼錯誤')

        with st.expander("🔧 :red[Source Code]"):
            st.code("""
password = st.text_input('輸入密碼', max_chars=15, type='password')
if st.button('密碼確認'): 
    if password == '88888' :st.write('密碼正確')
else: st.write('密碼錯誤')""", language="python")
        st.write("")  # 插入一個空行

    if "數字輸入" in filtered_names:
        st.markdown("#### 數字輸入：")
        number = st.number_input('輸入一個數字', value=None, step=5, min_value=0, max_value=1000) #step=5,代表每次數值加5
        st.write('你輸入的是',number)
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
number = st.number_input('輸入一個數字', value=None, step=5, min_value=0, max_value=1000)
    st.write('你輸入的是',number)""", language="python")
        st.write("")  # 插入一個空行

    if "日期輸入" in filtered_names:
        st.markdown('#### 日期輸入：')
        birthday = st.date_input('你的生日',datetime.date(1990,1,1))
        if st.button('生日確認'): st.write('你的生日是', birthday.strftime('%Y年%m月%d日'))
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
birthday = st.date_input('你的生日',datetime.date(1990,1,1))
    if st.button('生日確認'): st.write('你的生日是', birthday.strftime('%Y年%m月%d日'))""", language="python")
        st.write("")  # 插入一個空行

    if "時間輸入" in filtered_names:
        st.markdown('#### 時間輸入：')
        t = st.time_input('設定自動時間', value=None, step=3600)
        st.write('自動發信時間',t)
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
t = st.time_input('設定自動時間', value=None, step=3600)
    st.write('自動發信時間',t)""", language="python")
        st.write("")  # 插入一個空行

    if "填寫表單範例" in filtered_names:
        st.title('4.輸入資料應用案例')
        st.markdown('#### 填寫表單範例：')
        with st.form(key='form_demo'):
            form_name = st.text_input(label='姓名',placeholder="請輸入姓名")
            form_gender = st.selectbox('性別',['男生','女生','其他'])
            form_birthday = st.date_input('生日')
            form_height = st.number_input('身高',value=100, min_value=100, max_value=250)
            form_weight = st.number_input('體重',value=0, min_value=0, max_value=200)
            submit_button = st.form_submit_button(label='提交')
        if submit_button: st.success(f'你好，你的姓名為,{form_name},你的資訊已提交完成' )
        st.toast('已保存你的資料')
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
with st.form(key='form_demo'):
    form_name = st.text_input(label='姓名',placeholder="請輸入姓名")
    form_gender = st.selectbox('性別',['男生','女生','其他'])
    form_birthday = st.date_input('生日')
    form_height = st.number_input('身高',value=100, min_value=100, max_value=250)
    form_weight = st.number_input('體重',value=0, min_value=0, max_value=200)
    submit_button = st.form_submit_button(label='提交')
if submit_button: st.success(f'你好，你的姓名為,{form_name},你的資訊已提交完成' )
st.toast('已保存你的資料')""", language="python")
        st.write("")  # 插入一個空行

    if "BMI計算器" in filtered_names:
        st.markdown("#### BMI計算器：")
        height = st.slider("請輸入身高 (cm)", 140, 200, 170)
        weight = st.number_input("請輸入體重 (kg)", 30.0, 150.0, 60.0)
        bmi = weight / ((height / 100) ** 2)
        st.write(f"你的 BMI 是：`{bmi:.2f}`")
        if bmi < 18.5:
            st.warning("體重過輕")
        elif bmi < 24:
            st.success("體重正常")
        else:
            st.error("體重過重")
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
height = st.slider("請輸入身高 (cm)", 140, 200, 170)
weight = st.number_input("請輸入體重 (kg)", 30.0, 150.0, 60.0)
bmi = weight / ((height / 100) ** 2)
st.write(f"你的 BMI 是：{bmi:.2f}")
if bmi < 18.5:
st.warning("體重過輕")
elif bmi < 24:
st.success("體重正常")
else:
st.error("體重過重")""", language="python")
        st.write("")  # 插入一個空行

    if "進度條" in filtered_names:
        st.title('5.流程套件')
        st.markdown('#### 進度條：')
        progress_text = "正在處理中..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            my_bar.progress(percent_complete + 1, text=progress_text + f" {percent_complete + 1}% complete")
            time.sleep(0.01)
        my_bar.empty()
        st.button("Replay") #在 Streamlit 中，每一次使用者有任何互動（例如按按鈕）時，整個 .py 檔案都會從第一行重新執行一次
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
progress_text = "正在處理中..."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    my_bar.progress(percent_complete + 1, text=progress_text + f" {percent_complete + 1}% complete")
    time.sleep(0.01)
my_bar.empty()
st.button("Replay")""", language="python")
        st.write("")  # 插入一個空行

    if "進度流程清單" in filtered_names:
        st.markdown('#### 進度流程清單：')
        if st.button('重新執行'):
            st.status('下載網址中')
            st.write('搜尋網址中')
            time.sleep(1)
            st.write('搜尋數據中')
            time.sleep(1)
            st.write('下載完成')
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
if st.button('重新執行'):
    st.status('下載網址中')
    st.write('搜尋網址中')
    time.sleep(1)
    st.write('搜尋數據中')
    time.sleep(1)
    st.write('下載完成')""", language="python")
        st.write("")  # 插入一個空行

    if "跳板通知" in filtered_names:
        st.markdown('#### 跳板通知：')
        if st.button('存檔', type='primary'):
            st.toast('已保存你的圖片')
            time.sleep(1)
            st.toast('警告!儲存失敗')
            st.snow()
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
if st.button('存檔', type='primary'):
    st.toast('已保存你的圖片')
    time.sleep(1)
    st.toast('警告!儲存失敗')
    st.snow()""", language="python")
        st.write("")  # 插入一個空行

    if "使用指南" in filtered_names:
        st.title('6.檔案上傳與應用')
        st.markdown('#### 使用指南：')  
        with st.expander('使用指南'):
            st.write('Excel可視覺化應用程序')
            st.write('1.上傳Excel') 
            st.write('2.選擇顯示統計資料')
            st.write('3.篩選欄位功能') 
            st.write('4.選擇顯示日期')
            st.write('5.選擇顯示欄位')
            st.write('6.選擇顯示圖表')
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
with st.expander('使用指南'):
    st.write('Excel可視覺化應用程序')
    st.write('1.上傳Excel') 
    st.write('2.選擇顯示統計資料')
    st.write('3.篩選欄位功能') 
    st.write('4.選擇顯示日期')
    st.write('5.選擇顯示欄位')
    st.write('6.選擇顯示圖表')""", language="python")
        st.write("")  # 插入一個空行

    if "檔案上傳" in filtered_names:
        st.markdown('#### 檔案上傳：')
        uploaded_file = st.file_uploader("上傳Excel檔案", type=["csv", "xlsx"], accept_multiple_files=True) #允許上傳多個文件
        select_file = st.selectbox('選擇要查看的Excel文件', uploaded_file, format_func=lambda x: x.name)
        if select_file is not None:
            file_extension = select_file.name.split('.')[-1]
            if file_extension.lower() == 'csv':
                df = pd.read_csv(select_file)
            else:
                df = pd.read_excel(select_file, engine='openpyxl')
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
uploaded_file = st.file_uploader("上傳Excel檔案", type=["csv", "xlsx"], accept_multiple_files=True) #允許上傳多個文件
select_file = st.selectbox('選擇要查看的Excel文件', uploaded_file, format_func=lambda x: x.name)
if select_file is not None:
    file_extension = select_file.name.split('.')[-1]
    if file_extension.lower() == 'csv':
        df = pd.read_csv(select_file)
    else:
        df = pd.read_excel(select_file, engine='openpyxl')""", language="python")
        st.write("")  # 插入一個空行

    if "顯示統計資料" in filtered_names:
        st.markdown('#### 顯示統計資料：')
        if df is not None:
            show_summary=st.checkbox('顯示統計摘要')
            if show_summary:
                st.write('數據摘要統計:')
                st.write(df.describe()) 
        with st.expander("🔧 :red[Source Code]"):
            st.code("""    
if df is not None:
    show_summary=st.checkbox('顯示統計摘要')
    if show_summary:
        st.write('數據摘要統計:')
        st.write(df.describe())""", language="python")
        st.write("")  # 插入一個空行

    if "欄位篩選" in filtered_names:
        st.markdown('#### 欄位篩選：')
        if df is not None:
            multiselected_columns = st.multiselect('選擇顯示的欄位',df.columns)
            if multiselected_columns:
                st.write('選定的欄位')
                st.write(df[multiselected_columns])    
        with st.expander("🔧 :red[Source Code]"):
            st.code("""    
if df is not None:
    multiselected_columns = st.multiselect('選擇顯示的欄位',df.columns)
    if multiselected_columns:
        st.write('選定的欄位')
        st.write(df[multiselected_columns])""", language="python")
        st.write("")  # 插入一個空行

    if "日期範圍" in filtered_names:
        st.markdown('#### 日期範圍：')
    #日期篩選
        if '銷售日期' in df.columns:
            df['銷售日期'] = pd.to_datetime(df['銷售日期'])
            min_date = df['銷售日期'].min().date()
            max_date = df['銷售日期'].max().date()
            date_range = st.date_input('選擇日期範圍',(min_date,max_date))
            #轉換date_range為timestamp
            strat_date = pd.Timestamp(date_range[0])
            end_date = pd.Timestamp(date_range[1])
            #進行日期篩選數據
            df_filtered = df[(df['銷售日期'] >= strat_date) & (df['銷售日期'] <= end_date)]
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
if '銷售日期' in df.columns:
    df['銷售日期'] = pd.to_datetime(df['銷售日期'])
    min_date = df['銷售日期'].min().date()
    max_date = df['銷售日期'].max().date()
    date_range = st.date_input('選擇日期範圍',(min_date,max_date))
    strat_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1])
    df_filtered = df[(df['銷售日期'] >= strat_date) & (df['銷售日期'] <= end_date)]""", language="python")
        st.write("")  # 插入一個空行

     #視覺化欄位選擇
    if "資料篩選" in filtered_names:
        st.markdown('#### 資料篩選：')
        category_column = st.selectbox("選擇分類欄位（如型號）", [col for col in df_filtered.columns if any(x in col for x in ['型號', '地區', '通路'])])
        if category_column:
            unique_values = df_filtered[category_column].dropna().unique().tolist()
            filter_value = st.selectbox(f"選擇『{category_column}』的細項值", unique_values)
            df_filtered = df_filtered[df_filtered[category_column] == filter_value]
        else:
            filtered_df = df_filtered.copy()
        selected_column = st.selectbox("選擇欄位", [col for col in df_filtered.columns if any(x in col for x in ['數量', '金額', '單價'])])
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
category_column = st.selectbox("選擇分類欄位（如型號）", [col for col in df_filtered.columns if any(x in col for x in ['型號', '地區', '通路'])])
if category_column:
    unique_values = df_filtered[category_column].dropna().unique().tolist()
    filter_value = st.selectbox(f"選擇『{category_column}』的細項值", unique_values)
    df_filtered = df_filtered[df_filtered[category_column] == filter_value]
else:
    filtered_df = df_filtered.copy()
selected_column = st.selectbox("選擇欄位", [col for col in df_filtered.columns if any(x in col for x in ['數量', '金額', '單價'])])""", language="python")
        st.write("")  # 插入一個空行

    #視覺化類型選擇  
    if "圖表篩選" in filtered_names:
        st.markdown('#### 圖表篩選：')
        df_chart = df_filtered[['銷售日期', selected_column]].set_index('銷售日期')
        chart_type = st.selectbox('選擇圖表類型',['折線圖','柱狀圖','散點圖'])
        if chart_type == '折線圖':
            st.line_chart(df_chart)
        elif chart_type == '柱狀圖':
            st.bar_chart(df_chart)
        elif chart_type == '散點圖':
            st.scatter_chart(df_chart)
        with st.expander("🔧 :red[Source Code]"):
            st.code("""
df_chart = df_filtered[['銷售日期', selected_column]].set_index('銷售日期')
chart_type = st.selectbox('選擇圖表類型',['折線圖','柱狀圖','散點圖'])
if chart_type == '折線圖':
    st.line_chart(df_chart)
elif chart_type == '柱狀圖':
    st.bar_chart(df_chart)
elif chart_type == '散點圖':
    st.scatter_chart(df_chart)""", language="python")
        st.write("")  # 插入一個空行
elif page == "📊 圖表介紹":
    st.header("📊 圖表展示")

    # 熱門度依序排序的圖表資料
    chart_data = pd.DataFrame([
        ["折線圖", "plotly", "line()"],
        ["長條圖", "plotly", "bar()"],
        ["圓餅圖", "plotly", "Pie()"],
        ["熱力圖", "seaborn", "heatmap()"],
        ["雷達圖", "plotly", "Scatterpolar()"],
        ["環形圖", "plotly", "Pie(hole=0.5)"],
        ["面積圖", "plotly", "area()"],
        ["瀑布圖", "plotly", "Waterfall()"],
        ["儀表圖", "plotly", "Indicator(gauge)"],
        ["氣泡圖", "plotly", "scatter(size=...)"],
        ["地圖", "plotly", "scatter_mapbox()"],
        ["漏斗圖", "plotly", "Funnel()"],
        ["漸層圖", "matplotlib", "imshow()"]
    ], columns=["圖表名稱", "使用套件", "函數"])


    # ✅ 只用「圖表名稱」和「使用套件」作為可篩選欄位
    filterable_columns = ["圖表名稱", "使用套件"]
    filter_column = st.selectbox("📌 選擇篩選欄位", ["全部"] + filterable_columns)

    if filter_column == "全部":
        filtered_data = chart_data
        matched_types = set(chart_data["圖表名稱"])
    elif filter_column == "圖表名稱":
        selected_types = st.multiselect("✅ 選擇圖表名稱", chart_data["圖表名稱"].unique().tolist(), default=[])
        filtered_data = chart_data[chart_data["圖表名稱"].isin(selected_types)]
        matched_types = set(selected_types)
    else:
        options = chart_data[filter_column].unique()
        selected_value = st.selectbox("🔍 選擇條件值", options)
        filtered_data = chart_data[chart_data[filter_column] == selected_value]
        matched_types = set(filtered_data["圖表名稱"])

    st.dataframe(filtered_data, use_container_width=True)

    # 模擬資料（保留原本）
    df_nb = pd.DataFrame({
        "型號": ["ZenBook", "Vivobook", "ROG", "TUF", "ExpertBook", "ProArt"],
        "Q1 銷售量": [12000, 15000, 9000, 8000, 6000, 5000],
        "Q2 銷售量": [14000, 16000, 10000, 9500, 7000, 6500],
        "滿意度": [85, 78, 92, 80, 88, 90],
        "服務分數": [4.2, 3.9, 4.6, 4.0, 4.5, 4.7],
        "價格": [35000, 28000, 49000, 42000, 31000, 46000],
        "重量": [1.1, 1.4, 2.2, 2.5, 1.2, 1.6]
    })
    
    # 各圖表：僅顯示選到的類型，並包在 expander 裡
    if "漸層圖" in matched_types:
        st.caption("🎨 **漸層圖**：色彩呈現數值強度，並在格子中顯示實際數值。")

        with st.expander("🧬 漸層圖（動態選欄 + 色彩強度 + 數值顯示）"):
            selected_column = st.selectbox("請選擇要顯示強度的欄位", df_nb.columns[1:], key="gradient_column")
            
            min_val = float(df_nb[selected_column].min())
            max_val = float(df_nb[selected_column].max())
            vmin, vmax = st.slider(
                "調整顏色映射範圍（強度最小 / 最大值）",
                min_value=min_val,
                max_value=max_val,
                value=(min_val, max_val),
                step=(max_val - min_val) / 100
            )

            fig, ax = plt.subplots(figsize=(6, 3))
            values = df_nb[selected_column].values
            grad = np.tile(values.reshape(-1, 1), (1, 10))
            im = ax.imshow(grad, cmap="YlOrRd", aspect="auto", vmin=vmin, vmax=vmax)

            ax.set_yticks(np.arange(len(df_nb)))
            ax.set_yticklabels(df_nb["型號"], fontsize=10)
            ax.set_xticks([])  # 隱藏 X 軸刻度
            ax.set_xlabel("強度分佈（模擬）", fontsize=10)
            ax.set_ylabel("型號", fontsize=10)
            ax.set_title(f"{selected_column} 強度漸層圖", fontsize=12)

            # 👉 加上數值文字（只顯示中間第 5 列）
            for i, val in enumerate(values):
                ax.text(5, i, f"{val:.1f}", ha="center", va="center",
                        color="white" if val > (vmin + vmax) / 2 else "black", fontsize=9)

            plt.colorbar(im, ax=ax, label="強度")
            plt.tight_layout()
            st.pyplot(fig)

            with st.expander("🔧 Source Code"):
                st.code("""
    for i, val in enumerate(values):
        ax.text(5, i, f"{val:.1f}", ha="center", va="center",
                color="white" if val > (vmin + vmax) / 2 else "black")
                """, language="python")
    if "熱力圖" in matched_types:
        with st.expander("🧩 熱力圖：滿意度 vs 價格"):
            fig, ax = plt.subplots()
            heat_data = np.outer(df_nb["滿意度"], df_nb["價格"])
            sns.heatmap(heat_data, ax=ax)
            st.pyplot(fig)
            with st.expander("🔧 Source Code"):
                st.code("sns.heatmap(...)")

    if "儀表圖" in matched_types:
        with st.expander("💧 儀表圖：滿意度展示"):
            for idx, row in df_nb.iterrows():
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=row["滿意度"],
                    title={'text': f"{row['型號']} 滿意度"},
                    gauge={'axis': {'range': [0, 100]}}
                ))
                st.plotly_chart(fig, use_container_width=True)
            with st.expander("🔧 Source Code"):
                st.code("go.Indicator(mode='gauge+number', value=..., title=..., gauge=...)")

    if "折線圖" in matched_types:
        with st.expander("📈 折線圖：Q1 / Q2 銷售趨勢"):
            df_line = df_nb.set_index("型號")[["Q1 銷售量", "Q2 銷售量"]]
            st.line_chart(df_line)
            with st.expander("🔧 Source Code"):
                st.code("st.line_chart(df_line)")

    if "長條圖" in matched_types:
        with st.expander("📊 長條圖：Q1 銷售比較"):
            fig, ax = plt.subplots()
            df_nb.plot(kind="bar", x="型號", y="Q1 銷售量", ax=ax)
            st.pyplot(fig)
            with st.expander("🔧 Source Code"):
                st.code("df_nb.plot(kind='bar', x='型號', y='Q1 銷售量', ax=ax)")

    if "圓餅圖" in matched_types:
        with st.expander("🥧 圓餅圖：Q2 銷售占比"):
            fig, ax = plt.subplots()
            ax.pie(df_nb["Q2 銷售量"], labels=df_nb["型號"], autopct="%1.1f%%")
            ax.axis("equal")
            st.pyplot(fig)
            with st.expander("🔧 Source Code"):
                st.code("ax.pie(df_nb['Q2 銷售量'], labels=df_nb['型號'], autopct='%1.1f%%')")

    if "環形圖" in matched_types:
        with st.expander("🔄 環形圖：Q2 銷售占比"):
            fig = go.Figure(go.Pie(labels=df_nb["型號"], values=df_nb["Q2 銷售量"], hole=0.5))
            st.plotly_chart(fig)
            with st.expander("🔧 Source Code"):
                st.code("go.Pie(labels=..., values=..., hole=0.5)")

    if "面積圖" in matched_types:
        with st.expander("📉 面積圖：銷售趨勢比較"):
            df_area = df_nb.set_index("型號")[["Q1 銷售量", "Q2 銷售量"]]
            st.area_chart(df_area)
            with st.expander("🔧 Source Code"):
                st.code("st.area_chart(df_area)")

    if "瀑布圖" in matched_types:
        with st.expander("🧱 瀑布圖：Q1→Q2 銷售差異"):
            fig = go.Figure(go.Waterfall(
                x=df_nb["型號"],
                measure=["relative"] * len(df_nb),
                y=df_nb["Q2 銷售量"] - df_nb["Q1 銷售量"]
            ))
            st.plotly_chart(fig)
            with st.expander("🔧 Source Code"):
                st.code("go.Waterfall(...)")

    if "雷達圖" in matched_types:
        with st.expander("📍 雷達圖：型號評比"):
            fig = go.Figure()
            for i in range(len(df_nb)):
                fig.add_trace(go.Scatterpolar(
                    r=[df_nb.loc[i, '滿意度'], df_nb.loc[i, '服務分數'], df_nb.loc[i, '價格'], df_nb.loc[i, '重量']],
                    theta=["滿意度", "服務分數", "價格", "重量"],
                    fill="toself",
                    name=df_nb.loc[i, '型號']
                ))
            st.plotly_chart(fig)
            with st.expander("🔧 Source Code"):
                st.code("go.Scatterpolar(...)")

    if "漏斗圖" in matched_types:
        with st.expander("🧭 漏斗圖：轉換流程展示"):
            fig = go.Figure(go.Funnel(
                y=["造訪網站", "查看商品", "加入購物車", "完成訂單"],
                x=[3000, 2000, 1200, 800],
                textinfo="value+percent previous"
            ))
            st.plotly_chart(fig)
            with st.expander("🔧 Source Code"):
                st.code("go.Funnel(...)")

    if "氣泡圖" in matched_types:
        with st.expander("🧩 氣泡圖：售價與重量（模擬）"):
            fig = px.scatter(df_nb, x="價格", y="重量", size="Q2 銷售量", color="型號")
            st.plotly_chart(fig)
            with st.expander("🔧 Source Code"):
                st.code("px.scatter(..., size='Q2 銷售量')")

    if "地圖" in matched_types:
        with st.expander("⛳ 地圖：銷售地區分布（模擬）"):
            map_df = pd.DataFrame({
                "lat": [25.03, 35.68, 37.57, 22.28],
                "lon": [121.56, 139.76, 126.98, 114.15],
                "城市": ["Taipei", "Tokyo", "Seoul", "Hong Kong"]
            })
            st.map(map_df)
            with st.expander("🔧 Source Code"):
                st.code("st.map(map_df)")
elif page == "  🕴 GAI 新聞摘要":
    # 這頁面不再呼叫 set_page_config；請確保整個 app 只在檔案頂端呼叫一次。

    # 中文字體（避免亂碼）
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans CJK TC", "PingFang TC", "Heiti TC", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False

    # ---------- OpenRouter API 初始化（用 secrets.toml） ----------
    OPENROUTER_API_KEY  = st.secrets.get("OPENROUTER_API_KEY")
    OPENROUTER_BASE_URL = st.secrets.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

    if not OPENROUTER_API_KEY:
        st.error("找不到 OPENROUTER_API_KEY，請在 `.streamlit/secrets.toml` 或 Streamlit Cloud 的 Secrets 面板設定後再執行。")
        st.stop()

    default_headers = {}
    app_url  = st.secrets.get("APP_URL")
    app_name = st.secrets.get("APP_NAME")  # 只用 ASCII，避免 'ascii' codec 錯誤
    if app_url:
        default_headers["HTTP-Referer"] = app_url
    if app_name:
        default_headers["X-Title"] = app_name

    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        default_headers=default_headers or None
    )

    # ---------- 爬蟲輔助（避免與 DataFrame 撞名） ----------
    REQUEST_TIMEOUT = 12
    HTTP_SESSION = requests.Session()
    HTTP_SESSION.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
        )
    })

    # =========================================================
    # 🧠 議題分類（LLM）
    # =========================================================
    def classify_topic(title: str, content: str) -> str:
        """呼叫 OpenRouter（deepseek-chat）將標題與內文分類為單一議題"""
        try:
            resp = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "你是一位新聞議題分類專家，請根據新聞標題與內文，回傳最合適的一個議題分類，"
                            "例如：科技、財經、政治、產業趨勢、國際、人物報導、消費、AI、新創、教育、健康等。"
                            "只回傳分類名稱，不需要解釋。"
                        )
                    },
                    {"role": "user", "content": f"標題：{title}\n內文：{(content or '')[:500]}"},
                ],
                temperature=0.3,
                max_tokens=20
            )
            topic = (resp.choices[0].message.content or "").strip()
            return topic if topic else "未分類"
        except Exception as e:
            return f"分類失敗: {e}"

    # =========================================================
    # 📰 抓取新聞內容與標題
    # =========================================================
    @st.cache_data(show_spinner=False, ttl=600)
    def fetch_news_content(url: str, content_tags=None) -> str:
        """抓取新聞文章前 500 字做分析；預設合併 <article>/<p>/<div>/<span> 的文字。"""
        content_tags = content_tags or ["article", "p", "div", "span"]
        try:
            res = HTTP_SESSION.get(url, timeout=REQUEST_TIMEOUT)
        except Exception as e:
            return f"文章內容抓取失敗：{e}"

        if res.status_code != 200:
            return f"文章內容抓取失敗：HTTP {res.status_code}"

        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        article_content = []
        for tag in content_tags:
            for el in soup.find_all(tag):
                txt = (el.get_text() or "").strip()
                if txt:
                    article_content.append(txt)
        merged = "\n".join(article_content).strip()
        return merged[:500] if merged else "無法抓取文章內容"

    def _base_of(url: str) -> str:
        p = urlparse(url)
        return f"{p.scheme}://{p.netloc}"

    @st.cache_data(show_spinner=False, ttl=300)
    def fetch_headlines(list_url: str, site_name: str, tag: str, keyword: str = "華碩"):
        """從網站列表頁抓取含關鍵字的標題、連結，再抓內文；失敗回傳空陣列避免整個 app 掛掉。"""
        try:
            res = HTTP_SESSION.get(list_url, timeout=REQUEST_TIMEOUT)
        except Exception as e:
            st.warning(f"{site_name} 連線失敗：{e}")
            return []

        if res.status_code != 200:
            st.warning(f"{site_name} 回應碼 {res.status_code}（可能擋爬或需 JS）。")
            return []

        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        headline_elements = soup.find_all(tag)
        base = _base_of(list_url)

        headlines = []
        for h in headline_elements:
            title = (h.get_text() or "").strip()
            if not title or keyword not in title:
                continue
            a = h.find("a", href=True)
            if not a:
                continue
            href = a["href"].strip()
            news_url = urljoin(base, href)
            content = fetch_news_content(news_url)
            headlines.append({
                "新聞媒體": site_name,
                "新聞標題": title,
                "新聞內容": content,
                "新聞網址": news_url
            })
        return headlines

    # =========================================================
    # 🧱 UI：主畫面
    # =========================================================
    st.header("  🕴 GAI 新聞摘要")

    keyword = st.text_input("請輸入要搜尋的關鍵字（例如：華碩）", value="華碩")

    platforms = {
        "ETtoday新聞雲": {"url": "https://www.ettoday.net/news/tag/ASUS/", "tag": "h3"},
        "聯合新聞網":   {"url": "https://udn.com/search/tagging/2/ASUS", "tag": "h2"},
        "蘋果日報":     {"url": "https://tw.nextapple.com/search/asus", "tag": "h2"},
        "中時新聞":     {"url": "https://www.chinatimes.com/search/ASUS?chdtv", "tag": "h3"},
    }

    selected_sites = st.multiselect("📍 請選擇新聞平台（可複選）", list(platforms.keys()))

    if st.button("🔍 搜尋新聞"):
        if not selected_sites:
            st.warning("請先選擇至少一個新聞平台。")
        else:
            st.info("正在抓取新聞並分類議題，請稍候…")
            all_results = []
            progress = st.progress(0)
            total = len(selected_sites)

            for i, site_name in enumerate(selected_sites, start=1):
                site = platforms[site_name]
                articles = fetch_headlines(site["url"], site_name, site["tag"], keyword)
                for art in articles:
                    topic = classify_topic(art.get("新聞標題", ""), art.get("新聞內容", ""))
                    art["議題"] = topic
                    all_results.append(art)
                    time.sleep(0.8)  # 適度節流，避免 LLM 請求過快
                progress.progress(i / total)

            # 安全重排欄位，缺的自動補 NaN，避免 KeyError
            expected_cols = ["議題", "新聞媒體", "新聞標題", "新聞內容", "新聞網址"]
            df = pd.DataFrame(all_results).reindex(columns=expected_cols)

            if df.empty or df["新聞標題"].isna().all():
                st.warning("沒有抓到符合關鍵字的新聞，請更換關鍵字或平台重試。")
            else:
                missing = [c for c in expected_cols if c not in df.columns or df[c].isna().all()]
                if missing:
                    st.info(f"部分欄位缺少資料：{', '.join(missing)}。")
                st.session_state["news_df"] = df
                topics = [t for t in df["議題"].dropna().unique().tolist() if t]
                st.session_state["topics"] = sorted(topics) if topics else ["未分類"]
                st.success("✅ 抓取完成！下方可進行篩選與分析。")

    # =========================================================
    # 🔎 分析與互動
    # =========================================================
    if "news_df" in st.session_state:
        df = st.session_state["news_df"]
        unique_topics = st.session_state["topics"]

        selected_topics = st.multiselect("🧠 請選擇篩選的議題（可複選）", unique_topics, default=unique_topics, key="topic_filter")
        filtered_df = df[df["議題"].isin(selected_topics)].copy()

        st.dataframe(filtered_df, use_container_width=True)

        # 📊 議題分佈長條圖（極小版、可自適應）
        st.markdown("### 📊 圖表分析：各議題新聞分佈")
        if filtered_df.empty:
            st.info("目前篩選條件下沒有資料。")
        else:
            topic_counts = filtered_df["議題"].value_counts()
            fig, ax = plt.subplots(figsize=(3, 1), dpi=300)  # 小尺寸高 DPI
            bars = ax.bar(topic_counts.index, topic_counts.values)
            for bar in bars:
                h = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, h, f"{int(h)}",
                        ha="center", va="bottom", fontsize=8)
            ax.set_ylabel("新聞數量", fontsize=8)
            ax.tick_params(axis="x", labelsize=8)
            ax.tick_params(axis="y", labelsize=8)
            st.pyplot(fig, use_container_width=True, clear_figure=True)
            plt.close(fig)

        # 💬 使用者提問（依當前篩選結果生成脈絡）
        st.markdown("### 💬 對這些新聞內容發問")
        user_question = st.text_area("請輸入你的問題（例如：這些新聞中有哪些未來趨勢？）", key="qa_question")

        if st.button("送出提問", key="qa_submit") and user_question:
            if filtered_df.empty:
                st.warning("目前沒有可供分析的新聞內容，請先進行搜尋或調整篩選條件。")
            else:
                context_text = "\n\n".join(
                    f"【{row['議題']}】{row['新聞標題']}：{row['新聞內容']}"
                    for _, row in filtered_df.iterrows()
                )[:3000]

                full_prompt = (
                    "以下是多則新聞內容，請根據使用者的問題給出具體回覆。\n\n"
                    f"使用者提問：{user_question}\n\n"
                    f"新聞資料：{context_text}"
                )

                with st.spinner("LLM 正在產生回覆…"):
                    try:
                        resp = client.chat.completions.create(
                            model="deepseek/deepseek-chat",
                            messages=[
                                {
                                    "role": "system",
                                    "content": "你是一位中文新聞分析助手，請根據提供的新聞內容與使用者問題給出清晰、簡潔、具體的中文回應。"
                                },
                                {"role": "user", "content": full_prompt}
                            ],
                            temperature=0.5,
                            max_tokens=600
                        )
                        st.markdown("### 🤖 LLM 回覆")
                        st.write((resp.choices[0].message.content or "").strip())
                    except Exception as e:
                        st.error(f"回覆失敗：{e}")
elif page == "  📈 數據分析助手":
    import os, re
    # 這裡不需要再 import streamlit / pandas / plotly / OpenAI，
    # 若你已在檔案上方匯入過就好。未匯入者請在檔案頂端補上。

    st.header("📈 數據分析助手")

    # --- 讀取 OpenRouter 設定（優先 secrets，再退環境變數/預設） ---
    OPENROUTER_API_KEY  = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_BASE_URL = st.secrets.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    if not OPENROUTER_API_KEY:
        st.error("找不到 OPENROUTER_API_KEY，請在 .streamlit/secrets.toml 或環境變數設定。")
        st.stop()

    default_headers = {}
    app_url  = st.secrets.get("APP_URL")           # e.g. https://your-app.streamlit.app
    app_name = st.secrets.get("APP_NAME")          # e.g. ASUS-Data-Assistant
    if app_url:
        default_headers["HTTP-Referer"] = app_url  # 保持 ASCII，避免 'ascii' codec 錯誤
    if app_name:
        default_headers["X-Title"] = app_name

    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        default_headers=default_headers or None
    )
    openai_model = "deepseek/deepseek-r1:free"  # 若要避免 <think>，可改 "deepseek/deepseek-chat"

    # 移除 deepseek-r1 可能回傳的 <think>... 區塊
    def _strip_think(txt: str) -> str:
        return re.sub(r"<think>.*?</think>", "", txt or "", flags=re.DOTALL).strip()

    uploaded_file = st.file_uploader("請上傳一個 CSV 檔案", type=["csv"])

    if uploaded_file:
        # --- 讀檔（優先 UTF-8，失敗退回預設） ---
        try:
            df = pd.read_csv(uploaded_file, encoding="utf-8")
        except Exception:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file)

        st.subheader("🔍 數據預覽")
        st.dataframe(df.head(), use_container_width=True)

        st.subheader("📈 數據統計摘要")
        try:
            st.dataframe(df.describe(include="all"), use_container_width=True)
        except Exception:
            st.dataframe(df.describe(), use_container_width=True)

        st.subheader("📊 圖表視覺化")
        numeric_columns = df.select_dtypes(include="number").columns.tolist()
        non_numeric_columns = df.select_dtypes(exclude="number").columns.tolist()

        if numeric_columns and non_numeric_columns:
            x_axis = st.selectbox("選擇 X 軸欄位（分類）", non_numeric_columns, key="da_x")
            y_axis = st.selectbox("選擇 Y 軸欄位（數值）", numeric_columns, key="da_y")
            chart_type = st.radio("選擇圖表類型", ["Bar Chart", "Line Chart"], horizontal=True, key="da_chart")

            if chart_type == "Bar Chart":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
            else:
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("需同時包含分類欄位（如文字）與數值欄位，才能建立圖表。")

        st.subheader("🧠 使用 GPT 分析")
        user_query = st.text_area("請輸入你的分析指令（如：請幫我分析客戶評論、哪個產品銷售量最好?）", key="da_query")

        if st.button("送出給 GPT 分析", key="da_btn"):
            with st.spinner("分析中..."):
                # 只取前 10 列，避免 prompt 過長
                df_md = df.head(10).astype(str).to_markdown(index=False)
                prompt = f"""你是一位數據分析師，請根據以下的 DataFrame（以 markdown 表示）回答問題。

Data:
{df_md}

問題：
{user_query}

請以條列、簡潔具體的方式回覆，必要時給出重點洞察與可能的下一步分析建議。"""

                try:
                    resp = client.chat.completions.create(
                        model=openai_model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.5
                    )
                    raw = resp.choices[0].message.content
                    result = _strip_think(raw)
                    st.markdown("#### 🧾 分析結果")
                    st.write(result)
                except Exception as e:
                    st.error(f"發生錯誤：{e}")

elif page == "🔗 參考資料":
    st.header("🎨 進階排版與功能加強（streamlit-extras 功能介紹）")

    st.markdown("""
    `streamlit-extras` 提供許多輔助元件，讓頁面更有彈性、更好用。
    安裝方式：
    ```bash
    pip install streamlit-extras
    ```
    """)

    st.subheader("1. 增加垂直間距")
    st.write("上方段落")
    add_vertical_space(2)
    st.write("下方段落（中間有空白）")

    st.subheader("2. 顯示徽章 badge")
    badge(type="github", name="arnaudmiribel/streamlit-extras")
    badge(type="pypi", name="streamlit-extras")
    badge(type="twitter", name="streamlit")
    badge(type="buymeacoffee", name="arnaudmiribel")

    st.subheader("3. 快速連結提示 mention")
    mention(label="查看 Streamlit 官方網站", icon="🌐", url="https://streamlit.io")
    with st.expander("🔧 :red[Source Code]"):
        st.code("""
st.write("上方段落")
add_vertical_space(2)
st.write("下方段落（中間有空白）")

badge(type="github", name="arnaudmiribel/streamlit-extras")
badge(type="pypi", name="streamlit-extras")
badge(type="twitter", name="streamlit")
badge(type="buymeacoffee", name="arnaudmiribel")

mention(label="查看 Streamlit 官方網站", icon="🌐", url="https://streamlit.io")
        """, language="python")    

    st.header("🎨 進階排版與功能加強（streamlit-extras 功能介紹）")

    st.markdown("""
    `streamlit-extras` 提供許多輔助元件，讓頁面更有彈性、更好用。
    安裝方式：
    ```bash
    pip install streamlit-extras
    ```
    """)

    st.subheader("1. 增加垂直間距")
    st.write("上方段落")
    add_vertical_space(2)
    st.write("下方段落（中間有空白）")

    st.subheader("2. 顯示徽章 badge")
    badge(type="github", name="arnaudmiribel/streamlit-extras")
    badge(type="pypi", name="streamlit-extras")
    badge(type="twitter", name="streamlit")
    badge(type="buymeacoffee", name="arnaudmiribel")

    st.subheader("3. 快速連結提示 mention")
    mention(label="查看 Streamlit 官方網站", icon="🌐", url="https://streamlit.io")
    with st.expander("🔧 :red[Source Code]"):
        st.code("""
st.write("上方段落")
add_vertical_space(2)
st.write("下方段落（中間有空白）")

badge(type="github", name="arnaudmiribel/streamlit-extras")
badge(type="pypi", name="streamlit-extras")
badge(type="twitter", name="streamlit")
badge(type="buymeacoffee", name="arnaudmiribel")

mention(label="查看 Streamlit 官方網站", icon="🌐", url="https://streamlit.io")
        """, language="python")

# --- 頁尾 ---
st.markdown("---")
st.markdown("<div style='text-align:center'>© 2025 Streamlit 教學頁面</div>", unsafe_allow_html=True)

