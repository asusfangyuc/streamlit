# 🌐 核心：Streamlit 主框架
import streamlit as st  # 建立網頁介面與互動元件

# 📊 資料處理與分析
import pandas as pd  # 表格處理與資料分析
import numpy as np  # 數值模擬、陣列操作

# 📈 靜態圖表（Matplotlib / Seaborn）
import matplotlib.pyplot as plt  # 長條圖、折線圖、圓餅圖等
import matplotlib  # 字體與顯示細節設定
import seaborn as sns  # 熱力圖與統計視覺化

# 📉 互動式圖表（Plotly / ECharts）
import plotly.express as px  # 快速建立互動圖表（bar, scatter, line 等）
import plotly.graph_objects as go  # 進階圖表自訂控制（若有需求再用）
from streamlit_echarts import st_echarts  # ECharts 圖表支援（如雷達圖、環形圖）

# 🔧 Streamlit 擴充元件（UI 強化工具）
from streamlit_option_menu import option_menu  # 側邊欄選單元件（導航用）
from streamlit_extras.add_vertical_space import add_vertical_space  # 垂直留白
from streamlit_extras.badges import badge  # GitHub / PyPI 徽章顯示
from streamlit_extras.mention import mention  # 插入 icon 連結提示
from streamlit_extras.stoggle import stoggle  # 可折疊提示（類似 tooltip 說明）

# 頁面基本設定
st.set_page_config(page_title="Streamlit", layout="wide")

# CSS 樣式：米色底、墨綠選單、圓角排版、簡約筆記風
st.markdown("""
<style>
/* 🟡 背景與整體字體 */
body, .main, [data-testid="stAppViewContainer"] {
    background-color: #fefaf1 !important;  /* 奶茶米底 */
    color: #2e2e2e !important;
    font-family: "Helvetica", "微軟正黑體", sans-serif;
}

/* 📚 側邊欄背景與邊框 */
[data-testid="stSidebar"] {
    background-color: #faf5e6 !important;  /* 側邊米白底 */
    border-right: 2px solid #e0dccf;
    padding-top: 2rem;
    box-shadow: 4px 0 8px rgba(0,0,0,0.04);
    min-width: 300px;
    max-width: 340px;
    border-radius: 0 20px 20px 0;
}

/* 📘 logo 動畫：淡入 + 輕縮放 */
@keyframes fadeInZoom {
    0% {opacity: 0; transform: scale(0.8);}
    100% {opacity: 1; transform: scale(1);}
}
.animated-logo {
    animation: fadeInZoom 1.2s ease-in-out;
}

/* 📌 標題字樣式 */
.streamlit-heading {
    font-size: 22px !important;
    font-weight: bold;
    color: #395b64;
    text-align: center;
    margin-bottom: 20px;
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

# 頁面內容
if page == "📘 Streamlit":
    # 頁面設定
    st.set_page_config(page_title="Learning Streamlit - Streamlit 教學", layout="centered")

    # 加入 logo 動畫樣式
    st.markdown("""
    <style>
    @keyframes fadeInZoom {
        0% {
            opacity: 0;
            transform: scale(0.5);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    .animated-logo {
        animation: fadeInZoom 1s ease-in-out;
    }
    </style>
    """, unsafe_allow_html=True)

    # 頁首：僅保留文字主標題（無 logo、無 emoji）
    st.markdown("""
    <h1 style='text-align: center;'>Streamlit</h1>
    <p style='text-align: center;'>Welcome to Study Time! This tab is designed to help you understand the key concepts of Streamlit.</p>
    <p style='text-align: center;'>Please select a topic below to get started.</p>
    """, unsafe_allow_html=True)


    # 建立頁籤
    tabs = st.tabs(["🗺 Overview", "🔧 套件安裝", "📘 Streamlit 簡介"])

    # 分頁 1：Overview
    with tabs[0]:
        st.subheader("🗺 Overview")
        st.markdown("""
        當你開始學習 **Streamlit** 時，可以先從以下幾個面向著手：

        - 📄 **頁面結構**：如何使用 `st.title()`、`st.markdown()` 建立基本內容  
        - 🧩 **互動元件**：加入 `st.button()`、`st.selectbox()` 等  
        - 📊 **資料與圖表**：使用 `pandas` 顯示資料表、`matplotlib` 畫圖  
        - 🚀 **強化功能**：透過 `streamlit-extras`、`streamlit-echarts` 提升互動性與美觀性
        """)

    # 分頁 2：套件說明
    with tabs[1]:
        st.subheader("🔧 套件安裝與用途說明")
        st.markdown("""
        | 套件 | 用途說明 |
        |------|----------|
        | `streamlit` | 建立互動式網頁與介面元件 |
        | `streamlit-extras` | 額外元件（如徽章、連結、空白區）增強功能 |
        | `pandas` | 資料處理與表格顯示 |
        | `numpy` | 數值陣列與隨機資料模擬 |
        | `matplotlib` | 基本圖表繪製（長條圖、折線圖等） |
        | `openpyxl` | 支援讀取 Excel（.xlsx）檔案 |
        """)

        st.code("""
pip install streamlit
pip install streamlit-extras
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install streamlit-echarts
pip install openpyxl
        """, language='bash')

    # 分頁 3：簡介
    with tabs[2]:
        st.subheader("📘 什麼是 Streamlit？")
        st.markdown("""
        Streamlit 是一個讓你用 Python 快速建立 Web 應用程式的工具，適合資料科學、AI 展示、互動式教學等用途。

        🔧 **執行方式：**
        ```bash
        streamlit run app.py
        ```

        🔎 **核心特點：**
        - 快速部署  
        - 支援多種圖表  
        - 支援互動元件  
        - 不需寫 HTML 或 JS  

        🌐 官方展示網站：[https://extras.streamlit.app](https://extras.streamlit.app)
        """)

elif page == "🧮 功能介紹":
    
    st.header("按鈕")

    st.markdown('**超連結：**')
    st.link_button('前往google首頁','https://www.google.com/?hl=zh_TW', type='primary', help='google連結')
    st.link_button('前往youtube首頁','https://www.youtube.com/', disabled=True)

    with st.expander("🔧 :red[Source Code]"):
        st.code("""
st.link_button('前往google首頁','https://www.google.com/?hl=zh_TW', type='primary', help='google連結')
st.link_button('前往youtube首頁','https://www.youtube.com/', disabled=True)""", language="python")
    st.write("")  # 插入一個空行

    st.markdown("**下載按鈕：**")
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


    text_contents = "純文字的text"
    st.download_button('下載 text', text_contents)
    
    with st.expander("🔧 :red[Source Code]"):
        st.code("""
text_contents = "純文字的text"
st.download_button(
'text下載', 
text_contents)""", language="python")


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


    st.title('勾選與下拉式清單')

    st.markdown('**勾選清單：**')
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

    st.markdown('**下拉式清單：**')
    fruit_option = st.selectbox("請選擇你喜歡的水果:",['蘋果','香蕉','櫻桃','葡萄'])
    st.write('你選擇了:',fruit_option)
    with st.expander("🔧 :red[Source Code]"):
        st.code("""
fruit_option = st.selectbox("請選擇你喜歡的水果:",['蘋果','香蕉','櫻桃','葡萄'])
    st.write('你選擇了:',fruit_option)""", language="python")
    st.write("")  # 插入一個空行

    st.markdown('**清單與按鈕應用：投票系統**')
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


    st.title('文字、數字與日期輸入')

    st.markdown('**多行文字輸入**')
    text=st.text_area("輸入分析文字")
    st.write(f'你輸入了{len(text)}個字')

    with st.expander("🔧 :red[Source Code]"):
        st.code("""
text=st.text_area("輸入分析文字")
st.write(f'你輸入了{len(text)}個字')""", language="python")
    st.write("")  # 插入一個空行

    st.markdown('**文字輸入應用：通關密碼：**')
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

    st.markdown("**數值計算**")
    number = st.number_input('輸入一個數字', value=None, step=5, min_value=0, max_value=1000) #step=5,代表每次數值加5
    st.write('你輸入的是',number)
    with st.expander("🔧 :red[Source Code]"):
        st.code("""
number = st.number_input('輸入一個數字', value=None, step=5, min_value=0, max_value=1000)
    st.write('你輸入的是',number)""", language="python")
    st.write("")  # 插入一個空行

    st.markdown('**日期輸入**')
    birthday = st.date_input('你的生日',datetime.date(1990,1,1))
    if st.button('生日確認'): st.write('你的生日是', birthday.strftime('%Y年%m月%d日'))

    with st.expander("🔧 :red[Source Code]"):
        st.code("""
birthday = st.date_input('你的生日',datetime.date(1990,1,1))
    if st.button('生日確認'): st.write('你的生日是', birthday.strftime('%Y年%m月%d日'))""", language="python")
    st.write("")  # 插入一個空行

    st.markdown('**時間設定**')
    t = st.time_input('設定自動時間', value=None, step=3600)
    st.write('自動發信時間',t)
    with st.expander("🔧 :red[Source Code]"):
        st.code("""
t = st.time_input('設定自動時間', value=None, step=3600)
    st.write('自動發信時間',t)""", language="python")
    st.write("")  # 插入一個空行


    st.header("BMI 計算器")
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
    st.error("體重過重")
        """, language="python")


    st.title('流程套件')

    st.markdown('**進度條：**')
    progress_text = "正在處理中..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text + f" {percent_complete + 1}% complete")
    time.sleep(1)
    my_bar.empty()
    st.button("Replay") #在 Streamlit 中，每一次使用者有任何互動（例如按按鈕）時，整個 .py 檔案都會從第一行重新執行一次

    with st.expander("🔧 :red[Source Code]"):
        st.code("""
progress_text = "正在處理中..."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text + f" {percent_complete + 1}% complete")
time.sleep(1)
my_bar.empty()
st.button("Replay")""", language="python")

    st.markdown('**進度流程圖：**')
    with st.status('下載網址中'):
        st.write('搜尋網址中')
        time.sleep(1)
        st.write('搜尋數據中')
        time.sleep(1)
        st.write('下載完成')
    st.button('重新執行')

    with st.expander("🔧 :red[Source Code]"):
        st.code("""
with st.status('下載網址中'):
    st.write('搜尋網址中')
    time.sleep(1)
    st.write('搜尋數據中')
    time.sleep(1)
    st.write('下載完成')
st.button('重新執行')""", language="python")
        
    st.markdown('**跳板通知：**')
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

elif page == "📊 圖表介紹":
    st.header("📊 圖表展示")
    # 最簡明欄位結構
    chart_data = pd.DataFrame([
        ["漸層圖", "matplotlib", "imshow()"],
        ["熱力圖", "seaborn", "heatmap()"],
        ["儀表圖", "plotly", "Indicator(gauge)"],
        ["折線圖", "plotly", "line()"],
        ["長條圖", "plotly", "bar()"],
        ["圓餅圖", "plotly", "Pie()"],
        ["環形圖", "plotly", "Pie(hole=0.5)"],
        ["面積圖", "plotly", "area()"],
        ["瀑布圖", "plotly", "Waterfall()"],
        ["雷達圖", "plotly", "Scatterpolar()"],
        ["漏斗圖", "plotly", "Funnel()"],
        ["氣泡圖", "plotly", "scatter(size=...)"],
        ["地圖", "plotly", "scatter_mapbox()"]
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
    st.header("🕴 GAI 新聞摘要")
    st.write("這裡是 GAI 新聞摘要內容...")

elif page == "  📈 數據分析助手":
    st.header("📈 數據分析助手")
    st.write("這裡是 數據分析助手內容...")
    
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

# --- 頁尾 ---
st.markdown("---")
st.markdown("<div style='text-align:center'>© 2025 Streamlit 教學頁面</div>", unsafe_allow_html=True)