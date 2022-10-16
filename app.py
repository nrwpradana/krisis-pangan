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
    st.markdown('<h5 style="font-family:Arial; background-color: white"><br>'+\
            'Ukraina dan Rusia merupakan eksportir besar komoditas<br>Cereals dan Vegetables Oil.\
            </h5>', unsafe_allow_html=True)

with export_4:    
     st.markdown('<h5 style="font-family:Arial; background-color: white"><br>'+\
            'Rusia merupakan eksportir pupuk pertanian seperti<br>Potassium, Phospate dan Nitrogen.\
            </h5>', unsafe_allow_html=True)
st.markdown("---") 

st.markdown('<h5 style="font-family:Papyrus; background-color: paleturquoise"><i>'+
            'Banyak negara berkembang sangat bergantung pada impor pangan pertanian dari Ukraina dan Rusia*\
            </i></h5>', unsafe_allow_html=True)

#Summary
#st.markdown('#### Observasi 75 negara non-Eropa yang dianggap negara berkembang dan kurang berkembang*:')
import_1, import_2 = st.columns(2)
with import_1:
    st.markdown("# 🍞 xx,xx%")
    st.markdown(p_format+'<b>Memiliki ketergantungan terhadap impor pangan pertanian dari Ukraina-Rusia</b>', unsafe_allow_html=True)
with import_2:
    st.markdown("# 🥡 xx,xx%")
    st.markdown(p_format+'<b>Memiliki ketergantungan pupuk pertanian dari Rusia</b>', unsafe_allow_html=True)
st.caption("\* Berdasarkan \"Special Region\" group dari FAOSTAT")
#st.caption("\** Import proportion >25%")
#df for Import Fraction
import_share = pd.read_csv("data/2_import_rus_ukr_18-20.csv").fillna(0)
fil_import_inc = np.sort(np.append(import_share['IncGroups_WB'].unique(), "All"))
fil_import_reg = np.sort(np.append(import_share['Regions_WB'].unique(), "All"))
import_share_wheat = import_share.sort_values('Wheat_TOT', ascending=True).reset_index(drop=True)
import_share_fert  = import_share.sort_values('Fertilizer', ascending=True).reset_index(drop=True)
#Bar Chart for Import Fraction
with st.expander("Detail Impor"):
    filter_11, filter_12 = st.columns(2); st.markdown("---")
    plt_import_wheat, plt_import_fert = st.columns(2)
    # Filter by Regions and Incomes
    with filter_11:
        import_by_region = st.radio("BY REGIONS :", fil_import_reg) 
    with filter_12:
        import_by_income = st.radio("BY INCOMES :", fil_import_inc)
    # Plot Import Fraction with Filter  
    if (import_by_income == "All") and (import_by_region == "All"):
        f_imp_wheat, f_imp_fert = fs.plot_import(import_share_wheat, import_share_fert)
    elif import_by_income == "All":
        slice_wheat = import_share_wheat[import_share_wheat["Regions_WB"] == import_by_region]
        slice_fert  = import_share_fert[import_share_fert["Regions_WB"] == import_by_region]
        f_imp_wheat, f_imp_fert = fs.plot_import(slice_wheat, slice_fert)
    elif import_by_region == "All":
        slice_wheat = import_share_wheat[import_share_wheat["IncGroups_WB"] == import_by_income]
        slice_fert  = import_share_fert[import_share_fert["IncGroups_WB"] == import_by_income]
        f_imp_wheat, f_imp_fert = fs.plot_import(slice_wheat, slice_fert)
    else:
        filter_import = (import_share["Regions_WB"] == import_by_region) & (import_share["IncGroups_WB"] == import_by_income)
        slice_wheat = import_share[filter_import].sort_values("Wheat_TOT", ascending=True).reset_index(drop=True)
        slice_fert  = import_share[filter_import].sort_values("Fertilizer", ascending=True).reset_index(drop=True)
        f_imp_wheat, f_imp_fert = fs.plot_import(slice_wheat, slice_fert)
    
    plt_import_wheat.plotly_chart(f_imp_wheat); plt_import_fert.plotly_chart(f_imp_fert)
    plt_import_wheat.caption("Sumber : UN Comtrade Database, https://comtradeplus.un.org/.")
    plt_import_fert.caption("Sumber : UN Comtrade Database, https://comtradeplus.un.org/.")
    st.caption('\* Missing data for wheat&fertilizers import \
               &ensp;\*\* Missing data for fertilizers import')
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
