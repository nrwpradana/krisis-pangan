import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

def plot_import(slice_food, slice_fert):
    slice_food = slice_food.rename(columns={"Wheat_UKR":"Ukraine", "Wheat_RUS":"Russia"})
    h = 20*slice_food.shape[0]
    fig_food = px.bar(slice_food, y="Country", x=["Ukraine", "Russia"], custom_data= ["Wheat_TOT"], orientation='h', 
              range_x=[0,100], width=650, height=max(h, 650),
              color_discrete_sequence=['rgba(146, 114, 24, 1)', 'rgba(234, 241, 60, 1)'],
              template="simple_white", category_orders=slice_food['Country'])
    
    fig_food.update_layout(legend=dict(y=0.5, xanchor="right", title="Import Source"), title_text="<b>Import Fraction of Wheat from Ukraine & Russia, 2018-2020</b>")
    fig_food.update_traces(hovertemplate='<b>%{y}</b><br> Import Fraction: %{x:.2f} %<br> Total : %{customdata:.2f} %')
    fig_food.update_xaxes(title="<b>Import Fraction (%)</b>", showgrid=True, linewidth=2, gridcolor='black')
    fig_food.update_yaxes(title=None)
    
    fig_fert = px.bar(slice_fert, y="Country", x="Fertilizer", orientation='h', 
                range_x=[0,100], width=650, height=max(h, 650),
                color_discrete_sequence=['rgba(18, 16, 199, 1)'],
                template="simple_white", category_orders=slice_fert['Country'])
    
    fig_fert.update_layout(title_text="<b>Import Fraction of Fertilizers from Russia, 2018-2020</b>")
    fig_fert.update_traces(hovertemplate='<b>%{y}</b> <br> Import Fraction: %{x:.2f} %')
    fig_fert.update_xaxes(title="<b>Import Fraction (%)</b>", showgrid=True, linewidth=2, gridcolor='black')
    fig_fert.update_yaxes(title=None)
    
    return fig_food, fig_fert

def plot_fao_idx(df, title):
    col_map_fppi = {'Food Price Index':'skyblue','Meat':'red','Dairy':'gray','Cereals':'orange','Vegetable Oils':'black','Sugar':'green'}
    fig_idx_inf = px.line(df, x='Date', y=df.columns[:-1], range_y=[50, 250],
                    color_discrete_map=col_map_fppi)
    fig_idx_inf.update_layout(
        title_text="<b>"+title+"</b>",
        xaxis = dict(tickformat='%b %Y', hoverformat='<b>%b %Y</b>'),
        yaxis = dict(title='<b>Index</b>',title_font=dict(size=18), tickfont=dict(family='Helvetica', size=14, color='black')),
        template='simple_white',
        width=600, height=600,
        margin=dict(l=50, r=50, b=10, t=100, pad=0),
        legend=dict(font=dict(size=14), title=None, yanchor="bottom", y=0.65, xanchor="right", x=0.4, bgcolor='rgba(0,0,0,0)'),
        hovermode="x unified", hoverlabel=dict(bgcolor='rgba(255,255,255,0.5)', font_size=11)
    )
    fig_idx_inf.for_each_trace(lambda t: t.update(name = '<b>' + t.name +'</b>'))
    fig_idx_inf.update_xaxes(title=None, showgrid=True, tickfont=dict(size=14), title_font=dict(size=16))
    fig_idx_inf.update_traces(hovertemplate='<b>%{y:.2f}</b>', line=dict(width=3))
    return fig_idx_inf

def plot_wb_cp(df, title, cat):
    col_map_wb = {'Palm oil':'red', 'Soybean oil':'olivedrab','Rapeseed oil':'gold','Sunflower oil':'chocolate',
                  'Soybeans':'olivedrab', 'Maize':'orange', 'Rice':'slategrey', 'Wheat (US)':'peru',
                  'Phosphate rock':'navy', 'DAP':'gray', 'TSP':'black', 'Urea':'green', 'Potassium chloride':'gold'}
    if cat == 'Edible Oils': slice_cat = df.iloc[:,:5]; yrange = [500, 2500]
    elif cat == 'Grains': slice_cat = df.iloc[:,5:9]; slice_cat['Date'] = df['Date']; yrange = [100, 850]
    else: slice_cat = df.iloc[:,10:]; slice_cat['Date'] = df['Date']; yrange = [50, 1150]
    
    fig_cp = px.line(slice_cat, x='Date', y=slice_cat.columns, range_y=yrange,
                    color_discrete_map=col_map_wb)
    fig_cp.update_layout(
        title_text="<b>"+title+"</b>",
        xaxis = dict(tickformat='%b %Y', hoverformat='<b>%b %Y</b>'),
        yaxis = dict(title='<b>Nominal Price ($/mt)</b>',title_font=dict(size=18), tickfont=dict(family='Helvetica', size=14, color='black')),
        template='simple_white',
        width=600, height=600,
        margin=dict(l=50, r=50, b=10, t=100, pad=0),
        legend=dict(font=dict(size=14), title=None, yanchor="bottom", y=0.65, xanchor="right", x=0.4, bgcolor='rgba(0,0,0,0)'),
        hovermode="x unified", hoverlabel=dict(bgcolor='rgba(255,255,255,0.5)', font_size=14, font_family='Arial')
    )
    fig_cp.for_each_trace(lambda t: t.update(name = '<b>' + t.name +'</b>'))
    fig_cp.update_xaxes(title=None, showgrid=True, tickfont=dict(size=14), title_font=dict(size=16))
    fig_cp.update_traces(hovertemplate='<b>%{y:.2f}</b>', line=dict(width=3))
    return fig_cp

def plot_idx_inf(df, cat, title):
    slice_08, slice_22 = cat+' (2008)', cat+' (2022)'
    y_08, y_22 = df[slice_08], df[slice_22]
    diff = abs((y_08 - y_22)/y_08*100)
    
    fig_inf = go.Figure()
    fig_inf.add_trace(go.Scatter(
            x=df['Month'],
            y=y_08,
            hovertemplate="<b>%{y:.1f}%</b>", line=dict(color='orange'),
            name=slice_08
    ))
    fig_inf.add_trace(go.Scatter(
            x=df['Month'],
            y=y_22,
            hovertemplate="<b>%{y:.1f}%</b><br> <b>diff : %{customdata:.1f}%</b>",
            customdata=diff, line=dict(color='blue'),
            name=slice_22
    ))
    fig_inf.update_layout(
        title_text="<b>"+title+"</b>", title_font=dict(size=20),
        xaxis = dict(hoverformat="<b>%s</b>"),
        yaxis = dict(title='<b>Inflation Rate (%)</b>',title_font=dict(size=18), tickfont=dict(family='Helvetica', size=14, color='black')),
        template='simple_white',
        width=700, height=400,
        margin=dict(l=50, r=50, b=10, t=100, pad=0),
        legend=dict(font=dict(size=14), title=None, yanchor="bottom", y=0.65, xanchor="right", x=1, bgcolor='rgba(0,0,0,0)'),
        hovermode="x unified", hoverlabel=dict(bgcolor='rgba(255,255,255,0.7)', font_size=14)
    )
    fig_inf.update_xaxes(title=None, showgrid=True, tickfont=dict(size=14), title_font=dict(size=16))
    fig_inf.update_traces(line=dict(width=3))   
    return fig_inf

def plot_wb_idx_inf(df):
    df = df.rename(columns={"Food_48m_inflation":"Food Index", "Fertilizer_48m_inflation":"Fertilizers"})
    fig_idx_inf = px.line(df, x='Date', y=df.columns, range_y=[-100, 350],
                    color_discrete_sequence=['orange', 'mediumblue'])
    fig_idx_inf.update_layout(
        title_text="<b>World Bank Commodity Price Index Inflation (2000-2022)</b>", title_font=dict(size=20),
        xaxis = dict(tickformat='%b %Y', hoverformat='<b>%b %Y</b>'),
        yaxis = dict(title='<b>Index Inflation (%)</b>',title_font=dict(size=18), tickfont=dict(family='Helvetica', size=14, color='black')),
        template='simple_white',
        width=800, height=500,
        margin=dict(l=50, r=50, b=10, t=100, pad=0),
        legend=dict(font=dict(size=14), title=None, yanchor="bottom", y=0.8, x=0.8, bgcolor='rgba(0,0,0,0)'),
        hovermode="x unified", hoverlabel=dict(bgcolor='rgba(255,255,255,0.5)', font_size=14)
    )
    fig_idx_inf.add_vrect(
    x0="2007-01-01", x1="2008-12-01", fillcolor="coral", opacity=0.5,
    layer="below", line_width=0)
    fig_idx_inf.add_vrect(
    x0="2022-01-01", x1="2022-06-01", fillcolor="darkturquoise", opacity=0.5,
    layer="below", line_width=0)
    
    fig_idx_inf.for_each_trace(lambda t: t.update(name = '<b>' + t.name +'</b>'))
    fig_idx_inf.update_xaxes(title=None, showgrid=True, tickfont=dict(size=14), title_font=dict(size=16))
    fig_idx_inf.update_traces(hovertemplate='<b>%{y:.2f}%</b>', line=dict(width=3))
    return fig_idx_inf

def plot_er_overall(df):
    fig_31 = go.Figure()
    fig_31.add_trace(go.Bar(x=df['Food Price Crisis (2008)'], y=df['Economic Group'], orientation='h', name='Food Price Crisis (2008)',
                        marker_color='rgb(255,172,0)'))
    fig_31.add_trace(go.Bar(x=df['Covid-19 (2020)'], y=df['Economic Group'], orientation='h', name='Covid-19 (2020)',
                        marker_color='rgb(160,222,175)'))
    fig_31.add_trace(go.Bar(x=df['Ukraine Crisis (2022)'], y=df['Economic Group'], orientation='h', name='Ukraine Crisis (2022)',
                        marker_color='rgb(36,34,209)'))
    fig_31.update_layout(
        yaxis = dict(tickfont=dict(family='Helvetica', size=16, color='black')),
        template='simple_white',
        autosize=False,
        width=800, height=300,
        margin=dict(l=50, r=50, b=10, t=10, pad=0),
        paper_bgcolor="White", hovermode="y unified",
        legend=dict(y=0, xanchor="right", font=dict(size=14), bgcolor='rgba(0,0,0,0)'),    
    )
    fig_31.update_xaxes(title="<b>Share of imported calories (%)</b>", range=[0, 50], showgrid=True, tickfont=dict(size=14), title_font=dict(size=16))
    fig_31.update_traces(hovertemplate=' <b>%{x:.2f} %</b>')
    return fig_31

def plot_er_type(df):
    type_sum = df.groupby(['Episode']).sum()['Country_Label']
    fig_type = px.bar(df, x="Episode", y='Country_Label', color="Category", width=700, height=350,
                color_discrete_sequence=['red', 'skyblue', 'limegreen'],range_y=[0,50],
                template="simple_white")

    fig_type.update_layout(
        title_text="<b>Number of ER Policies by Types</b>", title_font=dict(size=20),
        yaxis = dict(title='<b>Number of Policies</b>',title_font=dict(size=18), tickfont=dict(family='Helvetica', size=16, color='black')),
        template='simple_white',
        margin=dict(l=50, r=80, b=10, t=100, pad=0),
        legend=dict(font=dict(size=14), title=None, yanchor="bottom", y=1, xanchor="right", x=1, bgcolor='rgba(0,0,0,0)', orientation='h'),
        hovermode="x unified", hoverlabel=dict(bgcolor='rgba(255,255,255,0.9)', font_size=14)
    )
    fig_type.data[-1].text = type_sum
    fig_type.update_traces(hovertemplate='<b>%{y}</b>', textfont_size=16, textangle=0, textposition="outside", width=0.5)
    fig_type.update_xaxes(title=None, tickfont=dict(size=16), linewidth=2, gridcolor='black')
    return fig_type

def plot_er_reg(df_cty_unique):
    # Preparing plot data
    count_reg = pd.DataFrame(df_cty_unique.value_counts(['Region', 'Episode']), columns=['Count']).reset_index().sort_values('Region')
    ct_ukr = count_reg[count_reg['Episode'] == 'UkraineCrisis (2022)']
    ct_08 = count_reg[count_reg['Episode'] == 'FoodPriceCrisis (2008)']
    # Preparing custom value
    ukr_list = []; c08_list = []; brk = '<br>'
    slice_ukr = df_cty_unique[df_cty_unique['Episode'] == 'UkraineCrisis (2022)']
    slice_08 = df_cty_unique[df_cty_unique['Episode'] == 'FoodPriceCrisis (2008)']
    for reg in count_reg['Region'].unique():
        cty_ukr_list = list(slice_ukr[slice_ukr['Region'] == reg]['Country_Label'])
        cty_ukr_hover = ["{}{}".format(brk,i) for i in cty_ukr_list]
        ukr_list.append(cty_ukr_hover)
        
        cty_08_list = list(slice_08[slice_08['Region'] == reg]['Country_Label'])
        cty_08_hover = ["{}{}".format(brk,i) for i in cty_08_list]
        c08_list.append(cty_08_hover)   
    
    #Plotting figure
    fig_reg = go.Figure()
    fig_reg.add_trace(go.Bar(x=ct_08['Region'], y=ct_08['Count'], customdata=c08_list, name='<b>Food Price Crisis (2008)</b>',
                        marker_color='rgb(255,172,0)',
                        text=ct_08['Count'], textfont_size=16))
    fig_reg.add_trace(go.Bar(x=ct_ukr['Region'], y=ct_ukr['Count'], customdata=ukr_list, name='<b>Ukraine Crisis (2022)</b>',
                        marker_color='rgb(36,34,209)', 
                        text=ct_ukr['Count'], textfont_size=16))
    fig_reg.update_layout(
        title_text="<b>Number of Countries Issuing ER by Regions</b>", title_font=dict(size=20),
        yaxis = dict(title='<b>Number of Countries</b>', title_font=dict(size=18), tickfont=dict(family='Helvetica', size=16, color='black'), range=[0,15]),
        template='simple_white', width=700, height=500,
        margin=dict(t=60, r=80, pad=0),
        paper_bgcolor="White",
        legend=dict(y=0.9, xanchor="right", font=dict(size=14), bgcolor='rgba(0,0,0,0)'),
        hovermode="x unified", hoverlabel=dict(bgcolor="white", font_size=16, font_family="Arial")
    )
    fig_reg.update_xaxes(title=None, showgrid=False, tickfont=dict(size=16))
    fig_reg.update_traces(hovertemplate='%{customdata}<extra></extra>', textposition="outside")
    return fig_reg
def plot_res_usd(df):
    usd_22 = df[df['Episode'] == 'UkraineCrisis (2022)']
    usd_08 = df[df['Episode'] == 'FoodPriceCrisis (2008)']

    fig_usd = go.Figure()
    fig_usd.add_trace(go.Bar(x=usd_08['Region'], y=usd_08['Restricted Export USD'], name='<b>Food Price Crisis (2008)</b>',
                        marker_color='rgb(255,172,0)'))
    fig_usd.add_trace(go.Bar(x=usd_22['Region'], y=usd_22['Restricted Export USD'], name='<b>Ukraine Crisis (2022)</b>',
                        marker_color='rgb(36,34,209)'))

    fig_usd.update_layout(
        title_text='<b>Export Values Affected by Restrictions</b>', title_font=dict(size=20),
        yaxis = dict(title='<b>Restricted Export (mio USD)</b>', title_font=dict(size=18), tickfont=dict(family='Helvetica', size=16, color='black')),
        template='simple_white', #autosize=False,
        width=700, height=500, margin=dict(t=60, r=80, pad=0), paper_bgcolor="White",
        legend=dict(y=0.9, xanchor="right", font=dict(size=14), bgcolor='rgba(0,0,0,0)'),
        hovermode="x unified", hoverlabel=dict(bgcolor="white", font_size=16, font_family="Arial")
    )
    fig_usd.update_xaxes(title=None, showgrid=False, tickfont=dict(size=16))
    fig_usd.update_traces(hovertemplate='%{y:.2f}')
    return fig_usd

def add_rect_paper(fig, x0, x1, color):
    fig.add_shape(type="rect",
        xref="paper", yref="paper",
        x0=x0, x1=x1, y0=0, y1=1,
        line_width=0, fillcolor=color, layer='below'
    )
def plot_er_hs4(df):
    fig_er_hs4= px.bar(df, x='Categories', y='Frequency',color='Episode', range_y=[0,150], 
                        barmode='group', color_discrete_sequence=['mediumblue', 'orange'])
    fig_er_hs4.update_layout(
        title_text="<b>Frequency of Commodity Categories Regulated by ER during The Crisis</b>", title_font=dict(size=20),
        xaxis = dict(tickformat='%b %Y', hoverformat='<b>%b %Y</b>'),
        yaxis = dict(title='<b>Frequency</b>',title_font=dict(size=18), tickfont=dict(family='Helvetica', size=14, color='black')),
        template='simple_white',
        width=800, height=600,
        margin=dict(l=50, r=50, b=10, t=100, pad=0),
        legend=dict(font=dict(size=14), title=None, yanchor="bottom", y=1, xanchor="right", x=1, bgcolor='rgba(0,0,0,0)', orientation='h'),
        hovermode="x unified", hoverlabel=dict(bgcolor='rgba(255,255,255,0.75)', font_size=14)
    )
    fig_er_hs4.for_each_trace(lambda t: t.update(name = '<b>' + t.name +'</b>'))
    fig_er_hs4.update_xaxes(title=None, tickfont=dict(size=14), tickangle=90) #, xaxis={'categoryorder':'array', 'categoryarray':['d','a','c','b']})
    fig_er_hs4.update_traces(hovertemplate='<b>%{y:.d}</b>')

    add_rect_paper(fig_er_hs4, 0,0.06,'red');add_rect_paper(fig_er_hs4, 0.06,0.12,'greenyellow')
    add_rect_paper(fig_er_hs4, 0.12,0.35,'gold');add_rect_paper(fig_er_hs4, 0.35,0.42,'gray')
    add_rect_paper(fig_er_hs4, 0.42,0.70,'olive');add_rect_paper(fig_er_hs4, 0.70,0.94,'steelblue')
    add_rect_paper(fig_er_hs4, 0.94,1,'fuchsia')
    return fig_er_hs4