Python script to ping all IP addresses in a network:


#!/usr/bin/python
#import the modules required for this script
import subprocess
import ipaddress
from subprocess import Popen, PIPE
subnet = input("Please enter the network: ")
network = ipaddress.ip_network(subnet)
for i in network.hosts():
    i=str(i)
    toping = subprocess.Popen(['ping', '-c', '3', i], stdout=PIPE)
    output = toping.communicate()[0]
    hostalive = toping.returncode
    if hostalive == 0:
        print(i, 'is reachable')
    else:
       print(i, 'is down')


       
