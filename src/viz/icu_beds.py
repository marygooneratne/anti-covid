import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas_profiling as pp
import plotly.figure_factory as ff
import altair as alt
import os
import requests
import plotly.figure_factory as ff

def clean_data():
    df = pd.read_csv('data/data-FPBfz.csv')

    df = df.rename(columns = {"ICU Beds":"ICU_Beds","Total Population":"Total_Population","Population Aged 60+":"Population_Aged_60+","Percent of Population Aged 60+":"Percent_Population_Aged_60","Residents Aged 60+ Per Each ICU Bed":"Residents_Per_ICU_Bed"})
    fip_codes_df = pd.read_csv('data/county_fips.csv', encoding = "ISO-8859-1")
    fip_codes_df['county_name'] = fip_codes_df['county_name'].apply(lambda x: x.replace(' County', ''))
    fip_codes = fip_codes_df.set_index('county_name')['fips'].to_dict()
    df['county_fips_code'] = df['County'].apply(lambda x: fip_codes.get(x))
    df_county = df[pd.notnull(df['county_fips_code'])]
    fips = df_county['county_fips_code'].tolist()
    values = df_county['ICU_Beds'].tolist()
    return df

def mat_plot(df):
    plt.figure(figsize=(20,20))
    by_state = df.groupby('State')[['ICU_Beds']].sum()
    ax = sns.barplot(x = "ICU_Beds", y ='State', data = by_state.reset_index().sort_values(by=['ICU_Beds'], ascending = False))
    plt.show()
def altair_nobeds(df):
    countWithNoICUBeds = df.query("ICU_Beds==0")
    alt.Chart(countWithNoICUBeds).mark_circle(size=50).encode(
        x='Total_Population',
        y='Population_Aged_60+',
        color='State',
        tooltip=['State', 'County','Percent_Population_Aged_60','Population_Aged_60+','Total_Population']
    ).interactive()

def altair_beds(df):
    countiesWithICUBeds = df.query("ICU_Beds>0")
    alt.Chart(countiesWithICUBeds).mark_circle(size=50).encode(
        x='Total_Population',
        y='Population_Aged_60+',
        color='State',
        tooltip=['State', 'County','Percent_Population_Aged_60','Population_Aged_60+','Total_Population']
    ).interactive()

def plotly_chart(df):
    df_county = df[pd.notnull(df['county_fips_code'])]
    fips = df_county['county_fips_code'].tolist()
    values = df_county['ICU_Beds'].tolist()
    colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
             "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
             "#08519c","#0b4083","#08306b"]
    endpts = list(np.linspace(1, 12, len(colorscale) - 1))
    fips = df_county['county_fips_code'].tolist()
    values = df_county['ICU_Beds'].tolist()


    fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='ICU Beds per County',
    legend_title='Residents Aged 60+ Per Each ICU Bed'
    )

    fig.layout.template = None
    fig.show()

if __name__ == "__main__":
    print('here')
    df = clean_data()
    mat_plot(df)
    # plotly_chart(df)
