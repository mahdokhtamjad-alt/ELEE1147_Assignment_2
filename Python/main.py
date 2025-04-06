import analysis_tools as at

def main():
    log_file = '../logs/sys.log'  
    output_dir = 'results' 

    at.analyze_log_file(log_file, output_dir)

if __name__ == '__main__':
            main() 
