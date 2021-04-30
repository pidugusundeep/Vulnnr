import requests
import colorama 
from colorama import Fore, init
init()

file_name = input(f" {Fore.RED}[ {Fore.GREEN}? {Fore.RED}] {Fore.RESET}File path {Fore.LIGHTMAGENTA_EX}=>{Fore.RESET} ")
oop  = open(file_name, 'r').readlines()
lol = len(oop)
def auto(url):
    
    try:
        counter = 0
        o = requests.get(url, timeout=5)
        if "drwxr-xr-x" in o.text:
            print(' {}[ {}$ {}] {}Working Shell => {}'.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET, o.url))
        elif "-rw-r--r--" in o.text:
            print(' {}[ {}$ {}] {}Working Shell => {}'.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET, o.url))
        if "404" in o.text:
            pass

        else:
            
            
            print(' {}[ {}? {}] {}No Shell => {}'.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET, o.url))
        
    except:
        print(' {}[ {}? {}] {}Connection Dropped'.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET))
        pass



with open(file_name, 'r') as f:
    print(' {}[ {}? {}] {}Started Vulnnr_Shell_Checker 1.0v '.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET))
    print(' {}[ {}* {}] {}Loaded {} {} {}urls \n'.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET, Fore.YELLOW, lol, Fore.RESET))
    buf = f.readlines()
    if buf[-1] == '\n':
        buf = buf[:-1]
    urls = [x[:-1] for x in buf]
    for url in urls:
        auto(url)
        
    print(' {}[ {}! {}] {}Done '.format(Fore.RED, Fore.GREEN, Fore.RED, Fore.RESET))