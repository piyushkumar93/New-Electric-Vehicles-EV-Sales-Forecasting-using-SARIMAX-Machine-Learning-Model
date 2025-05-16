# 🔋 Electric Vehicle (EV) Sales Forecasting (2025–2028) using SARIMAX

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Pandas](https://img.shields.io/badge/Pandas-data--analysis-yellowgreen)
![SARIMAX](https://img.shields.io/badge/SARIMAX-Time%20Series%20Forecasting-orange)
![Status](https://img.shields.io/badge/Model-Tested-brightgreen)

Forecasting electric vehicle (EV) sales across **2-wheelers, 3-wheelers, 4-wheelers, and buses** in India using the **SARIMAX time series model**. This project uses real-world data to predict sales trends from **2025 to 2028**.

---

## 🚀 Features

- Used SARIMAX for modeling seasonality, trend, and external noise in EV sales
- Forecasts EV sales for 4 vehicle categories (2W, 3W, 4W, Buses)
- Tuned SARIMAX `(p,d,q)(P,D,Q,s)` hyperparameters manually
- Evaluated model performance using **MAE** and **MAPE**
- Visualized forecast trends with confidence intervals for 2025–2028

---

## 📊 Dataset Overview

- Sourced from public government and EV market reports
- Covers monthly EV sales from 2019 to 2024
- Categorized by:
  - 2-Wheelers (2W)
  - 3-Wheelers (3W)
  - 4-Wheelers (4W)
  - Buses

---

## 📈 Forecast Results

- **MAPE** (Mean Absolute Percentage Error):
  - 2W: ~7.6%
  - 3W: ~12.4%
  - 4W: ~15.9%
  - Buses: ~25.5%
- Forecasted results show continued growth, especially in 2W and 4W segments

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Statsmodels (SARIMAX)
- Excel (initial EDA)

---

## 🛠️ How to Run

1. Clone the repo:
```bash
git clone https://github.com/piyushkumar93/New-Electric-Vehicles-EV-Sales-Forecasting-using-SARIMAX-Machine-Learning-Model.git
cd New-Electric-Vehicles-EV-Sales-Forecasting-using-SARIMAX-Machine-Learning-Model
