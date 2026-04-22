# Devops Monitor :
A python automation tool that monitors infrastructure health to reduce and avoid the manual devops tasks

## What is it ?
Devops Monitor is a python CLI tool that automates a sequence of devops task to reduce time and manual work. it monitors servers , disk space, websites, and log files - all in a single command 

## What does it do ?
Instead of manually checking everything step by step . this tool automatically :
- Checks the status of all the servers as we define them using oop and then print each server's name, ip address, and it is current status .
- Monitors disk space and warns if free space is actually low . 
- Accepts custom status messages as command line arguments
- Logs system status message with timestamp everytime the script runs .
- Parse logs and detects errors and warnings . 
- Sends email notifications when critical errors found .
- generate a csv health report file for all servers .
- Backup log files into a compressed file .


## Project Structure :
```
devops-monitor/
│
├── devops_monitor.py        # main entry point — ties everything together
├── modules/
│   ├── server_monitor.py    # Server OOP classes + status checker
│   ├── log_manager.py       # logging, parsing and backup
│   ├── disk_monitor.py      # disk space monitoring
│   ├── http_checker.py      # HTTP endpoint checker
│   ├── alert.py             # email alerting system
│   └── report.py            # CSV report generator
│
├── logs/                    # all log files stored here
├── backups/                 # compressed log backups
├── reports/                 # CSV health reports
└── README.md                # project documentation
```

## Requirements  And Modules Used :
- System with python3 installed 
- pandas - csv report generation 
- smtplib - email alerting 
- requests - http retrieval data 
- os/shutil - disk monitoring and log backup 
- re - log parsing with regex 
- oop - server class hierarchy with inheritance 

## How To Run :
'''bash 
git clone https://github.com/Mujababdelmawla/Devops_Monitor_Project
cd devops_monitor 
python3 -m venv (env-name)
source (env-name)/bin/activate 
pipenv install requests 
pipenv install pandas ps 
python3 devops_monitor.py "the system is working fine .. nothing to look at ..everything up to date"
'''

## Future Improvements :
- Schedule automatic runs using cron 
- Connect to real Gmail SMTP for email alerts
- Send disk space alerts via email 

## Author :
Mujab Youef : A Devops Engineer In Training 
