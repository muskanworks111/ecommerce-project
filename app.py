import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="E-Commerce Analytics", layout="wide")
st.title("🛒 E-Commerce Big Data Analytics Dashboard")

# Sample dataset
data = {
    "Category": ["Electronics", "Clothing", "Home", "Electronics", "Clothing"],
    "Sales": [12000, 5400, 8300, 15000, 6200],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar"],
}
df = pd.DataFrame(data)

st.subheader("Sales Overview by Category")
fig = px.bar(df, x="Month", y="Sales", color="Category", barmode="group")
st.plotly_chart(fig, use_container_width=True)