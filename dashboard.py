import os
from pdb import line_prefix
import sys
#os.chdir(os.path.dirname(sys.argv[0]))
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

# Cover Image
cover = Image.open('./cover_wheat.png')
st.image(cover, use_column_width=True)
# Title
st.markdown("# How Much does The War in Ukraine Impact Global Food Market?<br />\
            <p style='font-family:Arial; color:Black; font-size: 28px;'>A Comparative Analysis with 2007-2008 World Food Price Crisis", unsafe_allow_html=True)
# Summary
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
# SECTION 1.2 : Import Fraction from RUS-UKR
#-------------------------------------------
st.markdown('<h4 style="font-family:Arial; background-color: beige">'+
            '&ensp;Many developing and least developed countries highly reliant on agrifood imports from Ukraine and Russia\
            </h4>', unsafe_allow_html=True)
#Summary
st.markdown('#### Observing 75 non-European countries considered as developing and least developed countries*:')
import_1, import_2 = st.columns(2)
with import_1:
    st.markdown("# :ear_of_rice: 46,7%")
    st.markdown(p_format+'<b>Having high dependance** to wheat imports from Ukraine and Russia</b>', unsafe_allow_html=True)
with import_2:
    st.markdown("# 🧴 22,7%")
    st.markdown(p_format+'<b>Having high dependance** to fertilizers imports from Russia</b>', unsafe_allow_html=True)
st.caption("\* Based on \"Special Region\" group from FAOSTAT")
st.caption("\** Import proportion >25%")
#df for Import Fraction
import_share = pd.read_csv("data/2_import_rus_ukr_18-20.csv").fillna(0)
fil_import_inc = np.sort(np.append(import_share['IncGroups_WB'].unique(), "All"))
fil_import_reg = np.sort(np.append(import_share['Regions_WB'].unique(), "All"))
import_share_wheat = import_share.sort_values('Wheat_TOT', ascending=True).reset_index(drop=True)
import_share_fert  = import_share.sort_values('Fertilizer', ascending=True).reset_index(drop=True)
#Bar Chart for Import Fraction
with st.expander("Import Dependance Details"):
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
    plt_import_wheat.caption("Source : UN Comtrade Database, https://comtrade.un.org/. Accessed on July 2022")
    plt_import_fert.caption("Source : UN Comtrade Database, https://comtrade.un.org/. Accessed on July 2022")
    st.caption('\* Missing data for wheat&fertilizers import \
               &ensp;\*\* Missing data for fertilizers import')
st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

#---------------SECTION 2 : Commodities Price Change --------------------------
st.header("B. Commodities Price Inflation")
#-------------------------------------------
# SECTION 2.1 : FAO Food Price Index
#-------------------------------------------

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

#-------------------------------------------
# SECTION 2.2 : WB Commodity Price
#-------------------------------------------
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
#---------------SECTION 3 : Export Restriction Profile--------------------------
st.header("C. Export Restriction Caused by The Crisis")
#-----------------------------------------------------
# SECTION 3.1 : Overall Import Calories affected by ER
#-----------------------------------------------------
body_311 = '<p style="font-family:Arial; color:Black; font-size: 16px;">'+\
    'Because of supply chain distruption caused by concurrent crisis, there\'s an <b>uptrend of food trade policy, especially export restriction and import liberalisation.</b> '+\
    'This is usually done to increase domestic stocks availability to relieve/prevent critical shortages of foodstuffs, thus keeping food security intact.</p>'
st.markdown(body_311, unsafe_allow_html=True)
st.markdown('<h4 style="font-family:Arial; background-color: beige">'+
            '&ensp;Imported Calories Affected by Export Restriction\
            </h4>', unsafe_allow_html=True)
# Importing Affected Calories Data
df = pd.read_excel("data/4_Export_Restriction.xlsx", sheet_name="Imported_cal")
df.iloc[:, 1:] = df.iloc[:, 1:]*100

col_311, col_312 = st.columns([6,4])
# Plotting Data
with col_311:
    fig_er_overall = fs.plot_er_overall(df)
    st.plotly_chart(fig_er_overall)
    st.caption('Data Source : IFPRI, [Blog link](https://www.ifpri.org/blog/mc12-how-make-wto-relevant-middle-food-price-crisis#:~:text=Since%20Russia%E2%80%99s%20invasion%20of%20Ukraine%20in%20February%2C%2023%20countries%20have%20imposed%20export%20restrictions%20affecting%20over%2016%25%20of%20global%20agricultural%20trade%20on%20a%20kilocalorie%20basis.)')
# Summary Description
with col_312:
    body_312 = '<p style="font-family:Arial; color:Black; font-size: 16px;">'+\
        'As shown on the left figure, <b>export restriction applied during food crisis tends to impact developing and least developed countries (LDCs) more</b>'+\
        ' since these restrictions tend to target trade of staple food products (grains, edible oils, etc.).'+\
        '<b>These policies also stretch not only for conventional trading but also humanitarian shipments</b>, which those countries greatly depend upon for their basic needs.</p>'
    body_313 = '<p style="font-family:Arial; color:Black; font-size: 16px;">'+\
        '<b>Looking at the values, calories impacted by Ukraine Crisis also not much differ from Food Price Crisis during 2008, '+\
        'which all of its value only slightly above the current crisis.</b></p>'    
    st.markdown(body_312, unsafe_allow_html=True); st.markdown(body_313, unsafe_allow_html=True)

#-------------------------------------------
# SECTION 3.2 : Export Restriction Profile
#-------------------------------------------
st.markdown('<h4 style="font-family:Arial; background-color: beige">'+
            '&ensp;Export Restriction Profiles\
            </h4>', unsafe_allow_html=True)
ER_gen, ER_com = st.tabs(["🌍 General Overview", "🍎 Frequently Regulated Commodities", ])
# Importing Data
country_cnt = pd.read_excel("data/4_Export_Restriction.xlsx", sheet_name="Frequency_Country") # Read 'Count by Countries' Data
er_by_type = country_cnt.groupby(['Episode', 'Category']).count()['Country_Label'].reset_index() # Preparing ER by Types Data
er_cty_unique = country_cnt.drop_duplicates(subset=['Episode', 'Country_Label']) # Preparing ER by Number of Countries in Regions Data
# Preparing Restricted Export Values by Region
USD_restricted = pd.read_excel("data/4_Export_Restriction.xlsx", sheet_name="USD_Restricted")
usd_res_df = USD_restricted.groupby(['Region', 'Episode'])['Restricted Export USD'].sum().reset_index()

with ER_gen:
    col_321, col_322 = st.columns(2)
with col_321:
    # Plot Number of ER by Type
    st.markdown('### Number of Export Restrictions Active during The Crisis')
    f_er_type = fs.plot_er_type(er_by_type) 
    st.plotly_chart(f_er_type)
    
    # Plot Number of ER by Region
    st.markdown('### Export Restrictions by Regions')
    frec_reg, expval_reg = st.tabs(["🌍 Number of Countries", "💵 Restricted Export Values"])
    with frec_reg:
        f_er_reg = fs.plot_er_reg(er_cty_unique) # Country Count
        st.plotly_chart(f_er_reg)
    with expval_reg:
        f_res_usd = fs.plot_res_usd(usd_res_df) # Export Value
        st.plotly_chart(f_res_usd)
    st.caption('Data Source : IFPRI Food Restriction Tracker, [Public Tableau link](https://public.tableau.com/app/profile/laborde6680/viz/ExportRestrictionsTracker/FoodExportRestrictionsTracker)\
        . Accessed on July 2022')
    
# Summary Description
with col_322:   
    st.markdown('<p style="font-family:Arial; color:Black; font-size: 18px;">'+'<br><br><br><b>Both crisis currently have similar number of ER policies active during it.</b> \
        However difference in its type composition can be seen where <b>2022 crisis contains higher fraction of export licensing policies</b> \
        whereas 2008 crisis has higher fraction of export tax policies', unsafe_allow_html=True)
    st.markdown('<br>'*10,unsafe_allow_html=True)
    st.markdown('<p style="font-family:Arial; color:Black; font-size: 18px;">'+'<b>In total 33 and 32 countries publish ER policies during 2022 and 2008 crisis respectively, \
        covering in total 62.2k and 41.9k Mio USD of export values.</b> \
        <br><br><b>2022 noticeably receives more countries from Europe & Central Asia and MENA regions while 2008 receives more from Latin America & Carribean and Sub-Saharan Africa.</b> \
        This can be seen as a nod from geopolitical areas in which the conflict took place, which is around the Black Sea.<br><br> \
        <b>Country distribution also somewhat describes export values restricted by the measures</b>, for example during 2022 crisis Europe & Central Asia restricts much higher export values compared to 2008, \
        and during 2008 Latin America & Caribbean proves the opposite.',
        unsafe_allow_html=True) 
    
# Importing ER by Commodity Categories Data
hs4_freq = pd.read_excel("data/4_Export_Restriction.xlsx", sheet_name="Frequency HS4")
    
with ER_com:
    st.markdown('#### Here is shown the frequency of key commodity categories being regulated by ER during The Crisis. Commodity categories are\
         grouped using 4-digits Harmonized System Codes (HS4).')
    col_323, col_324 = st.columns([7,5])
    # Plot Commodity Categories Freq.
    with col_323:
        f_er_hs4 = fs.plot_er_hs4(hs4_freq)
        st.plotly_chart(f_er_hs4)
        st.markdown('<p style="font-family:Arial; color:Black; font-size: 14px;">\
                Categories in the same shade belongs to the same <b>parent category that is in bold</b>.<br>\
                e.g. Rice is part of Cereals</p>', 
                unsafe_allow_html=True)
        st.caption('Data Source : IFPRI Food Restriction Tracker, [Public Tableau link](https://public.tableau.com/app/profile/laborde6680/viz/ExportRestrictionsTracker/FoodExportRestrictionsTracker)\
            . Accessed on July 2022')
    # Summary Description
    with col_324:
        st.markdown('<p style="font-family:Arial; color:Black; font-size: 18px;">'+'<br><br><br><b>Commodities categorized as cereals, edible oils&fats, and fruits&vegetables are most often regulated by ER during the 2022 crisis.</b><br></p>'+
            '<p style="font-family:Arial; color:Brown; font-size: 18px;"><b>Overall, 2008 crisis tends to has higher frequency on all of parent categories except fertilizers.</b><br></p>'+
            '<p style="font-family:Arial; color:Black; font-size: 18px;">Due 2022 & 2008 crisis having similar number of ER being implemented, this means <b>2008 crisis envelops wider spread of commodities being regulated, thus wider area of commodities highly affected by it.</b> \
            For example many more ER regulates processed food export.</p>', unsafe_allow_html=True)
        
st.markdown("""<hr style="height:4px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
#-------------------------------------------
# SECTION 4 : Conclusion
#-------------------------------------------
st.header("D. Conclusion")

st.markdown(p_format+'<b>Ukraine-Russia Conflict during 2022 has as much impacts as previous notable food price crisis like the 2007-2008 Food Crisis on global agrifood market</b>, \
    looking at it by the <b>record and near-record breaking price spike</b> created and how much it <b>increases major policy responses (in this case export restriction) from exporting countries.</b> \
    This can happens due to both countries are important players inside such environment, further complimented by the already volatile market currently.<br><br>\
    <b>There are several action that can be done in addressing food security impacts of the Ukraine crisis</b> :<br>\
    Lowering supply chain distruption by reducing ER intensity on food and fertilizers commodities. Giving supports such as Social Safety Net and other humanitarian efforts to vulnerable communities. \
    Food diversification to less fertilizer-intensive crops to reduce production cost. Reducing subsidy mandate for biofuel production to enforces the use of vegetable oils as calories instead.', 
    unsafe_allow_html=True)

# References
with st.expander("REFERENCES"):
    st.markdown(p_format+'[1] FAO. (2022). The FAO Food Price Index drops for the third consecutive month in June. <a href="https://www.fao.org/worldfoodsituation/foodpricesindex/en">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[2] GAPKI. (2021). Production Drops After Public Curb, CPO Sees Highest Price. <a href="https://gapki.id/en/news/20528/production-drops-after-public-curb-cpo-sees-highest-price">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[3] USDA. (2022). Brazil: Oilseeds and Products Update No. BR2022-0014. <a href="https://www.fas.usda.gov/data/brazil-oilseeds-and-products-update-29">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[4] The World Bank. (2022). The impact of the war in Ukraine on commodity markets. <a href="https://www.worldbank.org/en/research/commodity-markets">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True) 
    st.markdown(p_format+'[5] USDA. (2022). Impacts and Repercussions of Price Increases on the Global Fertilizer Market. <a href="https://www.fas.usda.gov/data/impacts-and-repercussions-price-increases-global-fertilizer-market">link</a>. Accessed on July 2022.', 
                unsafe_allow_html=True)         
st.markdown(p_format+"<b>Data last updated : 05 August 2022</b>", unsafe_allow_html=True)