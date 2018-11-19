
import os
import sys
import string


print("Check dependencies: ")
print("")

os.system('test /usr/bin/python  && echo "[+] Python ok" || apt-get -y install python')
os.system('test /usr/bin/mdk3 && echo "[+] Mdk3 ok" || apt-get -y install mdk3')
os.system('test /usr/bin/aircrack-ng && echo "[+] Aircrack-ng ok" || apt-get -y install aircrack-ng')
print("")

print("Listing Wireless extensions: ")
os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' | grep 'w' > card.sh && cat -n card.sh")
print("")

wlancard = raw_input("Please select one Wireless extension: ")
os.system('cat card.sh | grep -n ^ | grep '+wlancard+' | cut -d: -f2 > card.sh')
os.system('card=`cat card.sh` && airodump-ng $card')
