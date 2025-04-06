"""
Script for generating line plots, histograms, and box plots to visualise usage data.
"""

import matplotlib.pyplot as plt  # Required for plotting, but might have version issues
from matplotlib.dates import DateFormatter
import seaborn as sns

def plot_time_series(df, ax, metric, rolling_metric, title, ylabel, color, rolling_color):
    """
    Plot a time series with a rolling average and anomalies (if applicable).
    
    Parameters:
    df: Dataframe containing metrics
    ax: Matplotlib axis
    metric: Column name of raw metric
    rolling_col: Column name fo rolling average
    title: Plots title
    ylabel: Y-axis name
    color: Line color for raw data
    rolling_color: Line color for rolling average
    """
    ax.plot(df.index, df[metric], label=f'{metric} Usage', color=color)
    ax.plot(df.index, df[rolling_metric], label=f'{metric} Rolling Avg', color=rolling_color)
    if metric == 'CPU':
        ax.fill_between(df.index, 0, 100, where=df['CPU_Anomaly'], color='red', alpha=0.3, label='Anomaly (CPU > 90%)')
    ax.set_title(title)  
    ax.set_ylabel(ylabel)
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
    ax.legend(loc='upper right')  
    ax.grid(True)  

def plot_histograms(df, ax, metric1, metric2, color1, color2):
    """Plot histograms for two metrics."""
    ax.hist(df[metric1], bins=20, color=color1, alpha=0.7, label=f'{metric1} Usage')
    ax.hist(df[metric2], bins=20, color=color2, alpha=0.7, label=f'{metric2} Usage')
    ax.set_title(f'Histogram of {metric1} and {metric2} Usage')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend()

def plot_boxplot(df, ax):
    """Plot a box plot for the system metrics."""
    sns.boxplot(data=df[['CPU', 'Memory', 'Temperature', 'Power']], ax=ax)
    ax.set_title('Box Plot of System Metrics')
    ax.set_ylabel('Value')

def generate_plots(df, output_dir='results'):
    """Generate and save all required plots."""
    
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(18, 14)) 
    fig.suptitle('System Resource Usage Analysis')

    # Time series plots
    plot_time_series(df, axes[0, 0], 'CPU', 'CPU_Rolling', 'CPU Usage with Rolling Average and Anomalies', 'CPU (%)', 'blue', 'cyan')
    plot_time_series(df, axes[0, 1], 'Memory', 'Memory_Rolling', 'Memory Usage with Rolling Average', 'Memory (MB)', 'green', 'lightgreen')
    plot_time_series(df, axes[1, 0], 'Temperature', 'Temperature_Rolling', 'Temperature with Rolling Average', 'Temperature (°C)', 'red', 'orange')
    plot_time_series(df, axes[1, 1], 'Power', 'Power_Rolling', 'Power Consumption with Rolling Average', 'Power (W)', 'purple', 'violet')

    # Histograms
    plot_histograms(df, axes[2, 0], 'CPU', 'Memory', 'blue', 'green')

    # Box plot
    plot_boxplot(df, axes[2, 1])

    # Tight layout issues might overlap plots
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)

    # Save each plot as a PNG file
    fig.savefig(f'{output_dir}/system_resource_usage_analysis.png')
    plt.show()
