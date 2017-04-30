
from socket import *
import sys
import os
import math
import time



""" creates a datagram(UDP) socket with ipv4 addressing """
s=socket(AF_INET,SOCK_DGRAM)

""" stores the number of command line arguments """
no_of_arg=len(sys.argv)
port_no = 6000
""" MSS stands for maximum segment size, file can be of any file-format, but should be in the current directory  """
if(no_of_arg!=2):
    print "expected format python %s <number of hosts> "%(sys.argv[0])



else:
    host=[]
    """ addr is a list of the tuples (host_ip,port_no) """
    addr=[]
    port=[]
    start = 7002
    no_of_hosts=int(sys.argv[1])
    n = no_of_hosts
    """ Inputs host ips and port numbers one after the other """
    for i in range(no_of_hosts):
        #host.append(raw_input("Enter hostname %d " %i))
        host.append('127.0.0.1')
        port.append(raw_input("Enter port of %d th host " %i))
        port[i] = int(port[i])
        #num = 7000 + i +1
        #port.append(num)
        addr.append((host[i],port[i]))

    """ t0 stores the starting time of the file transfer to the servers """
    t0=time.time()
    
    # Sending no. of hosts
    for i in range(no_of_hosts):
    	s.sendto("%d"%n,addr[i])
    	
    # sending address of each hosts
    for i in range(no_of_hosts):
    	for j in range(no_of_hosts):
    		s.sendto(host[j],addr[i])
    		s.sendto("%d"%port[j],addr[i])
    		     	
    # sending the port number which conducts election
    for i in range(no_of_hosts):
    	s.sendto("%d"%start,addr[i])

	totals = 0
	totalr = 0
	s.settimeout(10.0)
    for i in range(no_of_hosts):
    	try:
    		data, address = s.recvfrom(1024)
    		totals = totals + int(data)
    	#data, address = s.recvfrom(1024)
    	#totalr = totalr + int(data)
    	except:
			print "1 node found down"

    print "Total messages sent  = ", totals    	
    #print "Total messages received  = ", totalr    	
s.close()    

"""
    # sending election message to each node
    for i in range(no_of_hosts):
    	if(port[i]>port_no):
        	s.sendto("%d"%port_no,addr[i])   	

    

    count =0
    maxn =0
    #print "Time out"
    s.settimeout(1.0)
    try:
    	for i in range(no_of_hosts):
        	num,add = s.recvfrom(1024)
        	print num
        	if(int(num)>maxn):
        		maxn = int(num)
        	count = count +1
      
    except:
		if(count==0):
			print "I am the leader"
			sys.exit(0);
	
	# Sending Highest election id to all nodes!
    for i in range(no_of_hosts):
		s.sendto("CMSG",addr[i])
		s.sendto("%d"%maxn,addr[i])
			     
"""
