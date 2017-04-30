

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
	print "message sent" , a , "to", add
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
mreceived =0 
msent  = 0

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
print no_of_hosts

# receiving address of all hosts
for i in range(no_of_hosts):
	data,address=s.recvfrom(buff_size)
	h.append(data)
	data,address=s.recvfrom(buff_size)
	p.append(data)
	p[i] = int(p[i])
	a.append((h[i],p[i]))
	if(p[i]==port):
		mynum = i;
	#print h[i]
	#print p[i] 
#"""
time.sleep(10)
if(port==p[9]):
	s.sendto("%d"%port,a[(mynum+1)%no_of_hosts])
	print "starting election"
	print "Sending number: " , port, "to" , (mynum+1)%no_of_hosts
	msent = msent + 1

while(1==1):
	#j = j+1
	#print j	
	data,address = s.recvfrom(buff_size)
	mreceived = mreceived + 1
	if(data=="CMSG"):
		print "Leader excepted as "
		data,address = s.recvfrom(buff_size)
		print int(data)
		printm(msent,mreceived,ap)
		sys.exit(0)
	
	elif(int(data)< port):
		s.sendto("%d"%port,a[(mynum+1)%no_of_hosts])
		msent = msent + 1
		print "Sending number: " , port, "to" , (mynum+1)%no_of_hosts 

	elif(int(data)>port):
		s.sendto(data,a[(mynum+1)%no_of_hosts])
		msent = msent + 1
		print "Sending number: " , int(data), "to" , (mynum+1)%no_of_hosts 

	else:
		#time.sleep(10)
		print "Sending CMSG"
		print no_of_hosts
		for k in range(no_of_hosts):
			s.sendto("CMSG",a[k])
			s.sendto("%d"%port,a[k])
			msent = msent + 1
			#print "sent message to", a[k]
		printm(msent,mreceived,ap)
		sys.exit(0);	 	

s.close()
