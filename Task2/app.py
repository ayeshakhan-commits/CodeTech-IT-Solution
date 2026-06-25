import streamlit as st
import pandas as pd
import plotly.express as px

# Page orientation set karna
st.set_page_config(page_title="Retail Store Analytics", layout="wide")

st.title("🛍️ Retail Store Sales & Customer Behavior Dashboard")
st.markdown("Interactive analytics dashboard built for Teyzix Core Internship Task 2.")

# Data load karne ka function
@st.cache_data
def load_data():
    df = pd.read_csv('Retail_Store_Sales_Dataset.csv')
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    return df

df = load_data()

# Sidebar controls
st.sidebar.header("Filter Options")
selected_city = st.sidebar.multiselect("Select City:", options=df['Customer City'].unique(), default=df['Customer City'].unique())
selected_category = st.sidebar.multiselect("Select Product Category:", options=df['Product Category'].unique(), default=df['Product Category'].unique())

# Filtering logic
filtered_df = df[(df['Customer City'].isin(selected_city)) & (df['Product Category'].isin(selected_category))]

# Major KPI Cards
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Revenue (PKR)", value=f"{filtered_df['Total Amount'].sum():,.2f}")
with col2:
    st.metric(label="Total Orders Placed", value=len(filtered_df))
with col3:
    st.metric(label="Average Order Value", value=f"{filtered_df['Total Amount'].mean():,.2f}")
with col4:
    st.metric(label="Total Items Sold", value=int(filtered_df['Quantity'].sum()))

st.markdown("---")

# Layout arrangement for plots
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("📦 Category Performance")
    cat_sales = filtered_df.groupby('Product Category')['Total Amount'].sum().reset_index()
    fig_cat = px.bar(cat_sales, x='Total Amount', y='Product Category', orientation='h', color='Product Category')
    st.plotly_chart(fig_cat, use_container_width=True)

with right_col:
    st.subheader("🏙️ Revenue By Location")
    city_sales = filtered_df.groupby('Customer City')['Total Amount'].sum().reset_index()
    fig_city = px.bar(city_sales, x='Customer City', y='Total Amount', color='Customer City')
    st.plotly_chart(fig_city, use_container_width=True)