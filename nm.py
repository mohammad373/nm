# nm

import os
import sys
import time
import socket
import requests
import webbrowesr as web
from colorama import Fore

my_list = ["cpanel" , "bot.txt"  , "admin"] 

def __web__():
    os.system("clear")
    time.sleep(1)
    print(Fore.YELLOW + "Hello . Welcome Back ;)")
    time.sleep(1)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "*" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter The address Target " + Fore.GREEN + "==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "Error : Your Target Is Not Found Or None ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    if not "https" in target or not "http" in target:
        target = "http://" + target
    else:
        pass
    
    s = socket.gethostbyname(target)
    time.sleep(1)
    print(Fore.GREEN + "[+] ~ Your Ip Target is  :  " + Fore.BLUE + s)
    time.sleep(1)
    r = requests.get(target + "/" + "/wp-content/plugins/")
    if r.status_code == 404 or r.status_code == 500:
        try:
            print(Fore.RED + "[!] ~ Your Target Is Not WordPress ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    else:
        try:
            print(Fore.GREEN + "[*] ~ Your Target Is WordPress ;)")
            time.sleep(1)
            for i in my_list:
                try:
                    w = target + "/" + "/wp-content/plugins/" + i
                    if w.status_code == 404 or w.status_code == 500:
                        print(Fore.RED + w + Fore.YELLOW + " > " + Fore.BLUE + "Not Found ;(")
                    else:
                        print(Fore.GREEN + w + Fore.YELLOW + " > " + Fore.BLUE + "Found ;)")
                    
        except:
            pass
__web__()
