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
    config.read('config.ini') # Create config.ini file with all the paths for the programs and folders you want to use
    
    steam_path = config.get('ProgramPaths', 'Steam')
    discord_path = config.get('ProgramPaths', 'Discord')
        
    subprocess.Popen([steam_path])
    time.sleep(3)
    subprocess.Popen(discord_path, shell=True) # Discord executes the Update.exe with the command --processStart Discord.exe


close_program("OneDrive.exe")
close_program("DeepL.exe")
open_Programs()

