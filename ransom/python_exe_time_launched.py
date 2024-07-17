# WE NEED TO INSTALL THE FOLLOWING BELOW
# pip install psutil
# THIS PROGRAM EVALUATES THE TIME AN EXE WAS LAUNCHED
import psutil
import os
import datetime

def get_process_creation_time(process_name):
    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        if proc.info['name'] == process_name:
            return datetime.datetime.fromtimestamp(proc.info['create_time'])
    return None

if __name__ == "__main__":
    process_name = "YourExecutableName"  # Replace with your executable name without .exe
    create_time = get_process_creation_time(process_name)

    if create_time:
        print(f"The process '{process_name}' was loaded at: {create_time}")
    else:
        print(f"Process '{process_name}' not found or information unavailable.")
