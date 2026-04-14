#!/bin/bash
# Shadow Framework v5.0 - Auto Installer

# কালার কোড
G='\e[32m'
R='\e[31m'
Y='\e[33m'
B='\e[34m'
W='\e[0m'

clear
echo -e "${G}#######################################################${W}"
echo -e "${G}#                                                     #${W}"
echo -e "${G}#       SHADOW FRAMEWORK v5.0 INSTALLER               #${W}"
echo -e "${G}#                                                     #${W}"
echo -e "${G}#######################################################${W}"
echo ""

# ১. সিস্টেম আপডেট ও আপগ্রেড
echo -e "${B}[*] Updating system packages...${W}"
pkg update && pkg upgrade -y

# ২. প্রয়োজনীয় প্যাকেজ ইনস্টল করা
echo -e "${B}[*] Installing core dependencies...${W}"
pkg install python git nmap php curl wget whois dnsutils neofetch openssh -y

# ৩. পাইথন প্যাকেজ ইনস্টল করা
echo -e "${B}[*] Installing Python libraries...${W}"
pip install --upgrade pip
pip install colorama requests sqlmap

# ৪. ফাইল পারমিশন সেট করা
echo -e "${B}[*] Setting file permissions...${W}"
chmod +x shadow.py
chmod +x installer.sh

# ৫. গুরুত্বপূর্ণ টুল চেক (Sherlock & Zphisher requirements)
echo -e "${B}[*] Checking for extra requirements...${W}"
pkg install libxslt libxml2 -y # For Sherlock/some python tools

echo ""
echo -e "${G}#######################################################${W}"
echo -e "${G}#         INSTALLATION SUCCESSFULLY COMPLETE!         #${W}"
echo -e "${G}#######################################################${W}"
echo -e "${Y}এখন টুলটি চালু করতে লিখুন: python shadow.py${W}"
echo ""
