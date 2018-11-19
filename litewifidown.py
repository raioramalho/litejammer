
import os
import sys
import string

os.system('test /usr/bin/python  && echo "[+] Python ok" || apt-get -y install python')
os.system('test /usr/bin/mdk3 && echo "[+] Mdk3 ok" || apt-get -y install mdk3')
os.system('test /usr/bin/aircrack-ng && echo "[+] Aircrack-ng ok" || apt-get -y install aircrack-ng')

print("Listing Wlancard: ")
wlanscan = os.system('ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^/   /' | grep 'w'')
wlancard = raw_input("Please select one Wlancard: ")
