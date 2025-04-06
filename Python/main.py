"""
Main script to run system log analysis using analysis_tools with defined input/ouput paths.
"""
import analysis_tools as at

def main(): #Run analysis on log file
    log_file = '../logs/sys.log'  #Path to input log file
    output_dir = 'results' #Folder to save output

    at.analyze_log_file(log_file, output_dir)

if __name__ == '__main__':
            main() 
