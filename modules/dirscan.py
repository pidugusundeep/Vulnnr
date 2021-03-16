import requests, threading, colorama, time, sys
from colorama import init, Fore
PURPLE = Fore.LIGHTMAGENTA_EX
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Fore.RESET
init(autoreset=True)

file = open("dirs.txt","r") 
Counter = 0
oop = 0
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
        
'''
https://github.com/rpie/Vulner/blob/main/modules.py Hellsecs Dir scanner all credits to him
'''

def requestdir(url):
    try:
        
        req = requests.get(url=url, timeout=5,  headers={"user-agent": "Vulnnr"})
        if "not found" in req.text:
            #print(f'{PURPLE} [ {GREEN}? {PURPLE}] {Fore.RED}404 { PURPLE}[ {GREEN}{len(req.content)} {RESET}bytes {PURPLE}]{Fore.WHITE}  -  {url.replace("//", "/")}')
            return
        elif "The page you are looking for could not be found" in req.text:
            #print(f'{PURPLE} [ {GREEN}? {PURPLE}] {Fore.RED}404 { PURPLE}[ {GREEN}{len(req.content)} {RESET}bytes {PURPLE}]{Fore.WHITE}  -  {url.replace("//", "/")}')
            return
        if req.status_code == 200:
            print(f'{PURPLE} [ {GREEN}$ {PURPLE}] {GREEN}{req.status_code} {PURPLE}[ {GREEN}{len(req.content)} {RESET}bytes {PURPLE}]{Fore.WHITE}  -  {url.replace("//", "/")}')
        
            

            
            
        elif req.status_code != 404:
            print(f'{PURPLE} [ {GREEN}? {PURPLE}] {Fore.YELLOW}{req.status_code} { PURPLE}[ {GREEN}{len(req.content)} {RESET}bytes {PURPLE}]{Fore.WHITE}  -  {url.replace("//", "/")}')
        


        
        if TimeoutError:
            time.sleep(0.4)
            pass
        
        
        
    except Exception as e:
        
        print(f"\n{PURPLE} [ {GREEN}! {PURPLE}] {Fore.RESET}Connection {RED}Timeout\n")
        time.sleep(2)
            


def dirscan():
    print(f"\n {PURPLE}[ {GREEN}* {PURPLE}] {YELLOW}if u would like to add more directories please edit modules/dirs.txt\n")
    target = input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}Target {PURPLE}=> {RESET}")
    print()
    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Loaded {Counter} directories")
    oop = 0
    dirs = open('dirs.txt', 'r').readlines()
    for content in dirs:
        content = content.rstrip()
        url = target+'/'+content
        t = threading.Thread(target=requestdir, args=(url, ))
        t.start()
        time.sleep(0.5)
        
        
        