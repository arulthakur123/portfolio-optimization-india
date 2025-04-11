import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
data = pd.read_csv("data.csv", header=[0, 1], index_col=0, parse_dates=True)
returns = pd.read_csv("returns.csv", index_col=0, parse_dates=True)

# Portfolio Optimization
mean_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252

# Number of assets
num_assets = len(mean_returns)

# Monte Carlo Simulation
num_portfolios = 10000
results = np.zeros((3 + num_assets, num_portfolios))
risk_free_rate = 0.06

for i in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std_dev

    results[0, i] = portfolio_return
    results[1, i] = portfolio_std_dev
    results[2, i] = sharpe_ratio
    results[3:, i] = weights

# Convert results array to DataFrame
columns = ['Return', 'Volatility', 'Sharpe'] + list(mean_returns.index)
results_df = pd.DataFrame(results.T, columns=columns)

# Find optimal portfolio
max_sharpe_port = results_df.loc[results_df['Sharpe'].idxmax()]

# Save optimal weights to CSV
optimal_weights = max_sharpe_port[3:]
optimal_weights.to_csv("optimal_weights.csv")

# Visualize efficient frontier
plt.figure(figsize=(12, 8))
plt.scatter(results_df.Volatility, results_df.Return, c=results_df.Sharpe, cmap='viridis', alpha=0.7)
plt.colorbar(label='Sharpe Ratio')
plt.scatter(max_sharpe_port[1], max_sharpe_port[0], c='red', s=100, label='Max Sharpe Ratio')
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier with Max Sharpe Ratio')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("efficient_frontier.png")
plt.show()

# Correlation matrix heatmap
corr_matrix = returns.corr()
plt.figure(figsize=(15, 12))
sns.heatmap(corr_matrix, cmap="coolwarm", center=0, xticklabels=False, yticklabels=False)
plt.title("Stock Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Print summary
print("\n✅ Insights Generated")
print("Expected Annual Return:", round(max_sharpe_port['Return'] * 100, 2), "%")
print("Annual Volatility:", round(max_sharpe_port['Volatility'] * 100, 2), "%")
print("Sharpe Ratio:", round(max_sharpe_port['Sharpe'], 2))
