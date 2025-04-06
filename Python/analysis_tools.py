"""
Script for reading logs, processing data, evaluating and visualising the results. 
"""
import data_processing as dp
import visualisation as vs

def analyze_log_file(log_file, output_dir='results'):
    """Main function to orchestrate the analysis and visualization of the log file."""
    df = dp.parse_log_file(log_file)  # Parse log file into dataframe
    dp.calculate_rolling_averages(df) # Calculate rolling averages
    dp.detect_anomalies(df) # Detect instances of high CPU usage
    summary_stats, correlation_matrix = dp.perform_analysis(df)  # Run analysis
    dp.save_results(summary_stats, correlation_matrix, output_dir) # Saves results to output direectory
    vs.generate_plots(df, output_dir) #Create generate visual plot charts
