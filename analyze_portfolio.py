import pandas as pd
import matplotlib.pyplot as plt

# Load optimal weights
portfolio = pd.read_csv('optimal_portfolio.csv')

# Filter out very small weights for clarity
portfolio = portfolio[portfolio['Weight'] > 0.01]

# Sort by weight
portfolio = portfolio.sort_values(by='Weight', ascending=False)

# Bar chart of allocations
plt.figure(figsize=(10, 6))
plt.bar(portfolio['Stock'], portfolio['Weight'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Optimal Portfolio Allocation (Top 50 Indian Stocks)')
plt.xlabel('Stock')
plt.ylabel('Weight')
plt.tight_layout()
plt.savefig('optimal_allocation.png')
plt.show()
