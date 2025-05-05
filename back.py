import os
import time
import subprocess
import sys

def update():

    platform = 'test'
    if platform == 'linux' or platform == 'linux2':
        #speed Test -->
        lx_curl = subprocess.run({'sudo apt-get install curl'}, shell=True, capture_output=True, text=True)
        lx_update = subprocess.run({'curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash'}, shell=True, capture_output=True, text=True)
        lx_install = subprocess.run({'sudo apt-get install speedtest'}, shell=True, capture_output=True, text=True)
    
        print('updating...\n')
        print(lx_curl.stdout())
        print(lx_update.stdout())
        print(lx_install.stdout())
        print('\n-=-'*13)
        print('Verify if it was installed correctly!!!')
        time.sleep(0.5)
        input('Type ENTER something to Continue: ')
    
    elif platform == 'win32':
        print('test')
        
def wpa2_brute_force():
    print('test')

def ip_loockup():
    print('test')

def speed_test():
    print('test')

update()