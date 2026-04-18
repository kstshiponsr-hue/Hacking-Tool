#!/bin/bash
# Shadow Framework v5.6 - Official Installer
# Author: shipon

# কালার কোড ডিফাইন
G='\e[32m'
R='\e[31m'
Y='\e[33m'
B='\e[34m'
C='\e[36m'
W='\e[0m'

clear
echo -e "${G}#######################################################${W}"
echo -e "${G}#                                                     #${W}"
echo -e "${G}#       SHADOW MEGA-INSTALLER v5.6                    #${W}"
echo -e "${G}#       System Configuration & Setup                  #${W}"
echo -e "${G}#                                                     #${W}"
echo -e "${G}#######################################################${W}"
echo ""

# ১. সিস্টেম আপডেট ও আপগ্রেড
echo -e "${C}[*] Updating system packages...${W}"
pkg update && pkg upgrade -y

# ২. মূল লিনাক্স প্যাকেজসমূহ ইনস্টল
echo -e "${C}[*] Installing core Linux tools...${W}"
packages=(python git nmap php curl wget whois dnsutils neofetch openssh clang libxml2 libxslt)
for pkg in "${packages[@]}"; do
    echo -e "${B}[+] Installing $pkg...${W}"
    pkg install "$pkg" -y
done

# ৩. পাইথন লাইব্রেরি সেটআপ
echo -e "${C}[*] Setting up Python environment...${W}"
pip install --upgrade pip
pip install colorama requests sqlmap

# ৪. এক্সটারনাল টুলস ক্লোনিং (যদি না থাকে)
echo -e "${C}[*] Cloning third-party hacking tools...${W}"

# Zphisher
if [ ! -d "zphisher" ]; then
    echo -e "${B}[+] Cloning Zphisher...${W}"
    git clone --depth=1 https://github.com/htr-tech/zphisher.git
fi

# PyPhisher
if [ ! -d "PyPhisher" ]; then
    echo -e "${B}[+] Cloning PyPhisher...${W}"
    git clone https://github.com/KasRoudra/PyPhisher.git
fi

# Sherlock
if [ ! -d "sherlock" ]; then
    echo -e "${B}[+] Cloning Sherlock...${W}"
    git clone https://github.com/sherlock-project/sherlock.git
    echo -e "${Y}[!] Installing Sherlock requirements...${W}"
    pip install -r sherlock/requirements.txt
fi

# Seeker
if [ ! -d "seeker" ]; then
    echo -e "${B}[+] Cloning Seeker...${W}"
    git clone https://github.com/thewhiteh4t/seeker.git
fi

# ৫. ফাইল পারমিশন এবং ক্লিনআপ
echo -e "${C}[*] Finalizing configuration...${W}"
chmod +x shadow.py
chmod +x installer.sh

# ৬. ফিনিশিং মেসেজ
clear
echo -e "${G}"
echo "    ____  ____  _   _  ____  ____  _      "
echo "   / ___||  _ \| | | |/ ___||  _ \| |     "
echo "   \___ \| |_) | |_| | |  _ | |_) | |     "
echo "    ___) |  __/|  _  | |_| ||  __/|_|     "
echo "   |____/|_|   |_| |_|\____||_|   (_)     "
echo -e "${W}"
echo -e "${G}#######################################################${W}"
echo -e "${G}#         INSTALLATION SUCCESSFULLY COMPLETE!         #${W}"
echo -e "${G}#             ALL TOOLS ARE READY TO USE              #${W}"
echo -e "${G}#######################################################${W}"
echo ""
echo -e "${Y}টুলটি শুরু করতে টাইপ করুন: python shadow.py${W}"
echo ""
