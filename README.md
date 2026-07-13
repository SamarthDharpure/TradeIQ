<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,100:22C55E&height=180&section=header&text=TradeIQ&fontSize=58&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Stock%20Market%20Predictor&descAlignY=58&descSize=18&descColor=DCFCE7" width="100%" alt="TradeIQ banner" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1500&color=22C55E&center=true&vCenter=true&width=650&lines=85%25%2B+Accuracy+on+S%26P500+Forecasts;100%2B+Stocks+%7C+Real-Time+Data+via+yFinance;Python+%C2%B7+TensorFlow+%C2%B7+Scikit-learn+%C2%B7+Streamlit" alt="Typing SVG" />

**A machine learning platform that forecasts stock trends and prices in real time, from raw ticker data to interactive predictions**

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

<br/>

[![GitHub Repo stars](https://img.shields.io/github/stars/SamarthDharpure/TradeIQ?style=flat-square&color=22C55E)](https://github.com/SamarthDharpure/TradeIQ/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/SamarthDharpure/TradeIQ?style=flat-square&color=22C55E)](https://github.com/SamarthDharpure/TradeIQ/network)
[![GitHub issues](https://img.shields.io/github/issues/SamarthDharpure/TradeIQ?style=flat-square&color=22C55E)](https://github.com/SamarthDharpure/TradeIQ/issues)
[![Last commit](https://img.shields.io/github/last-commit/SamarthDharpure/TradeIQ?style=flat-square&color=22C55E)](https://github.com/SamarthDharpure/TradeIQ/commits)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E.svg?style=flat-square)](#-license)

[Overview](#-overview) · [Features](#-features) · [Pipeline](#-pipeline) · [Tech Stack](#-tech-stack) · [Getting Started](#️-getting-started) · [Usage](#-usage) · [Screenshots](#-screenshots) · [Roadmap](#-roadmap)

</div>

<br/>

## 📖 Overview

**TradeIQ** is a machine learning–powered stock market prediction platform that turns raw historical price data into forward-looking forecasts. It combines a time-series model trained on S&P500 data with a real-time data feed from yFinance, wrapped in an interactive **Streamlit** app so a user can type a ticker and immediately see historical trends, live prices, and a predicted trajectory.

**Project timeline:** January 2025 – May 2025

<br/>

<div align="center">

|  🎯 Model Accuracy  |  🔮 Stocks Supported  |  ⚡ Training Speed  |  📈 Prediction Stability  |
|:---:|:---:|:---:|:---:|
|  **85%+**  |  **100+**  |  **+25% faster**  |  **+18% more stable**  |

</div>

<br/>

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 AI/ML Forecasting
Time-series model achieving 85%+ accuracy on historical S&P500 datasets.

### 🔮 Broad Coverage
Predicts trends for 100+ global stocks from a simple ticker input.

### ⚡ Real-Time Data
Live market data pulled directly from the yFinance API.

</td>
<td width="50%">

### 📊 Interactive Charts
Dynamic, explorable visualizations built with Matplotlib and Pandas.

### 🔍 Efficient Training
Feature engineering cut training time by 25%.

### 🖥️ Streamlit UI
Clean, fast interface for ticker lookup and prediction exploration.

</td>
</tr>
</table>

<br/>

## 🔄 Pipeline

```mermaid
flowchart LR
    A["User Input<br/>(Stock Ticker)"] --> B["yFinance API<br/>Live + Historical Data"]
    B --> C["Preprocessing<br/>Pandas · NumPy"]
    C --> D["Feature Engineering"]
    D --> E["ML Model<br/>TensorFlow · Scikit-learn"]
    E --> F["Prediction Output"]
    F --> G["Streamlit UI<br/>Charts · Matplotlib"]
    C --> G
```

**Flow:** a ticker entered in the UI triggers a live pull from yFinance, which is cleaned and feature-engineered before being fed into the trained model. Both the raw historical series and the model's forecast are rendered back into the Streamlit app as interactive charts.

<br/>

## 🧑‍💻 Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | [Python](https://www.python.org/) |
| **ML / Modeling** | [Scikit-learn](https://scikit-learn.org/) · [TensorFlow](https://www.tensorflow.org/) |
| **Data Handling** | [Pandas](https://pandas.pydata.org/) · [NumPy](https://numpy.org/) |
| **Data Source** | [yFinance API](https://pypi.org/project/yfinance/) |
| **Visualization** | [Matplotlib](https://matplotlib.org/) |
| **App / Frontend** | [Streamlit](https://streamlit.io/) |
| **Tooling** | [VS Code](https://code.visualstudio.com/) · Git |

</div>

<br/>

## 📂 Project Structure

```
TradeIQ/
├── app.py               # Main Streamlit app
├── model/                # ML models and training scripts
├── data/                 # Sample datasets
├── requirements.txt      # Dependencies
└── README.md
```

<br/>

## ⚙️ Getting Started

### Prerequisites
- Python 3.9+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/SamarthDharpure/TradeIQ.git
cd TradeIQ
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

<br/>

## 🚀 Usage

1. Launch the app and enter any **stock ticker** (e.g. `AAPL`, `TSLA`, `GOOGL`)
2. Pull **real-time financial data** via yFinance
3. Explore **dynamic charts** of historical stock trends
4. View **predicted future prices** generated by the ML model

<br/>

## 📸 Screenshots

<div align="center">

### Home Page
<img width="700" alt="Home Page" src="https://github.com/user-attachments/assets/b5819055-1951-410e-a005-4a70398ef611" />

### Stock Prediction
<img width="500" alt="Stock Prediction" src="https://github.com/user-attachments/assets/e451a1d1-6d4f-4a45-a0e3-dc8f66072b66" />

### Prediction Graphs

<img width="700" alt="Prediction Graph 1" src="https://github.com/user-attachments/assets/59b6e886-a72b-4344-92ab-629a367306de" />

<img width="700" alt="Prediction Graph 2" src="https://github.com/user-attachments/assets/4aaf67e5-0647-4100-ba72-a7f7fadac281" />

<img width="700" alt="Prediction Graph 3" src="https://github.com/user-attachments/assets/4ee6426e-8c5c-4e0a-ad24-c65da8fbeac5" />

<img width="700" alt="Prediction Graph 4" src="https://github.com/user-attachments/assets/e45eb5ff-7af4-4868-ae21-de7824ba2ad7" />

</div>

<br/>

## 🗺️ Roadmap

- [ ] Support for crypto and forex tickers
- [ ] Model comparison view (LSTM vs. traditional regressors)
- [ ] Portfolio-level forecasting across multiple tickers
- [ ] Downloadable prediction reports (PDF/CSV)
- [ ] Dockerized deployment

> Have an idea? [Open an issue](https://github.com/SamarthDharpure/TradeIQ/issues) — contributions and suggestions are welcome.

<br/>

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add: your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

<br/>

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

<br/>

## 🧑‍💻 Author

<div align="center">

**Samarth Dharpure**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samarth-dharpure-88a10b248/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SamarthDharpure)

</div>

<br/>

<div align="center">

### ⭐ If TradeIQ was useful to you, consider giving it a star — it helps a lot!

</div>
