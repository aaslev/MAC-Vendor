# Mac to vendor lookup script
# lookup.txt which is a "sh ip arp" output from a cisco L3 switch / router
# aaslev 2017-10-13
##################### import libraries #####################
import os
import re #regexp library
import requests
from datetime import datetime
##################### Define variables #####################
url = "https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf"
startTime = datetime.now() #Set start time for script
#rstring = r'([0-9a-fA-F]{4}.[0-9a-fA-F]{4}.[0-9a-fA-F]{4})' # <- old regexp
rstring = r'([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}' #pick from arp
rstring2 = r'([0-9a-fA-F]{2}\:){2}[0-9a-fA-F]{2}' #pick from mac list
mac_to_vendor = [] #define list
##################### Define Functions #####################
def MAC_database():
    if os.path.isfile('mac.txt'):
        print "MAC Database exists, initiating main program >\n"
    else:
        print "Downloading MAC Database... "
        r = requests.get(url)
        with open("mac.txt", "wb") as macdb:
            macdb.write(r.content)
        print "Done!"

    with open('mac.txt', 'r') as file2:
        for readline in file2:
            mac_to_vendor.append(readline)

def MAC_compare():
    for line2 in mac_to_vendor:
        mac_address2 = re.search(rstring2, line2)
        if mac_address2:
            mac2 = line2.split("\t")
            mac3 = line2[0:8].replace(":","")
            mac3 = mac3.replace(" ","")

            if mac == mac3:
                print mac_address.group(), "\t", mac2[1]
                break
##################### main program #####################
os.system('clear')
MAC_database() #check if mac "database" exists, otherwise download it.
print "Mac address\tCorporation\n-----------\t-----------"

with open('lookup.txt', 'r') as file1:
        for line in file1:
            mac_address = re.search(rstring, line)
            if mac_address:
                mac = mac_address.group().replace(".","").upper()[0:6] #put the result in a regular string and strip the dots
                mac = mac.replace(" ","")

                MAC_compare() #check against wireshark mac vendor list:

print "-------------------------------\n\nrun time: " , datetime.now() - startTime
