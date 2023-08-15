import psutil
import subprocess
import configparser
import time

def close_program(process_name):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == process_name:
            psutil.Process(process.info['pid']).terminate()

def open_Programs():
    config = configparser.ConfigParser()
    config.read('../config.ini') # Create config.ini file with all the paths for the programs and folders you want to use
    
    vs_code_path = config.get('ProgramPaths', 'VSCode')
    explorer_path = config.get('ProgramPaths', 'Explorer')
    chrome_path = config.get('ProgramPaths', 'Chrome')
    onedrive_path = config.get('ProgramPaths', 'OneDrive')
    folder_path = config.get('FolderPaths', 'FullStackDev')
    web_address = config.get('WebAddresses', 'Localhost')

    subprocess.Popen([onedrive_path])
    time.sleep(3)
    subprocess.Popen([vs_code_path])
    time.sleep(3)
    subprocess.Popen([explorer_path, folder_path])
    time.sleep(3)
    subprocess.Popen([chrome_path, web_address])

close_program("steam.exe")
open_Programs()

