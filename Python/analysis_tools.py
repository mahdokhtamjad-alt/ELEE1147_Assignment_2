import data_processing as dp
import visualisation as vs

def analyze_log_file(log_file, output_dir='results'):
    """Main function to orchestrate the analysis and visualization of the log file."""
    df = dp.parse_log_file(log_file)  
    dp.calculate_rolling_averages(df)
    dp.detect_anomalies(df)
    summary_stats, correlation_matrix = dp.perform_analysis(df)  
    dp.save_results(summary_stats, correlation_matrix, output_dir)
    vs.generate_plots(df, output_dir) 
