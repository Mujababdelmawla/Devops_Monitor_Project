from datetime import datetime 
import os 
import shutil 
import re 

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"
    log_file = "./logs/devops.log"
    with open(log_file, 'a') as file :
        file.write(log_entry)

    print(f"the log message has been saved at {log_file} !....")

def parse_log():
    with open('./logs/devops.log', 'r') as file:
        logs = file.readlines()
        error_logs = [log for log in logs if re.search(r'ERROR|WARNING', log)]
        
    if error_logs:
        print("erorr logs has been detected !!....")

    return error_logs

def backup_logs():
    backup_dir = "./backups"
    # create the backup directory if it doesn't exists
    os.makedirs(backup_dir, exist_ok=True)
    # compress the logs folder inot backups
    shutil.make_archive('backups/logs_backup', 'zip', './logs')
    print(f"logs has been backed up to {backup_dir} successfully...")