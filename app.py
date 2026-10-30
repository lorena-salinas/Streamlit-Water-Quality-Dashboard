# To run, type in the terminal:  streamlit run app.py

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Water Quality Dashboard", layout="wide")

st.title("Water Quality Dashboard")
st.header("CIS 3590 - Internship Ready Software Development")
st.subheader("Lorena Salinas")

st.success("Welcome to my first data-driven app!")

st.divider()


st.sidebar.header("File Upload")
st.sidebar.info("Upload a CSV file with water quality data, or use the default Biscayne Bay file.")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# if the user doesn't upload use the default file in the project folder
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("File uploaded")
else:
    df = pd.read_csv("biscayneBay_waterquality.csv")


# To create tabs
overview, tables, plots , maps = st.tabs(["Overview", "Data", "Charts", "Maps"])

with overview:
    st.subheader("Overview")
    st.markdown(
        "This app explores water-quality readings from **Biscayne Bay, Miami**. "
        "Each row is one reading with a time, GPS position, and measurements such as "
        "temperature, salinity and depth. Use the sidebar to upload your own CSV, "
        "then explore the tabs above."
    )

# Adds content to tables tab
with tables:
    st.subheader("Raw Data")
    st.dataframe(df, width="stretch")

    # Let the user choose which columns to show (all columns are selected to start)
    selected_columns = st.multiselect(
        "Select columns to display",
        options=df.columns.tolist(),
        default=df.columns.tolist(),
    )
    st.subheader("Descriptive Statistics")
    if selected_columns:
        st.dataframe(df[selected_columns].describe(), width="stretch")
    else:
        st.info("Select at least one column to display the data.")


# Adds content to the charts tab
with plots:
    st.subheader("Parameters Over Time")
    st.markdown("Pick a measurement to see how it changed over time.")
    # Add all possible parameters to list of parameters in the selectbox and dynamically change the y axis in the plot to the selected parameter
    parameter = st.selectbox("Select a parameter", df.columns.tolist())
    fig1 = px.line(
        df, x="Time", y=parameter,
        title=f"{parameter} Over Time"
    )
    st.plotly_chart(fig1, width="stretch")

    st.subheader("Temperature vs Salinity")
    fig2 = px.scatter(
        df, x="Temperature (c)", y="Salinity (ppt)",
        color="Total Water Column (m)",
        title="Temperature vs Salinity (Colored by Depth)"
    )
    st.plotly_chart(fig2, width="stretch")

    st.subheader("3D View of the Bay Floor")
    st.markdown("Position on the horizontal axes, water depth on the vertical axis. Drag to rotate.")
    fig3 = px.scatter_3d(
        df, x="Longitude", y="Latitude",
        z="Total Water Column (m)",
        title="3D Visualization of the Bay Floor",
        color= "Temperature (c)"
    )
    fig3.update_scenes(zaxis_autorange="reversed")
    fig3.update_traces(marker_size=3)
    st.plotly_chart(fig3, width="stretch")

# Adds content to the maps tab
with maps:
    st.subheader("Map")
    first_map = px.scatter_map(
        df, lat= "Latitude", lon="Longitude",
        title="Vehicle Track on a Map",
        center={"lat":25.9121, "lon":-80.1371},
        zoom=16, color= "Temperature (c)",
        color_continuous_scale="Viridis")
    st.plotly_chart(first_map, width="stretch")