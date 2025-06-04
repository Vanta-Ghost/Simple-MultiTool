import requests
import os
import json

logo = """ 
\033[38;2;51;51;204;12m
 █████   █████                       █████                   █████████  █████                        █████   
░░███   ░░███                       ░░███                   ███░░░░░███░░███                        ░░███    
 ░███    ░███   ██████   ████████   ███████    ██████      ███     ░░░  ░███████    ██████   █████  ███████  
 ░███    ░███  ░░░░░███ ░░███░░███ ░░░███░    ░░░░░███    ░███          ░███░░███  ███░░███ ███░░  ░░░███░   
 ░░███   ███    ███████  ░███ ░███   ░███      ███████    ░███    █████ ░███ ░███ ░███ ░███░░█████   ░███    
  ░░░█████░    ███░░███  ░███ ░███   ░███ ███ ███░░███    ░░███  ░░███  ░███ ░███ ░███ ░███ ░░░░███  ░███ ███
    ░░███     ░░████████ ████ █████  ░░█████ ░░████████    ░░█████████  ████ █████░░██████  ██████   ░░█████ 
     ░░░       ░░░░░░░░ ░░░░ ░░░░░    ░░░░░   ░░░░░░░░      ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░░     ░░░░░  
                                                                                                             
                                                                                                             
            \033[0m                                                                                                 

"""
while True:
    os.system("title Vanta Ghost")
    os.system("cls")
    print(logo)
    print("Vanta Ghost")
    print("[1] IP lookup")
    print("[2] Webhook Sender")
    print("[3] Show HWID")
    print("")
    x = input("Option:  ")
    
    if x == "1":
        os.system("cls")
        print("IP lookup\n")
        ip = input("Enter IP address:")
        os.system("cls")
        r = request.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        print("RESULTS\n")
        print(f"\033[38;2;0;255;0;12mCountry:\033[0m  {data["country"]}")
        print(f"\033[38;2;0;255;0;12mCity:\033[0m  {data["city"]}")
        print(f"\033[38;2;0;255;0;12mRegion:\033[0m  {data["regionName"]}")
        print(f"\033[38;2;0;255;0;12mTimeZone:\033[0m  {data["timezone"]}")
        print("")
        pause = input("Press enter to return...")
        
    if x == "2":
        os.system("cls")
        print("IP Webhook Sender\n")
        url = input("Webhook url: ")
        message = input("message: ")
        name = input("webhook name: ")
        
        


