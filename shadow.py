import os
import sys
import time
import requests
import datetime
import socket
import platform
import subprocess
from colorama import Fore, Style

# কালার সেটিংস
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
B = Fore.BLUE
W = Style.RESET_ALL

LOG_FILE = "shadow_logs.txt"

def banner():
    os.system('clear')
    print(f"""{R}
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
               {G}[ SHADOW v5.6 - THE MEGA FRAMEWORK ]{W}
    {Y}-------------------------------------------------------{W}
    {C} User: shipon | System: Termux | Version: 5.6 Gold {W}
    {Y}-------------------------------------------------------{W}
    """)

def write_log(message):
    with open(LOG_FILE, "a") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] {message}\n")

def run_cmd(cmd):
    print(f"\n{G}[*] Status: Running Process...{W}")
    print(f"{B}[#] Shell Command: {cmd}{W}\n")
    try:
        write_log(f"Executed: {cmd}")
        os.system(cmd)
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")
    print(f"\n{Y}-------------------------------------------------------{W}")
    input(f"{G}[+] Press Enter to return to menu...{W}")

def get_sys_info():
    banner()
    print(f"{C}--- System Information ---{W}")
    print(f"{Y}[+] Device: {platform.node()}")
    print(f"[+] OS: {platform.system()} {platform.release()}")
    print(f"[+] Architecture: {platform.machine()}")
    print(f"[+] Python Version: {platform.python_version()}")
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print(f"[+] Local IP: {ip_addr}{W}")
    input(f"\n{C}Press Enter to Back...{W}")

# --- ১. ইনফরমেশন গ্যাদারিং ---
def info_gathering():
    while True:
        banner()
        print(f"{C}১. Nmap (Network Scanner)")
        print(f"২. Whois (Domain Info)")
        print(f"৩. IP-Tracer (Geo Location)")
        print(f"৪. DNS Lookup (Host Record)")
        print(f"৫. Discord User OSINT")
        print(f"০. Back{W}")
        ch = input(f"\n{G}Shadow(Info) > {W}")
        if ch == '1':
            ip = input(f"{Y}Target IP/URL: {W}")
            run_cmd(f"nmap -A -v {ip}")
        elif ch == '2':
            dom = input(f"{Y}Domain Name: {W}")
            run_cmd(f"whois {dom}")
        elif ch == '3':
            ip = input(f"{Y}IP Address: {W}")
            run_cmd(f"curl http://ip-api.com/line/{ip}")
        elif ch == '4':
            dom = input(f"{Y}Domain: {W}")
            run_cmd(f"nslookup {dom}")
        elif ch == '5':
            discord_osint()
        elif ch == '0': break

def discord_osint():
    banner()
    print(f"{C}--- Discord OSINT Tool ---{W}")
    user_id = input(f"{Y}Enter Target User ID: {W}")
    url = f"https://discordlookup.mesalytic.moe/v1/user/{user_id}"
    try:
        req = requests.get(url).json()
        if 'username' in req:
            print(f"\n{G}[+] Username: {req['username']}")
            print(f"[+] Global Name: {req.get('global_name', 'N/A')}")
            print(f"[+] Badges: {', '.join(req.get('badges', ['None']))}")
            print(f"[+] Avatar: {req.get('avatar', {}).get('link', 'N/A')}{W}")
        else: print(f"{R}[!] User not found!{W}")
    except: print(f"{R}[!] Error reaching API.{W}")
    input(f"\n{G}Press Enter...{W}")

# --- ২. ওয়েব ভালনারেবিলিটি ---
def web_attack():
    while True:
        banner()
        print(f"{C}১. Nikto (Vuln Scan)\n২. SQLMap (Database)\n৩. Nuclei (Advanced)\n৪. Dirb (Directory){W}")
        print(f"৫. Admin Panel Finder\n০. Back")
        ch = input(f"\n{G}Shadow(Web) > {W}")
        if ch == '1':
            url = input("URL: "); run_cmd(f"nikto -h {url}")
        elif ch == '2':
            url = input("Vulnerable URL: "); run_cmd(f"sqlmap -u {url} --batch --random-agent")
        elif ch == '3':
            url = input("URL: "); run_cmd(f"nuclei -u {url}")
        elif ch == '4':
            url = input("URL: "); run_cmd(f"dirb {url}")
        elif ch == '0': break

# --- ৩. ফিশিং সেকশন ---
def phishing():
    while True:
        banner()
        print(f"{C}১. Zphisher\n২. PyPhisher\n৩. Seeker (Location)\n০. Back{W}")
        ch = input(f"\n{G}Shadow(Phish) > {W}")
        if ch == '1':
            os.system("cd zphisher && bash zphisher.sh")
        elif ch == '2':
            os.system("cd PyPhisher && python3 pyphisher.py")
        elif ch == '3':
            os.system("cd seeker && python3 seeker.py")
        elif ch == '0': break

# --- ৪. সোশ্যাল হান্টার (Sherlock) ---
def social_hunter():
    banner()
    print(f"{C}--- Sherlock Username Tracker ---{W}")
    user = input(f"\n{G}Enter Username: {W}")
    run_cmd(f"python3 sherlock/sherlock/sherlock.py {user}")

# --- ৫. আইপি লগিং ও ট্র্যাকিং ---
def ip_tracker():
    while True:
        banner()
        print(f"{C}১. Create IP Logger (Grabify Info)\n২. IP Address Details\n৩. My IP Info\n০. Back{W}")
        ch = input(f"\n{G}Shadow(IP) > {W}")
        if ch == '1':
            print(f"{Y}[*] Visit: https://grabify.link\n[*] Create a link and track target IP.{W}")
            input("\nPress Enter...")
        elif ch == '2':
            ip = input("Target IP: "); run_cmd(f"curl http://ip-api.com/line/{ip}")
        elif ch == '3':
            run_cmd("curl ifconfig.me")
        elif ch == '0': break

# --- মেইন মেনু ---
def main():
    while True:
        banner()
        print(f"{Y}১. Information Gathering   ২. Web Attack & Scan")
        print("৩. Phishing Attacks        ৪. Social Media Hunter")
        print("৫. IP & Discord Tracker    ৬. System Information")
        print(f"৭. Exploitation (Payload)  ৮. View History Logs")
        print(f"৯. Update Shadow Tool      ০. Exit{W}")
        
        choice = input(f"\n{G}Shadow(Main) > {W}")

        if choice == '1': info_gathering()
        elif choice == '2': web_attack()
        elif choice == '3': phishing()
        elif choice == '4': social_hunter()
        elif choice == '5': ip_tracker()
        elif choice == '6': get_sys_info()
        elif choice == '7': run_cmd("msfconsole")
        elif choice == '8': run_cmd(f"cat {LOG_FILE}")
        elif choice == '9':
            print("Updating..."); os.system("git pull")
        elif choice == '0':
            print(f"{R}Exiting Shadow...{W}"); sys.exit()
        else:
            print(f"{R}ভুল অপশন!{W}"); time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped by user.{W}")
        sys.exit()
