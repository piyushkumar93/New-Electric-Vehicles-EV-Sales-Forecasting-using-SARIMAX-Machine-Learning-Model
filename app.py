import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Page configuration
st.set_page_config(page_title="EV Sales Forecasting", layout="wide")

st.title("🔋 Electric Vehicle Sales Forecasting (2025–2028)")
st.markdown("Forecasting future sales for EVs (2W, 3W, 4W, and Buses) using SARIMAX on monthly data.")

# Load Excel with 'Month' column
@st.cache_data
def load_data():
    df = pd.read_excel("729d71a3-2516-4b3d-8713-2d9e0e3fb176.xlsx")
    df['Month'] = pd.to_datetime(df['Month'], format="%B %Y")
    df.set_index('Month', inplace=True)
    return df

df = load_data()

# Sidebar selections
vehicle_type = st.sidebar.selectbox("Select vehicle type", df.columns)
forecast_years = st.sidebar.slider("Forecast period (years)", min_value=1, max_value=5, value=4)

# Get selected series
data = df[vehicle_type]

# SARIMAX modeling
model = SARIMAX(data, order=(1,1,1), seasonal_order=(1,1,0,12))
model_fit = model.fit(disp=False)

# Forecasting
steps = forecast_years * 12
forecast = model_fit.get_forecast(steps=steps)
forecast_mean = forecast.predicted_mean
conf_int = forecast.conf_int()

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
data.plot(ax=ax, label='Actual Sales')
forecast_mean.plot(ax=ax, label='Forecast', color='orange')
ax.fill_between(conf_int.index,
                conf_int.iloc[:, 0],
                conf_int.iloc[:, 1], color='pink', alpha=0.3)
plt.title(f"{vehicle_type} Sales Forecast ({forecast_years} Years)")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("📈 Built by [Piyush Kumar](https://www.linkedin.com/in/piyush-kumar-146b661aa/)")
