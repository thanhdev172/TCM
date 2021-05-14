import sys
from scapy.all import *

if len(sys.argv) !=4 :
	print("Usage %s target startport endport" %(sys.argv[0]))
	sys.exit(0)
target = str(sys.argv[1])
startPort = int(sys.argv[2])
endPort = int(sys.argv[3])
print("Scanning " + target + " for open TCP ports")

if(startPort == endPort):
	endPort += 1

for x in range(startPort, endPort):
	packet = IP(dst=target)/TCP(dport=x, flags='S')
	res = sr1(packet, timeout=0.5, verbose=0)
	if res.haslayer(TCP) and  res.getlayer(TCP).flags==0x12:
		print("Port " + str(x) + " is open!")
	sr(IP(dst=target) / TCP(dport=res.sport, flags='R'), timeout=0.5, verbose=0)
print("Scan is complete!")
