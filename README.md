# 🔋 Electric Vehicle Sales Forecasting (2025–2028) using SARIMAX

![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Time%20Series%20Modeling-orange)
![Status](https://img.shields.io/badge/Deployed-Live-brightgreen)

This project forecasts monthly sales of electric vehicles (EVs) in India across four categories —  
**2-Wheelers, 3-Wheelers, 4-Wheelers, and Buses** — from 2025 to 2028 using the **SARIMAX time series model**.

The app is built and deployed with **Streamlit** for interactive exploration of forecast results.

---

## 🚀 Features

- Interactive dashboard to select vehicle category and forecast horizon (1 to 5 years)
- Visualizes historical monthly EV sales data
- Forecasts future sales with confidence intervals
- Built using SARIMAX to capture seasonality and trends
- Fast and responsive with user-friendly UI

---

## 📈 Usage

Visit the live app here:  
👉 [https://new-electric-vehicles-ev-sales-forecasting-using-sarimax.streamlit.app/](https://new-electric-vehicles-ev-sales-forecasting-using-sarimax.streamlit.app/)

Use the sidebar to:
- Choose a vehicle category (2W, 3W, 4W, Buses)
- Select the number of forecast years (1 to 5)

The plot updates dynamically with the forecasted sales and confidence intervals.

---

## 🧰 Tech Stack

- Python 3.9+  
- Streamlit (Dashboard UI)  
- Pandas, NumPy (Data handling)  
- Matplotlib (Plotting)  
- Statsmodels (SARIMAX modeling)  
- OpenPyXL (Excel file reading)

---

## 📂 Project Structure

├── app.py # Streamlit dashboard app
├── ev_sales_data.xlsx # Monthly EV sales data (Month, 2W, 3W, 4W, Buses)
├── requirements.txt # Dependencies for running app
├── README.md # Project documentation

## 🛠️ How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/piyushkumar93/New-Electric-Vehicles-EV-Sales-Forecasting-using-SARIMAX-Machine-Learning-Model.git
cd New-Electric-Vehicles-EV-Sales-Forecasting-using-SARIMAX-Machine-Learning-Model
Install dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
```


📊 Sample Output

(Add your forecast graph screenshot here)

🙋‍♂️ Author
Piyush Kumar
B.Tech Instrumentation & Control Engineering — NSUT (2023–2027)
📧 piyushkumar-ug23@nsut.ac.in
🔗 LinkedIn | GitHub


