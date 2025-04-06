"""
Script for reading logs, analyzing readings and saving the results.
"""


import pandas as pd  
import numpy as np

def parse_log_line(line):
    """Parse a single line of the log file into its components."""
    try:
        timestamp, metrics = line.split(' - ')
        timestamp = pd.to_datetime(timestamp)
        
        # Extract metrics from "metric: value" format
        metrics = metrics.split(', ')
        cpu = int(metrics[0].split(': ')[1])
        mem = int(metrics[1].split(': ')[1])
        temp = int(metrics[2].split(': ')[1])
        power = int(metrics[3].split(': ')[1])
        
        return [timestamp, cpu, mem, temp, power] 
    except Exception as e:
        print(f"Error parsing line: {line}. Error: {e}")
        return None  

def parse_log_file(log_file):
    """Read and parse the entire log file into a DataFrame."""
    with open(log_file, 'r') as file:
        data = [parse_log_line(line) for line in file]
    
    # Creates dataframe and drops any rows that return as None
    df = pd.DataFrame(data, columns=['Timestamp', 'CPU', 'Memory', 'Temperature', 'Power']) 
    df.dropna(inplace=True)

    # Uses timestamp as the index for time series analysis
    df.set_index('Timestamp', inplace=True) 

    return df  

def calculate_rolling_averages(df, window=5):
    """Calculate rolling averages for the given DataFrame."""
    df['CPU_Rolling'] = df['CPU'].rolling(window=window).mean()
    df['Memory_Rolling'] = df['Memory'].rolling(window=window).mean()  
    df['Temperature_Rolling'] = df['Temperature'].rolling(window=window).mean()
    df['Power_Rolling'] = df['Power'].rolling(window=window).mean()

def detect_anomalies(df):
    """Detect anomalies in the DataFrame (e.g., CPU usage > 90%)."""
    df['CPU_Anomaly'] = df['CPU'] > 90  

def perform_analysis(df):
    """Perform and print basic analysis: summary statistics and correlation matrix."""
    summary_stats = df.describe()
    correlation_matrix = df.corr() 

    print("Summary Statistics:")
    print(summary_stats)  
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    return summary_stats, correlation_matrix

def save_results(summary_stats, correlation_matrix, output_dir='results'):
    """Save the analysis results to CSV files."""
    summary_stats.to_csv(f'{output_dir}/summary_statistics.csv')
    correlation_matrix.to_csv(f'{output_dir}/correlation_matrix.csv')
