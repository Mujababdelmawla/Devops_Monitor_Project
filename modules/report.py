import pandas as pd 
import os 

def generate_report(server_data):
    # server_data is the list of dicts from check_all_servers()
    df = pd.DataFrame(server_data)  # list of dicts → table
    # create reports folder if it doesn't exist
    os.makedirs('./reports', exist_ok=True)
    # save to CSV
    df.to_csv('./reports/health_report.csv', index=False)
    print("report has been generated successfully....")