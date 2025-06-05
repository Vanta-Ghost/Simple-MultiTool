import requests
import os
import json
import platform
import uuid
import hashlib
import subprocess

logo = """ 
\033[38;2;51;51;204m
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

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_hwid():
    try:
        mac = uuid.getnode()
        system = platform.system()
        
        if system == "Windows":
            volume = subprocess.check_output("vol C:", shell=True).decode()
            serial = volume.split()[-1]
        else:
            serial = subprocess.check_output("cat /etc/machine-id", shell=True).decode().strip()

        raw = f"{mac}-{serial}"
        hwid = hashlib.sha256(raw.encode()).hexdigest()
        return hwid
    except Exception as e:
        return f"Error fetching HWID: {e}"

while True:
    os.system("title Vanta Ghost")
    clear_screen()
    print(logo)
    print("Vanta Ghost")
    print("[1] IP Lookup")
    print("[2] Webhook Sender")
    print("[3] Show HWID")
    print("")
    x = input("Option: ").strip()
    
    if x == "1":
        clear_screen()
        print("IP Lookup\n")
        ip = input("Enter IP address: ").strip()
        clear_screen()
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}")
            data = r.json()
            if data["status"] == "success":
                print("RESULTS\n")
                print(f"\033[38;2;0;255;0mCountry:\033[0m  {data['country']}")
                print(f"\033[38;2;0;255;0mCity:\033[0m     {data['city']}")
                print(f"\033[38;2;0;255;0mRegion:\033[0m   {data['regionName']}")
                print(f"\033[38;2;0;255;0mTimeZone:\033[0m {data['timezone']}\n")
            else:
                print("Invalid IP or no data found.")
        except Exception as e:
            print("Error during lookup:", e)
        input("Press Enter to return...")

    elif x == "2":
        clear_screen()
        print("Webhook Sender\n")
        url = input("Webhook URL: ").strip()
        message = input("Message: ").strip()
        name = input("Webhook Name: ").strip()

        data = {
            "content": message,
            "username": name
        }

        try:
            r = requests.post(url, json=data)
            if r.status_code in [200, 204]:
                print("✅ Webhook sent successfully!")
            else:
                print("❌ Failed to send webhook. Check the URL.")
        except Exception as e:
            print("ERROR SENDING WEBHOOK:", e)

        input("Press Enter to return...")

    elif x == "3":
        clear_screen()
        print("Your HWID (hashed):\n")
        print(get_hwid())
        print("")
        input("Press Enter to return...")

    else:
        print("Invalid option.")
        input("Press Enter to return...")
