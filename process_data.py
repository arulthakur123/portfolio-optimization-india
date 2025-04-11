import pandas as pd

# Load the data
data = pd.read_csv('data.csv', index_col=0, parse_dates=True)

# Drop columns with any missing values
data.dropna(axis=1, inplace=True)

# Calculate daily returns
returns = data.pct_change().dropna()

# Save cleaned returns data
returns.to_csv('returns.csv')

print("✅ Daily returns calculated and saved to returns.csv")
