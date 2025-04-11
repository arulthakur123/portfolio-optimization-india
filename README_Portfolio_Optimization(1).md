
# 📊 Financial Risk & Portfolio Optimization (India)

This project focuses on constructing an optimized portfolio using **Modern Portfolio Theory (Markowitz)** for the **top 50 Indian stocks (NIFTY 50)**. It evaluates **expected return**, **risk (volatility)**, and the **Sharpe Ratio**, and uses **Monte Carlo simulations** to explore optimal allocations. All insights are generated using Python libraries like `NumPy`, `Pandas`, `Matplotlib`, and `yfinance`.

---

## 🔧 Tools & Libraries Used

- `Python 3.10+`
- `NumPy`, `Pandas`, `Matplotlib`
- `yfinance` – to fetch historical stock data
- `Seaborn` – for enhanced visuals (optional)

---

## 💼 Problem Statement

In the Indian stock market context, building a **well-diversified portfolio** is crucial to balancing **returns vs. risks**. This project attempts to:

- Use **daily adjusted closing prices** from **2020 to 2024**
- Simulate thousands of portfolios to find the one with the **maximum Sharpe Ratio**
- Analyze the **volatility, expected return**, and **risk-adjusted returns**
- Provide **data-driven insights** for long-term Indian investors

---


## 📁 Project Structure

```
portfolio_optimization/
│
├── env/                         # Virtual environment
├── data.csv                    # Historical price data for 50 NIFTY stocks
├── returns.csv                 # Calculated daily returns
├── fetch_data.py              # Script to download historical stock data
├── process_data.py            # Script to calculate daily returns
├── generate_insights.py       # Monte Carlo simulations + Portfolio Optimization
├── insights/                   # Plots and outputs generated
│   └── efficient_frontier.png
│
└── README.md                   # You're here!
```
## 📊 Visualizations
## Portfolio Allocation Chart

![Portfolio Allocation](portfolio_allocation.png)

### 1. Efficient Frontier with Max Sharpe Portfolio
![Efficient Frontier](images/efficient_frontier.png)

### 2. Portfolio Composition (Weights)
![Portfolio Weights](images/portfolio_composition.png)

### 3. Risk Contribution per Asset
![Risk Contribution](images/risk_contribution.png)

### 4. Return Contribution per Asset
![Return Contribution](images/return_contribution.png)

---

## 📈 Key Insights

- **Expected Annual Return:** ~26.19%
- **Annual Volatility:** ~18.51%
- **Sharpe Ratio:** ~1.09
- **Best Portfolio Allocation** (Top Assets):
  ```
  - TCS: 15.2%
  - HDFCBANK: 14.8%
  - INFY: 13.5%
  - RELIANCE: 11.3%
  ...
  ```

---

## 🔍 Bonus Insights (Optional)

You can enhance this project further by:
- Analyzing **sector-wise exposure** (e.g., IT, Finance, Pharma)
- Comparing with a **benchmark index (like NIFTY 50 ETF)**
- Running **stress tests** or simulating crashes
- Adding a **rebalancing strategy**

---

---

## 📌 Future Work

- Apply **machine learning** to predict future returns
- Use **CVaR or Value-at-Risk** for deeper risk evaluation
- Add **Power BI or Tableau** dashboard (optional)

---

## ✍️ Author

**Arul **  
Data Analyst & Python Enthusiast  
[GitHub](https://github.com/arulthakur123) •

