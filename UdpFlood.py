import sys

from scapy.all import *

if len(sys.argv) != 3:

	print "usage: %s dst_ip dst_port" % sys.argv[0]

	print "example: %s 1.2.3.4 5001" %sys.argv[0]

	exit(1)

pkt = IP(dst=sys.argv[1])/UDP(dport=int(sys.argv[2]))

send(pkt, loop=1)
