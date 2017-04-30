""" Implementation of the Server side of the Point to Multipoint file tranfer using Stop and Wait ARQ"""

from socket import *
import sys
import random
import time

def printm(a,b,add):
	print "Number of messages sent = ", a
	print "Number of messages received = ", b
	soc = socket(AF_INET,SOCK_DGRAM)
	#h = "127.0.0.1"
	#s.bind(ap)
	soc.sendto("%d"%a,add)
	#soc.sendto("%d"%b,add)

""" Stores the number of command line arguments"""
no_of_arg=len(sys.argv)

if(no_of_arg!=2):
        print "expected format python %s <port no>" %(sys.argv[0])
	sys.exit(1)
""" specifies the IP of the server, hence the Network Interface is also known """
host="127.0.0.1"
""" Listening port of the server """
port=int(sys.argv[1])

h = []
p = []
a = []
randomList=[]
msent = 0
mreceived = 0

""" A datagram(UDP) socket is created and suports ipv4 addressing"""
s=socket(AF_INET,SOCK_DGRAM)

""" contains the source host address and port number as a tuple """
addr=(host,port)

""" the server binds to this socket and waits for hosts """
s.bind(addr)
""" the input buffer size is fixed to 2048 bytes """
buff_size=1024


#"""
# receiving no. of hosts
data,address=s.recvfrom(buff_size)
no_of_hosts = int(data)
ap = address
print " number of hosts  = ", no_of_hosts

#receiving left child
data,address=s.recvfrom(buff_size)
left = int(data)
#print "left child", left

#receiving right child
data,address=s.recvfrom(buff_size)
right = int(data)
#print "right child", right

#receiving parent
data,address=s.recvfrom(buff_size)
parent = int(data)
#print "parent", parent

#receive leader starter
data,address=s.recvfrom(buff_size)
chk = int(data)
#print "starting node = ", chk

for i in range(no_of_hosts):
	data,address=s.recvfrom(buff_size)
	h.append(data)
	data,address=s.recvfrom(buff_size)
	p.append(data)
	p[i] = int(p[i])
	a.append((h[i],p[i]))


if(chk==port):
    time.sleep(5)
    # sending election message to each node
    if parent == -1:
    	print "leader excepted as", port
    	for i in range(no_of_hosts):
			s.sendto("CMSG",a[i])
			s.sendto("%d"%port,a[i])
			msent = msent +1 
    	printm(msent,mreceived,ap)
    	sys.exit(0)
		
    
    else:
    	h = "127.0.0.1"
    	a = (h,parent)
    	s.sendto("%d"%port,a)
    	msent = msent + 1 
    
#"""
while(1==1):
	data,address = s.recvfrom(buff_size)
	mreceived = mreceived + 1
	#no_of_msgs = no_of_msgs +1
	if(data == "CMSG"):
		data,address = s.recvfrom(buff_size)
		print "Leader Excepted as" , int(data)
		printm(msent,mreceived,ap)  
		sys.exit(0);

	elif parent == -1:
		print "leader excepted as", port
		for i in range(no_of_hosts):
			s.sendto("CMSG",a[i])
			s.sendto("%d"%port,a[i])
			msent = msent +1 
		printm(msent,mreceived,ap)
		sys.exit(0)

	else:
		ho = "127.0.0.1"
		ad = (ho,parent)
		s.sendto("%d"%port,ad) 
		msent = msent + 1   	
	
""" socket is closed """
s.close()
