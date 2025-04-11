import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load returns data
returns = pd.read_csv('returns.csv', index_col=0, parse_dates=True)

# Calculate mean returns and covariance matrix
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Number of portfolios to simulate
num_portfolios = 5000
risk_free_rate = 0.06  # You can tweak this based on Indian FD/Bond rate

results = np.zeros((3, num_portfolios))
weights_record = []

for i in range(num_portfolios):
    weights = np.random.random(len(mean_returns))
    weights /= np.sum(weights)
    weights_record.append(weights)
    
    portfolio_return = np.dot(weights, mean_returns) * 252  # Annualize returns
    portfolio_stddev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_stddev
    
    results[0, i] = portfolio_stddev
    results[1, i] = portfolio_return
    results[2, i] = sharpe_ratio

# Locate the portfolio with highest Sharpe ratio
max_sharpe_idx = np.argmax(results[2])
optimal_weights = weights_record[max_sharpe_idx]

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(results[0, :], results[1, :], c=results[2, :], cmap='viridis', marker='o', s=10, alpha=0.3)
plt.colorbar(label='Sharpe Ratio')
plt.scatter(results[0, max_sharpe_idx], results[1, max_sharpe_idx], color='red', marker='*', s=200, label='Max Sharpe Ratio')
plt.title('Efficient Frontier for Top 50 Indian Stocks')
plt.xlabel('Annualized Volatility (Std Dev)')
plt.ylabel('Annualized Return')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('efficient_frontier.png')
plt.show()

# Save optimal weights to CSV
optimal_weights_df = pd.DataFrame({'Stock': mean_returns.index, 'Weight': optimal_weights})
optimal_weights_df.to_csv('optimal_portfolio.csv', index=False)

print("✅ Optimization complete. Efficient frontier plotted and optimal weights saved.")
