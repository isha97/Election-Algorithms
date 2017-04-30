""" Implementation of the Server side of the Point to Multipoint file tranfer using Stop and Wait ARQ"""

from socket import *
import sys
import random
import time

def printm(a,b,add,p):
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

# receiving address of all hosts
for i in range(no_of_hosts):
	data,address=s.recvfrom(buff_size)
	h.append(data)
	data,address=s.recvfrom(buff_size)
	p.append(data)
	p[i] = int(p[i])
	a.append((h[i],p[i]))
	#print h[i]
	#print p[i] 

#receive leader starter
data,address=s.recvfrom(buff_size)
chk = int(data)

if(chk==port):
    time.sleep(2)
    # sending election message to each node
    for i in range(no_of_hosts):
         if(p[i]>port):
             s.sendto("%d"%port,a[i])
             msent = msent + 1
             #no_of_msgs = no_of_msgs +1   	

    count =0
    maxn =0
    #print "Time out"
    s.settimeout(1.0)
    try:
    	for i in range(no_of_hosts):
        	num,add = s.recvfrom(1024)
        	mreceived = mreceived + 1
        	#print num
        	if(int(num)>maxn):
        		maxn = int(num)
        	count = count +1
      
    except:
		if(count==0):
			print "I am the leader"
			for i in range(no_of_hosts):
				s.sendto("CMSG",a[i])
				s.sendto("%d"%port,a[i])
				msent = msent + 1
			printm(msent,mreceived,ap,port)
			sys.exit(0);
	
	# Sending Highest election id to all nodes!
    for i in range(no_of_hosts):
		s.sendto("CMSG",a[i])
		s.sendto("%d"%maxn,a[i])
		msent  = msent + 1


#"""
while(1==1):
	data,address = s.recvfrom(buff_size)
	mreceived = mreceived + 1
	#no_of_msgs = no_of_msgs +1
	if(data == "CMSG"):
		data,address = s.recvfrom(buff_size)
		if(int(data)>port):
			print "Leader Excepted as" , int(data)
			printm(msent,mreceived,ap,port)  
			sys.exit(0);
		elif(int(data)==port):
			for i in range(no_of_hosts):
				if(p[i]>port):
					s.sendto("DOUBLECHECK",a[i])
					s.sendto("%d"%port,a[i]) 
					msent = msent + 1
			count = 0
			maxn = 0
        	try:
        		for i in range(no_of_hosts):
        			data, address = recvfrom(buff_size)
        			mreceived = mreceived + 1
        			count = count +1
        			if(maxn<int(data)):
        				maxn = int(data)
        	except:
        		if(count ==0):
        			print "leader excepted as", int(data)
        
			"""for i in range(no_of_hosts):
				s.sendto("CMSG",a[i])
				s.sendto("%d"%maxn,a[i])
				msent = msent + 1 """
			printm(msent,mreceived,ap,port)
			sys.exit(0);

	elif(data == "DOUBLECHECK"):
		s.sendto("%d"%port,address)
		msent = msent + 1
		
	else:
		if(int(data)<port):
			s.sendto("%d"%port,address)
			msent = msent + 1
			#print address
			#print "Message sent"
	
""" socket is closed """
s.close()
