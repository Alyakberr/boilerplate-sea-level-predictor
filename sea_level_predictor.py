import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
def draw_plot():
    # Read the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit (full dataset)
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_full = pd.Series(range(1880, 2051))
    y_pred_full = res_full.intercept + res_full.slope * x_pred_full
    plt.plot(x_pred_full, y_pred_full, 'r', label='Best fit line (1880–2050)')

    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'g', label='Best fit line (2000–2050)')

    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
