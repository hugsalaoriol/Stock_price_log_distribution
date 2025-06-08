# This code aims to demosntrate the character of fat-tailed non-Gaussian shape of price diferences' distribution.
# Disclaimer: According to Efficient Market Hypothesis, price changes are unpredictable from the historical time series of those changes.

# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import random
import sklearn as sk
from sklearn.metrics import mean_squared_error
import scipy.stats as stats
from scipy.stats import cauchy
from scipy.stats import kurtosis
from scipy.stats import norm


# Setting the random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Downloading the data from Yahoo Finance
start_date = '2020-01-01'
end_date = '2025-01-01'
tickers = ['^GSPC', 'GC=F', 'CL=F', 'JPM'] # S&P 500 index, Gold futures, Crude Oil futures, and JPMorgan Chase & Co.

data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)['Close']
data_clean = data.dropna()  # Drop rows with NaN values
price_differences = data_clean.diff() # Calculate the price differences
price_differences = np.log(data_clean / data_clean.shift(1)) # Calculate the log returns

################################################################################################################################################################################################

#In order to demonstrate the character of fat-tailed non-Gaussian shape of price diferences' distribution, the following will be made:
# 1. Plot the price differences as a histogram with a kernel density estimate (KDE) overlay.

# 2. Plot a Q-Q plot to visualize the distribution of price differences. If the points follow a straight line, it indicates that the data is normally distributed. 
# Deviations from the line indicate departures from normality.

# 3. Compute the kurtosis of the price differences. A kurtosis value greater than 3 indicates a fat-tailed distribution, while a value less than 3 indicates a thin-tailed distribution.

#4. Plot a fat tailed Cauchy distribution 

################################################################################################################################################################################################

# 1. Plotting the price differences as a histogram with KDE overlay
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Flatten axes for easier iteration
axes = axes.flatten()

# Loop through the tickers and plot in each subplot
for i, ticker in enumerate(tickers):
    data = price_differences[ticker].dropna()

    # Plot histogram with KDE
    sns.histplot(data, bins=50, kde=True, stat="count", ax=axes[i], color='steelblue', alpha=0.6)

    # Fit a Gaussian (normal) distribution
    mu, std = norm.fit(data)

    # Create x values for the fitted curve
    x = np.linspace(data.min(), data.max(), 1000)
    y = norm.pdf(x, mu, std) * len(data) * (data.max() - data.min()) / 50  # Adjust for 'count' histogram
    
    # Plot the Gaussian fit
    axes[i].plot(x, y, color='green', linestyle='--', label='Fitted Gaussian')

    # Customize plot
    axes[i].set_title(f'{ticker}')
    axes[i].set_xlabel('Price Differences')
    axes[i].set_ylabel('Frequency')
    axes[i].grid(True)
    axes[i].legend()

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()


# 2. Plotting Q-Q plot to visualize the distribution of price differences
fig, axes = plt.subplots(2, 2, figsize=(15, 10)) # Create a figure with 2 rows and 2 columns (4 subplots)

# Flatten axes for easier iteration
axes = axes.flatten()

# Loop through the tickers and plot the Q-Q plot for each
for i, ticker in enumerate(tickers):
    if ticker not in price_differences.columns:
        print(f"Ticker '{ticker}' is missing from the data.")
        continue

    data = price_differences[ticker].dropna()
    (osm, osr), (slope, intercept, r) = stats.probplot(data, dist="norm")

    # Plot the Q-Q scatter
    axes[i].scatter(osm, osr, alpha=0.5, label='Data')

    # Add reference line
    x_line = np.linspace(min(osm), max(osm), 100)
    y_line = slope * x_line + intercept
    axes[i].plot(x_line, y_line, color='red', linestyle='--', label='Normal Q-Q Line')

    axes[i].set_title(f'{ticker}')
    axes[i].set_xlabel('Theoretical Quantiles')
    axes[i].set_ylabel('Sample Quantiles')
    axes[i].grid(True)
    axes[i].legend()

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()


# 3. Compute the kurtosis of the price differences
for ticker in tickers:
    if ticker in price_differences.columns:
        # Drop NaN values
        data = price_differences[ticker].dropna()
        
        # Calculate kurtosis
        kurt_value = kurtosis(data)
        
        # Print the result for each ticker
        print(f"Kurtosis for {ticker}: {kurt_value}")


# 4. Plot a fat-tailed Cauchy distribution
# Set up the number of subplots (based on the number of tickers)
fig, axes = plt.subplots(2, 2, figsize=(15, 10)) # Adjust the size as needed
axes = axes.flatten()  # Flatten the 2x2 axes to make iteration easier

# Loop through each ticker and plot the Cauchy distribution fit
for i, ticker in enumerate(tickers):
    if ticker in price_differences.columns:
        data = price_differences[ticker].dropna()

        # Fit a Cauchy distribution
        cauchy_params = cauchy.fit(data)
        
        # Fit a Gaussian (Normal) distribution
        norm_params = norm.fit(data)
        
        # Plot the histogram and KDE
        sns.histplot(data, kde=True, bins=50, stat='density', label='Data', ax=axes[i], color='steelblue', alpha=0.6)
        
        # Plot the fitted Cauchy distribution
        x = np.linspace(min(data), max(data), 1000)
        y_cauchy = cauchy.pdf(x, *cauchy_params)
        axes[i].plot(x, y_cauchy, color='red', linestyle='--', label='Fitted Cauchy')

        # Plot the fitted Gaussian distribution
        y_norm = norm.pdf(x, *norm_params)
        axes[i].plot(x, y_norm, color='green', linestyle=':', label='Fitted Gaussian')

        axes[i].set_title(f"{ticker}")
        axes[i].set_xlabel('Price Differences')
        axes[i].set_ylabel('Density')
        axes[i].grid(True)
        axes[i].legend()

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
