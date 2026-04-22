import os

def check_disk_space(path='/'):
    statvfs = os.statvfs(path)
    free_space = statvfs.f_frsize * statvfs.f_bavail
    free_gb = free_space / (1024 * 1024 * 1024)
    print(f"free disk space available is {free_gb}....")
    
    if free_gb < 10:
       print("WARNING: Low disk space!")
    return free_gb