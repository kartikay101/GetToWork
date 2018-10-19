import time
import os
from datetime import datetime as dt

#class OS(Enum):
#    def checkPlatform(osName):
#        return osName.lower()== platform.system().lower()
#
#    MAC = checkPlatform("darwin")
#    LINUX = checkPlatform("linux")
#    WINDOWS = checkPlatform("windows")
#
if os.name == 'posix':
    #hosts_file=("/etc/hosts") # on an ubuntu platform it can be found here
    hosts_file=("hostslist") # for testing purposes
elif os.name == 'nt':
    hosts_file=r"C:\Windows\System32\Drivers\etc\hosts"



local="127.0.0.1"
website_list=[] # empty is better

stime=0
etime=0

def start():
 global website_list
 global stime
 global etime
 while len(website_list)>0 :
    if dt.now()>stime and dt.now()<etime:
        print("here")
        with open(hosts_file,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(local+" "+ website+"\n")
    else:
        with open(hosts_file,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            website_list=[]
            break
    time.sleep(10)

def remover(value):  # added for instant removal of site from the list
    with open(hosts_file,'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if value not in line:
                file.write(line)
        file.truncate()
