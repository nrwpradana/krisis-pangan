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

# Judul
st.markdown("# Benarkah Konflik Rusia-Ukraina Menyebabkan Krisis Pangan ?<br />\
            <p style='font-family:Arial; color:Black; font-size: 28px;'>Analisis Dibandingkan dengan 2007-2008 World Food Price Crisis", unsafe_allow_html=True)

# Ringkasan
st.markdown('<p style="font-family:Arial; color:Black; font-size: 16px;">\
            From 6 months since the start of <b>Ukraine-Russia Conflict (February - August 2022)</b>, many significant impacts have been received around the globe.\
            One of which is yet another <b>global food crisis that overlaps with food crisis due to Covid-19</b>. This is because both of the main belligerents have significant position as a producer of food-related commodities.\
            Here we\'ll discuss about <b>how much changes the global food market already taken during the crisis</b>, \
            and <b>how does it compare</b> to other infamous food price crisis during the 21st century, which in this case the <b>2007-2008 Food Price Crisis.</b></p>',
            unsafe_allow_html=True)

#---------------SECTION 1 : General Overview --------------------------
# SECTION 1.1 : Export Fraction from RUS-UKR
#-------------------------------------------
st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.header("A. Ukraine&Russia as Important Players in Agrifood Markets")
# Global Export Fraction Section
st.markdown('<h4 style="font-family:Arial; background-color: beige">'+
            '&ensp;Ukraine&Russia are high exporter of key commodities that support global food security\
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
    fig1.update_layout(title_text="<b>Global Food Export Fraction from Ukraine&Russia, 2019-2020</b>",
                       legend=dict(y=0.5, xanchor="right", title="Export Source"))
    fig1.update_traces(hovertemplate='<b>%{y}</b><br> Export Fraction: %{x:.2f}%<extra></extra>')
    fig1.update_xaxes(title="<b>Export Fraction (%)</b>",tickfont=dict(size=16), showgrid=True, gridcolor='black')
    fig1.update_yaxes(title=None, tickfont=dict(size=16))
    st.plotly_chart(fig1)
    st.caption("Source : UN Comtrade Database, https://comtrade.un.org/data. Accessed on July 2022.")
with export_2:
    # Plot Fertilizer Export Fraction
    fig2 = px.bar(exp_fert, y="Commodity", x="ExportShare_19-20", color="Country", orientation='h', 
              range_x=[0,50], width=600, height=300,
              color_discrete_sequence=['rgba(37,58,255,0.8)', 'rgba(221, 30, 30, 0.8)'],
              template="simple_white")
    fig2.update_layout(title_text="<b>Global Fertilizer Export Fraction from Russia&Belarus, 2019-2020</b>",
                       legend=dict(y=0.5, xanchor="right", title="Export Source"))
    fig2.update_traces(hovertemplate='<b>%{y}</b><br> Export Fraction: %{x:.2f}%<extra></extra>')
    fig2.update_xaxes(title="<b>Export Fraction (%)</b>",tickfont=dict(size=16), showgrid=True, gridcolor='black')
    fig2.update_yaxes(title=None, tickfont=dict(size=16))
    st.plotly_chart(fig2)
    st.caption("Source : UN Comtrade Database, https://comtrade.un.org/data. Accessed on July 2022.")
    
export_3, export_4 = st.columns(2)
with export_3:
    st.markdown(p_format+'<b>As for food</b>, both of these countries are leading net exporter of <br><b>two commodity categories :</b><br>'\
                '&emsp;1. <b>Cereals</b> : Wheat, Corn (Maize), Barley<br>'\
                '&emsp;2. <b>Vegetable oils</b> : Sunflower oil, Rapeseed oil', unsafe_allow_html=True)
with export_4:
    st.markdown(p_format+'<b>And for non-food commodities</b>, Russia is also a leading net exporter of <b>Nitrogenous, Phosphorus, and Potassium-based fertilizers, </b>'\
        'while being one of the leading fuel producer like crude oil and natural gas.', unsafe_allow_html=True)    
st.markdown("---") 

#-------------------------------------------
# SECTION : Conclusion
#-------------------------------------------
st.header("B. Kesimpulan")

st.markdown(p_format+'Kesimpulan sementara yaitu konflik Rusia-Ukraina dapat menyebabkan krisis pangan dunia.', 
    unsafe_allow_html=True)

# References
with st.expander("REFERENSI"):
    st.markdown(p_format+'[1] FAO. (2022). The FAO Food Price Index drops for the third consecutive month in June. <a href="https://www.fao.org/worldfoodsituation/foodpricesindex/en">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[2] GAPKI. (2021). Production Drops After Public Curb, CPO Sees Highest Price. <a href="https://gapki.id/en/news/20528/production-drops-after-public-curb-cpo-sees-highest-price">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[4] The World Bank. (2022). The impact of the war in Ukraine on commodity markets. <a href="https://www.worldbank.org/en/research/commodity-markets">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True)  
#st.markdown(p_format+"<b>Data last updated : 05 August 2022</b>", unsafe_allow_html=True)
