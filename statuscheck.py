#Test status of bluetooth controller 
##maybe try to set it up in this step if it is not ready for pairing

import subprocess
from subprocess import *
import os

def main():
#get status
    cmd = ['bluetoothctl', 'show']
    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['awk', '{ print $2; }'], stdin=p1.stdout, stdout=subprocess.PIPE)
    output = (p2.communicate()[0]).decode()

#create list of cmd output
    status = []
    for line in output.split('\n'):
        status.append(line)
    status = list(filter(None, status))

#pull items from list
    power = status[4]
    discover = status[5]
    pair = status[7]

#print("\nBluetooth Status:\n\tPowered: ", power, "\n\tDiscoverable: ", discover, "\n\tPairable: ", pair, "\n")

    if power == 'no' or discover == 'no' or pair == 'no':
        print("\n\tBluetooth is not ready to connect\n")
        #answer = "Bluetooth is not ready to connect\n"
    else:
        print("\n\tBluetooth ready to connect\n")
        #answer = "Bluetooth ready to connect\n"
    
    #return(answer)

#if __name__ == "__main__":
#    main()
