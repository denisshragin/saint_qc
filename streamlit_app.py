import pandas as pd
import plotly.express as px
import streamlit as st

# Display title and text
st.title("Number of a 'Saint' municipalities in Quebec province")
st.markdown("Here we can see the 1st dataframe created during this project.")

# Read dataframe
dataframe = pd.read_csv(
    "saint_regions.csv",
    names=[
        "Region administrative",
        "Number of a 'Saint' municipalities",
        ],
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and the location we've chosen with a blue dot.")

# Create the plotly express figure
fig = px.choropleth_mapbox(df_saint, geojson='https://github.com/denisshragin/saint_qc/blob/main/quebec_regions.geojson',
                           color="Number of a 'Saint' municipalities",
                           locations="Region Administrative ",
                           featureidkey="properties.res_nm_reg",
                           color_continuous_scale="blues",
                           center={"lat": 48.0, "lon": -68.0},
                           mapbox_style="carto-positron", zoom=5)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the figure
st.plotly_chart(fig, use_container_width=True)
