import subprocess
import configparser
import time

def open_Programs():
    config = configparser.ConfigParser()
    config.read('../config.ini') # Create config.ini file with all the paths for the programs and folders you want to use
    
    outlook_path = config.get('ProgramPaths', 'Outlook')
    explorer_path = config.get('ProgramPaths', 'Explorer')
    opera_path = config.get('ProgramPaths', 'Opera')
    chrome_path = config.get('ProgramPaths', 'Chrome')
    folder_path = config.get('FolderPaths', 'Beto')
    web_address_one = config.get('WebAddresses', 'AbaNinja')
    web_address_two = config.get('WebAddresses', 'ChatGPT')
    
    subprocess.Popen([outlook_path])
    time.sleep(3)
    subprocess.Popen([explorer_path, folder_path])
    time.sleep(3)
    subprocess.Popen([opera_path, web_address_one])
    time.sleep(3)
    subprocess.Popen([chrome_path, web_address_two])


open_Programs()

