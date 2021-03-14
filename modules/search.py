from googlesearch import search
import time
import colorama
from colorama import init, Fore
init()

PURPLE = Fore.LIGHTMAGENTA_EX
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
RESET = Fore.RESET


def dorker(dork, count):
    requ = 0
    filename = "Results/Dorked.txt"
    counter = 0
    f = open(filename, "w+")
        
    for results in search(dork, tld="com", lang="en", num=int(count), start=0, stop=None, pause=2):
        counter = counter + 1
        
        print (f" {PURPLE}[ {GREEN}$ {PURPLE}]{RESET}", counter, results.split('/')[2])
        
        time.sleep(0.1)
        requ += 1
        if requ >= int(count):
            break
        data = (counter, results)
        f.write("http://"+results.split('/')[2] + "/" + '\n')
        
    f.close()
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}saved results to {GREEN}{filename}")
        
