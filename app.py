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
from PIL import Image
st.set_page_config(layout="wide")
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

#st.set_page_config(page_title='Ukraina-Rusia', page_icon="🇺🇦", layout="wide")
st.beta_set_page_config(page_title='your_title', page_icon = "🇺🇦", layout = 'wide', initial_sidebar_state = 'auto')

# Judul
st.markdown("# Benarkah Konflik Ukraina dan Rusia Menyebabkan Krisis Pangan ?<br />\
            <p style='font-family:Arial; color:Black; font-size: 28px;'>Analisis Dibandingkan dengan Krisis Pangan 2007-2008", unsafe_allow_html=True)
st.text('by Nadhiar Ridho Wahyu Pradana')

st.markdown('<p style="font-family:Arial; color:Black; font-size: 16px;">\
            Dari 8 bulan sejak dimulainya Konflik <b>Ukraina - Rusia (Februari - Oktober 2022)</b>, banyak dampak signifikan telah diterima di seluruh dunia.\
            Salah satunya adalah <b>krisis pangan global lainnya yang tumpang tindih dengan krisis pangan akibat Covid-19</b>. Hal ini karena kedua peperangan utama memiliki posisi yang signifikan sebagai produsen komoditas terkait pangan.\
            HDi sini saya akan membahas tentang <b>seberapa banyak perubahan yang telah diambil pasar makanan global selama krisis</b>, \
            dan <b>bagaimana jika dibandingkan</b> dengan krisis harga pangan terkenal lainnya selama abad ke-21, yang dalam hal ini <b>Krisis Harga Pangan 2007-2008.</b></p>',
            unsafe_allow_html=True)

st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.header("A. Ukraina & Rusia merupakan Negara Penting dalam Pasar Agrifood Dunia")

# Global Export Fraction 
st.markdown('<h4 style="font-family:Arial; background-color: beige">'+
            '&ensp;Ukraina & Rusia adalah pengekspor besar komoditas utama yang mendukung ketahanan pangan global\
            </h4>', unsafe_allow_html=True)
export_1, export_2 = st.columns(2)
exp_food = pd.read_csv("data/1a_export_fraction_food.csv")
exp_fert = pd.read_csv("data/1b_export_fraction_fertilizer.csv")
with export_1:
    # Plot Food Export Fraction
    fig1 = px.bar(exp_food, y="Commodity", x="ExportShare_19-20", color="Country", orientation='h', 
              range_x=[0,50], width=600, height=300,
              color_discrete_sequence=['rgba(255,244,51,0.8)', 'rgba(37,58,255,0.8)'],
              template="simple_white")
    fig1.update_layout(title_text="<b>Global Food Export Fraction Ukraina & Rusia, 2019-2020</b>",
                       legend=dict(y=0.5, xanchor="right", title="Export Source"))
    fig1.update_traces(hovertemplate='<b>%{y}</b><br> Export Fraction: %{x:.2f}%<extra></extra>')
    fig1.update_xaxes(title="<b>Export Fraction (%)</b>",tickfont=dict(size=16), showgrid=True, gridcolor='black')
    fig1.update_yaxes(title=None, tickfont=dict(size=16))
    st.plotly_chart(fig1)
    st.caption("Source : UN Comtrade Database, https://comtrade.un.org/data.")
with export_2:
    # Plot Fertilizer Export Fraction
    fig2 = px.bar(exp_fert, y="Commodity", x="ExportShare_19-20", color="Country", orientation='h', 
              range_x=[0,50], width=600, height=300,
              color_discrete_sequence=['rgba(37,58,255,0.8)', 'rgba(221, 30, 30, 0.8)'],
              template="simple_white")
    fig2.update_layout(title_text="<b>Global Fertilizer Export Fraction dari Rusia & Belarus, 2019-2020</b>",
                       legend=dict(y=0.5, xanchor="right", title="Export Source"))
    fig2.update_traces(hovertemplate='<b>%{y}</b><br> Export Fraction: %{x:.2f}%<extra></extra>')
    fig2.update_xaxes(title="<b>Export Fraction (%)</b>",tickfont=dict(size=16), showgrid=True, gridcolor='black')
    fig2.update_yaxes(title=None, tickfont=dict(size=16))
    st.plotly_chart(fig2)
    st.caption("Source : UN Comtrade Database, https://comtrade.un.org/data.")
    
export_3, export_4 = st.columns(2)
with export_3:
    st.markdown(p_format+'<b>Untuk komoditas makanan</b>, kedua negara ini adalah eksportir terkemuka dari<br><b>dua komoditas :</b><br>'\
                '&emsp;1. <b>Cereals</b> : Wheat, Corn (Maize), Barley<br>'\
                '&emsp;2. <b>Vegetable oils</b> : Sunflower oil, Rapeseed oil', unsafe_allow_html=True)
#with export_4:
#    st.markdown(p_format+'<b>untuk komoditas non-makanan</b>, Rusia juga merupakan pengekspor terkemuka pupuk berbasis <b>Nitrogen, Fosfor, dan Kalium, </b>'\ 
#                'sekaligus menjadi salah satu produsen bahan bakar terkemuka seperti minyak mentah dan gas alam.', unsafe_allow_html=True)    
#st.markdown("---") 

with export_4:
    st.markdown(p_format+'<b>Untuk komoditas non-makanan</b>, Rusia juga merupakan pengekspor terkemuka pupuk berbasis <b>Nitrogen, Fosfor, dan Kalium, </b>'\
        'sekaligus menjadi salah satu produsen bahan bakar terkemuka seperti minyak mentah dan gas alam.', unsafe_allow_html=True)    
st.markdown("---") 

st.header("B. Kesimpulan")

st.markdown(p_format+'<b> Kesimpulan sementara yaitu konflik Rusia-Ukraina dapat menyebabkan krisis pangan dunia. </b>', 
    unsafe_allow_html=True)

# Referensi
with st.expander("REFERENSI"):
    st.markdown(p_format+'[1] FAO. (2022). The FAO Food Price Index drops for the third consecutive month in June. <a href="https://www.fao.org/worldfoodsituation/foodpricesindex/en">link</a>.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[2] GAPKI. (2021). Production Drops After Public Curb, CPO Sees Highest Price. <a href="https://gapki.id/en/news/20528/production-drops-after-public-curb-cpo-sees-highest-price">link</a>.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[3] The World Bank. (2022). The impact of the war in Ukraine on commodity markets. <a href="https://www.worldbank.org/en/research/commodity-markets">link</a>.', 
                unsafe_allow_html=True)  
#st.markdown(p_format+"<b>Data last updated : 05 August 2022</b>", unsafe_allow_html=True)