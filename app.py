# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Page setup
st.set_page_config(page_title="EV Sales Forecasting", layout="wide")

st.title("🔋 Electric Vehicle Sales Forecasting (2025–2028)")
st.markdown("Forecasting EV sales for 2W, 3W, 4W, and Buses using SARIMAX time series models.")

# Load your data
@st.cache_data
def load_data():
    df = pd.read_csv("ev_sales_data.csv", parse_dates=['Date'], index_col='Date')
    return df

df = load_data()

# Sidebar
vehicle_type = st.sidebar.selectbox("Choose vehicle type", df.columns)
years = st.sidebar.slider("Select forecast period (years)", 1, 5, 4)

# Subset data
data = df[vehicle_type]

# Fit SARIMAX model
model = SARIMAX(data, order=(1,1,1), seasonal_order=(1,1,0,12))
model_fit = model.fit(disp=False)

# Forecasting
forecast_steps = years * 12
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_mean = forecast.predicted_mean
conf_int = forecast.conf_int()

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))
data.plot(label='Actual Sales', ax=ax)
forecast_mean.plot(label='Forecast', ax=ax)
ax.fill_between(conf_int.index,
                conf_int.iloc[:, 0],
                conf_int.iloc[:, 1], color='pink', alpha=0.3)
plt.title(f"{vehicle_type} Forecast for Next {years} Year(s)")
plt.xlabel("Date")
plt.ylabel("Monthly Sales")
plt.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("📈 Built by [Piyush Kumar](https://www.linkedin.com/in/piyush-kumar-146b661aa/) | NSUT | SARIMAX Forecasting | Streamlit")
