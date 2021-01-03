1. # an IP address and print the IP

# function to remove leading zeros
def removeZeros(ip):

    # splits the ip by "."
    # converts the words to integeres to remove leading removeZe
    # convert back the integer to string and join them back to a string
    new_ip = ".".join([str(int(i)) for i in ip.split(".")])
    return new_ip ;

ip ="100.020.003.400"
print(removeZeros(ip))
# example2
ip ="001.200.001.004"
print(removeZeros(ip))


2. Extract IP address from file using Python

import re
with open('C:/Users/user/Desktop/New Text Document.txt') as fh:
   fstring = fh.readlines()

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
lst=[]
for line in fstring:
   lst.append(pattern.search(line)[0])
print(lst)


3.
