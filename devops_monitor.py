from modules.server_monitor import Server, WebServer, DatabaseServer, check_all_servers
from modules.log_manager import log_message, parse_log, backup_logs
import argparse
from modules.disk_monitor import check_disk_space
from modules.http_checker import check_http
from modules.alert import send_alert
from modules.report import generate_report



server1 = Server("FrontEnd", "192.168.0.1" ,"UNKNOWN")
server2 = WebServer("BackEnd", "192.168.0.2", "ONLINE", "8080")
server3 = DatabaseServer("DataBase", "192.168.0.3", "ONLINE", "MYSQL")


def parse_arguments():
    parser = argparse.ArgumentParser(description="script related Devops monitor tool")
    parser.add_argument('status_message', type=str, help="system status message to log")
    return parser.parse_args()


def main():
    print("\n====== DevOps Monitor Starting ======\n")

    args = parse_arguments()  # first thing!
 

    # step 1: check all servers after defining them as a list 
    servers = [server1, server2, server3]
    server_data = check_all_servers(servers)

    # step 2: check disk space
    check_disk_space('/')

    # step 3: check http endpoint
    check_http('https://google.com')

    # step 4: log message
    log_message(args.status_message) 
  

    # step 5: parse logs for errors
    errors = parse_log()

    # step 6: send alert if errors found
    if errors:
        try:

           send_alert("Email Notification", "please check the system")
        except Exception as e:

            print(f"Email alert skipped: {e}")

    # step 7: generate report
    generate_report(server_data)

    # step 8: backup logs
    backup_logs()

    print("\n====== DevOps Monitor Complete ======\n")


    
if __name__ == "__main__":
    main()