import sys

print(sys.version)

import os
from pdb import line_prefix
import sys
import streamlit as st
import pandas as pd
import numpy as np
import figure_style as fs
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from PIL import Image
st.set_page_config(page_title='Krisis Pangan', page_icon = "🍔", layout = 'wide', initial_sidebar_state = 'auto')
st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: large;
}
</style>
""",
    unsafe_allow_html=True,
)
p_format = '<p style="font-family:Arial; color:Black; font-size: 16px;">'

st.markdown("# Benarkah Konflik Ukraina dan Rusia Menyebabkan Krisis Pangan ?<br />\
            <p style='font-family:Arial; color:Black; font-size: 28px;'>Dibanding dengan Krisis Pangan 2007-2008", unsafe_allow_html=True)
st.text('by Nadhiar Ridho Wahyu Pradana')

st.markdown('<p style="font-family:Arial; color:Black; font-size: 16px;">\
            Dari 8 bulan sejak dimulainya Konflik <b>Ukraina - Rusia (Februari - Oktober 2022)</b>, banyak dampak signifikan telah diterima di seluruh dunia.\
            Salah satunya adalah <b>krisis pangan global lainnya yang tumpang tindih dengan krisis pangan akibat Covid-19</b>. Hal ini karena kedua peperangan utama memiliki posisi yang signifikan sebagai produsen komoditas terkait pangan.\
            HDi sini saya akan membahas tentang <b>seberapa banyak perubahan yang telah diambil pasar makanan global selama krisis</b>, \
            dan <b>bagaimana jika dibandingkan</b> dengan krisis harga pangan terkenal lainnya selama abad ke-21, yang dalam hal ini <b>Krisis Harga Pangan 2007-2008.</b></p>',
            unsafe_allow_html=True)

st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

#BAGIAN A

st.markdown('<h2 style="font-family:Arial;background-color: skyblue">'+
            'A. Perubahan Harga Komoditas Tahun 2022</h2><br>', unsafe_allow_html=True)

html_string = '''
<iframe title="Commodity price changes in 2022" aria-label="Column Chart" id="datawrapper-chart-BI2gD" 
src="https://datawrapper.dwcdn.net/BI2gD/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; 
border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";
window.addEventListener("message",(function(e){if(void 0!==e.data["datawrapper-height"]){var t=document.querySelectorAll("iframe");
for(var a in e.data["datawrapper-height"])for(var r=0;r<t.length;r++){if(t[r].contentWindow===e.source)t[r].style.height=e.data["datawrapper-height"][a]+"px"}}}))}();</script>
'''
components.html(html_string,height=430)

st.markdown(p_format+'<b>Perang di Ukraina telah memberikan gejolak besar bagi pasar komoditas.</b> Pandangan Pasar Komoditas terbaru dari Bank Dunia membahas bagaimana '\
    'perang telah mengganggu produksi dan perdagangan beberapa komoditas, terutama di mana Rusia dan Ukraina adalah eksportir utama, termasuk energi, pupuk, dan biji-bijian.'\
    ' Kenaikan harga ini terjadi di atas pasar komoditas yang sudah ketat karena pemulihan permintaan yang solid dari pandemi Covid-19, serta berbagai kendala pasokan terkait pandemi.',unsafe_allow_html=True)
st.markdown("---") 

#BAGIAN B

st.markdown('<h2 style="font-family:Arial;background-color: skyblue">'+
            'B. Ekspor Bahan Pangan Ukraina - Rusia</h2>', unsafe_allow_html=True)

# Global Ekspor
st.markdown('<h4 style="font-family:Papyrus; background-color: white"><i><center><br>'+\
            '"Ukraina & Rusia adalah pengekspor besar komoditas utama yang mendukung ketahanan pangan global"<br>\
            </center></i></h4>', unsafe_allow_html=True)
export_1, export_2 = st.columns(2)
exp_food = pd.read_csv("data/1a_export_fraction_food.csv")
exp_fert = pd.read_csv("data/1b_export_fraction_fertilizer.csv")
with export_1:
    # Plot Food Export Fraction
    fig1 = px.bar(exp_food, y="Commodity", x="ExportShare_19-20", color="Country", orientation='h', 
              range_x=[0,50], width=600, height=300,
              color_discrete_sequence=['rgba(255,244,51,0.8)', 'rgba(37,58,255,0.8)'],
              template="simple_white")
    fig1.update_layout(title_text="<b>Ekspor Agrifood Ukraina & Rusia 2019-2020</b>",
                       legend=dict(y=0.5, xanchor="right", title="Negara"))
    fig1.update_traces(hovertemplate='<b>%{y}</b><br> Persentase Ekspor: %{x:.2f}%<extra></extra>')
    fig1.update_xaxes(title="<b>Persentase Ekspor (%)</b>",tickfont=dict(size=16), showgrid=False, gridcolor='black')
    fig1.update_yaxes(title=None, tickfont=dict(size=16))
    st.plotly_chart(fig1)
    st.caption("Sumber : UN Comtrade Database, https://comtradeplus.un.org/.")
with export_2:
    # Plot Fertilizer Export Fraction
    fig2 = px.bar(exp_fert, y="Commodity", x="ExportShare_19-20", color="Country", orientation='h', 
              range_x=[0,50], width=600, height=300,
              color_discrete_sequence=['rgba(49,36,79,255)', 'rgba(221, 30, 30, 0.8)'],
              template="simple_white")
    fig2.update_layout(title_text="<b>Ekspor Pupuk Rusia 2019-2020</b>",
                       legend=dict(y=0.5, xanchor="right", title="Negara"))
    fig2.update_traces(hovertemplate='<b>%{y}</b><br> Persentase Ekspor: %{x:.2f}%<extra></extra>')
    fig2.update_xaxes(title="<b>Persentase Ekspor (%)</b>",tickfont=dict(size=16), showgrid=False, gridcolor='black')
    fig2.update_yaxes(title=None, tickfont=dict(size=16))
    st.plotly_chart(fig2)
    st.caption("Sumber : UN Comtrade Database, https://comtradeplus.un.org/.")
    
export_3, export_4 = st.columns(2)
with export_3:
#    st.markdown(p_format+'<b>Untuk komoditas makanan</b>, kedua negara ini adalah eksportir terkemuka dari<br><b>dua komoditas :</b><br>'\
#                '&emsp;1. <b>Cereals</b> : Wheat, Corn (Maize), Barley<br>'\
#                '&emsp;2. <b>Vegetable oils</b> : Sunflower oil, Rapeseed oil', unsafe_allow_html=True)
    st.markdown('<h5 style="font-family:Arial; background-color: white"><br>'+\
            'Ukraina dan Rusia merupakan eksportir besar komoditas<br>Cereals dan Vegetables Oil.\
            </h5>', unsafe_allow_html=True)

with export_4:
#    st.markdown(p_format+'<b>Untuk komoditas non-makanan</b>, Rusia juga merupakan pengekspor terkemuka pupuk berbasis <b>Nitrogen, Fosfor, dan Kalium, </b>'\
#        'sekaligus menjadi salah satu produsen bahan bakar terkemuka seperti minyak mentah dan gas alam.', unsafe_allow_html=True)    
     st.markdown('<h5 style="font-family:Arial; background-color: white"><br>'+\
            'Rusia merupakan eksportir pupuk pertanian seperti<br>Potassium, Phospate dan Nitrogen.\
            </h5>', unsafe_allow_html=True)
st.markdown("---") 

#BAGIAN C

st.header("C. Inflase Harga Komoditas")

col_211, col_212, padding_21 = st.columns([1,5,5])
with col_211:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/FAO_logo.svg/800px-FAO_logo.svg.png", width=100)
with col_212:
    st.info("### FAO Food Price Index (FFPI)")
st.markdown(p_format+'FFPI measures the <b>monthly change in international prices of several food commodities.</b>\
            It\'s measured as the average of five categories weighted by the average export shares of each groups over 2014-2016.',unsafe_allow_html=True)
# Read FFPI Index Value
df_08 = pd.read_excel('data/3a_FAO_FPPI.xlsx', sheet_name='Index_08')
df_08['Date'] = pd.to_datetime(df_08['Date'], format='%d/%m/%Y')
df_22 = pd.read_excel('data/3a_FAO_FPPI.xlsx', sheet_name='Index_22')
df_22['Date'] = pd.to_datetime(df_22['Date'], format='%d/%m/%Y')

FAO_idx, FAO_inf = st.tabs(["📈 FFPI", "🔺 FFPI Inflation"])
with FAO_idx:
    # Plot Index Value
    plt_ffpi_08, plt_ffpi_22 = st.columns(2)
    f_ffpi_08 = fs.plot_fao_idx(df_08, 'Food Price Crisis (2008) Timeframe')
    f_ffpi_22 = fs.plot_fao_idx(df_22, 'Ukraine Crisis (2022) Timeframe')
    st.markdown('<p style="font-family:Arial; color:Black; font-size: 16px;"><b>Note : 2014-2016 = 100</b></p>', unsafe_allow_html=True)
    plt_ffpi_08.plotly_chart(f_ffpi_08); plt_ffpi_22.plotly_chart(f_ffpi_22)
    st.caption('Data Source : FAO, https://www.fao.org/worldfoodsituation/foodpricesindex/. Accessed on July 2022')
    # Summary Description
    st.markdown(p_format+'<b>In general, index values from 2022 timeframe tend to have higher value than its 2008 counterparts for all categories except dairy.</b> \
                The most <b>drastic difference is from vegetable oils index<b> which at its peak <b>surpasses its 2008 values by 60-90%</b>. \
                <b>A similar trend</b> also emerges where the index steadily climbs up until around June in the last year (2008, 2022) where it starts to stabilize.',
                unsafe_allow_html=True)
    st.markdown(p_format+'<b>Looking at the nominal value, FPI in June 2022 is down to 154 (-2,3%) from the previous month, and has been on down slope from March. However, it\'s still around 23\% more than 2021 value. \
                Cereals and vegetable oils are also having similar trend</b>, as with both of them are the most affected categories among the five categories. \
                On the other hands, <b>meat, dairy and sugar</b> is still having an upward trend with substantially lower inflation rate</b> compared to the other two.', 
                unsafe_allow_html=True)
    st.markdown(p_format+'International price has been dropping for cereals due to higher wheat availability from northern hemisphere, \
        higher maize stocks from South America due to harvests progressed ahead of time, which also exerting downward pressure to other grain prices, weakening them as a result. \
        On the other hands, vegetable oils prices have also declining due to better export prospect of palm oil from Indonesia, \
        sluggish import demand for sunflower and soybean oil, and upcoming harvest season in general [1].',
                unsafe_allow_html=True)

# Plot Index Inflation
ffpi_inf = pd.read_excel('data/3a_FAO_FPPI.xlsx', sheet_name='Inflation')
with FAO_inf:
    fao_cat = ['Food Price Index', 'Meat', 'Dairy', 'Cereals', 'Edible Oils', 'Sugar']
    fao_by_cat = st.radio("BY CATEGORIES :", fao_cat, horizontal=True) 
    ffpi_inf_1, ffpi_inf_2 = st.columns([6,5])
    if fao_by_cat:
        f_ffpi_inf = fs.plot_idx_inf(ffpi_inf, fao_by_cat, "FFPI Inflation Rate 2022 v.s. 2008")
        ffpi_inf_1.plotly_chart(f_ffpi_inf)
    ffpi_inf_1.caption('Data Source : FAO, https://www.fao.org/worldfoodsituation/foodpricesindex/. Accessed on July 2022')
    ffpi_inf_1.caption('Inflation rate is measured as changes in nominal prices during the 23-month period e.g. Jan 2022 v.s. Jan 2020.')
    # Summary Description
    with ffpi_inf_2:
        st.markdown(p_format+'<br><br><br><b>2022 Inflation rate is substantially lower for FPI, dairy, and cereals compared to 2008. \
            Lower value may be attibuted to higher food prices in 2020 due to Covid-19 whereas 2006 is more stable.</b><br><br> \
            However <b>edible oils and sugar 2022 receives higher inflation rate</b> which may be because the market for these two categories is <b>more volatile due to fast development of biofuels</b>, \
            which takes on share of which edible oils and sugar used upon. Lastly meat index inflation has similar values between crisis.',
            unsafe_allow_html=True)


st.markdown('---')
col_221, col_222, padding_22 = st.columns([1,5,5])
with col_221:
    st.image("https://brandlogos.net/wp-content/uploads/2021/12/world_bank-brandlogo.net_.png", width=100)
with col_222:
    st.info("### World Bank Commodities Price Data")

# Read WB Commodity Price Value
wb_cp_08 = pd.read_csv('data/3b_CMO_food_fert_08.csv')
wb_cp_08['Date'] = pd.to_datetime(df_08['Date'], format='%d/%m/%Y')
wb_cp_22 = pd.read_csv('data/3b_CMO_food_fert_22.csv')
wb_cp_22['Date'] = pd.to_datetime(df_22['Date'], format='%d/%m/%Y')
 
WB_idx, WB_inf, WB_idx_inf = st.tabs(["📈 Commodity Price (CP)", "🔺 Commodity Price Inflation", "🔶 Commodity Index Inflation"])

with WB_idx:
    # Plot WB CP Value
    cp_by_cat = st.radio("BY CATEGORIES :", ['Grains', 'Edible Oils', 'Fertilizers'], horizontal=True) 
    plt_cp_08, plt_cp_22 = st.columns(2)
    f_cp_08 = fs.plot_wb_cp(wb_cp_08, 'Food Price Crisis (2008) Timeframe', cp_by_cat)
    f_cp_22 = fs.plot_wb_cp(wb_cp_22, 'Ukraine Crisis (2022) Timeframe', cp_by_cat)
    plt_cp_08.plotly_chart(f_cp_08); plt_cp_22.plotly_chart(f_cp_22)
    st.caption('Source : World Bank Commodities Price Data, https://www.worldbank.org/en/research/commodity-markets. Accessed on July 2022')
    
    # Summary Description
    st.markdown(p_format+'<b>For grains, the price of wheat, soybean, and maize have reached higher peak than in the 2008 timeframe back in March and slowly stabilizing onwards.</b>\
        <b>Rice on the other hands is more stable during 2022 crisis</b>, unlike 2008 crisis where it\'s also highly affected alongside other commodities. \
        Here we can see that distruption of grain supplies from the Black Sea truly affecting global grain prices. We may also exert it to the spike of fertilizers price since maize and wheat are fertilizer-intensive crops.', unsafe_allow_html=True)
    
    st.markdown(p_format+'<b>All of edible oil products reach new peak during 2022 timeframe compared to 2008. Currently the price sits at around 15-40% increase since the start of 2022.</b>\
        Several key factors affecting edible oils price inflation : [2, 3]<br>. \
        &ensp;&ensp;1. Palm oil production decline from Indonesia & Malaysia amidst Covid-19 pandemic.<br>\
        &ensp;&ensp;2. Evergrowing biofuel production which ultimately uses palm oil and soybean oil as primary ingredients.<br>\
        &ensp;&ensp;3. Supply chain distruption from Ukraine & Russia due to ongoing conflict.<br>\
        &ensp;&ensp;4. Recent drought in Brazil which reduces soybean supply capacity.', unsafe_allow_html=True)
    
    st.markdown(p_format+'<b>Continuing uptrend since 2020, fertilizers prices reached its peak during March 2022.</b> \
        <b>Higher price spike is observed for Urea and Potassium Chloride compared to 2008 crisis</b>, while <b>Phosphate-based fertilizer veils lower than 2008.</b> \
        Several key factors affecting fertilizers price inflation : [4, 5]<br>\
        &ensp;&ensp;1. Price increase of natural gas which is one of the main ingredient for Nitrogenous fertilizers.<br>\
        &ensp;&ensp;2. Economic sanctions which cut off fertilizers trade from Russia and Belarus.<br>\
        &ensp;&ensp;3. Export restriction from Russia and China to ensure the fulfillment domestic needs first.', unsafe_allow_html=True)
    
# Read WB CP Inflation Data
wb_cp_inf = pd.read_csv('data/3b_CMO_food_fert_inflation_08&22.csv')
with WB_inf:
    # Plot WB CP Inflation
    cp_cat = ['Palm oil', 'Soybean oil','Rapeseed oil','Sunflower oil',
              'Soybeans', 'Maize', 'Rice', 'Wheat, US',
              'Phosphate rock', 'DAP', 'TSP', 'Urea', 'Potassium chloride']
    cp_inf_by_cat = st.selectbox("BY CATEGORIES :", cp_cat)

    cp_inf_1, cp_inf_2 = st.columns([6,5])
    if fao_by_cat:
        f_cp_inf = fs.plot_idx_inf(wb_cp_inf, cp_inf_by_cat, "WB Commodity Price Inflation Rate 2022 v.s. 2008")
        cp_inf_1.plotly_chart(f_cp_inf)
    cp_inf_1.caption('Data Source : World Bank Commodities Price Data, https://www.worldbank.org/en/research/commodity-markets. Accessed on July 2022')
    cp_inf_1.caption('Inflation rate is measured as changes in nominal prices during the 23-month period e.g. Jan 2022 v.s. Jan 2020.')
    
    # Summary Description
    with cp_inf_2:
        st.markdown(p_format+'<br><br><br><b>Taking a note from rice price data, we can also see that rice prices during 2022 deflate compared to 2020.</b> \
            <b>Other grains inflation except for wheat also tend to be lower than 2008 crisis, however it\'s still in the range of 50-150% inflation compared to 2020.</b><br><br>\
            <b>All edible oils inflation rate</b>, except rapeseed oil which rocketed to 200%, <b>have similar profile to 2008 crisis</b>, that is in the realm of 150-200%.<br><br>\
            <b>As for fertilizers, their inflation rate is kept around 150-300%</b>. Phosphate rock and potassium chloride have similar inflation rate profiles to 2008 crisis. \
            Urea already reach its 2008 highest peak from the start of the year. <b>DAP and TSP inflation rate is substantially lower than during 2008 crisis.</b>',
            unsafe_allow_html=True)
    
# Read WB Index Inflation Data
wb_cp_idx_inf = pd.read_csv('data/3b_CMO_indices_inflation_08&22.csv')
wb_cp_idx_inf['Date'] = pd.to_datetime(wb_cp_idx_inf['Date'], format='%d/%m/%Y')    
with WB_idx_inf:
    # Plot WB Index Inflation
    cp_idx_inf_1, cp_idx_inf_2 = st.columns([7,5])
    f_cp_idx_inf = fs.plot_wb_idx_inf(wb_cp_idx_inf)
    cp_idx_inf_1.plotly_chart(f_cp_idx_inf)
    st.caption('Source : World Bank Commodities Price Data, https://www.worldbank.org/en/research/commodity-markets. Accessed on July 2022')
    
    # Summary Description
    with cp_idx_inf_2:
        st.markdown('<p style="font-family:Arial; color:Black; font-size: 24px;">'+'<br><br><br> \
            Looking at food and fertilizers price inflation during the 21st century, the current price spike ranks second to 2007-2008 food price crisis and only third after 1974 global recession.',
            unsafe_allow_html=True)

st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.header("C. Kesimpulan")

st.markdown(p_format+'<b> Kesimpulan sementara yaitu konflik Rusia-Ukraina dapat menyebabkan krisis pangan dunia. </b>', 
    unsafe_allow_html=True)
st.markdown("---") 


# Referensi
with st.expander("REFERENSI"):
    st.markdown(p_format+'[1] FAO. (2022). The FAO Food Price Index drops for the third consecutive month in June. <a href="https://www.fao.org/worldfoodsituation/foodpricesindex/en">link</a>.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[2] GAPKI. (2021). Production Drops After Public Curb, CPO Sees Highest Price. <a href="https://gapki.id/en/news/20528/production-drops-after-public-curb-cpo-sees-highest-price">link</a>.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[3] The World Bank. (2022). The impact of the war in Ukraine on commodity markets. <a href="https://www.worldbank.org/en/research/commodity-markets">link</a>.', 
                unsafe_allow_html=True)  
