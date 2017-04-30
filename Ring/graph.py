# code for plotting performance measurement
import matplotlib.pyplot as plt


rtt=[29,28,27,26,25,24,23,22,21,20]
p=[1,2,3,4,5,6,7,8,9,10]
bx=plt.subplot(111)
bx.plot(p,rtt,linestyle='--',marker='o',linewidth=1.5)
bx.grid()
bx.set_xlim(1,12)
bx.set_ylim(1,35)
bx.set_title('Messages v/s ID',color='#000000',weight="bold",size="large")
bx.set_ylabel('Number of messages sent')
bx.set_xlabel('Process initiating the election')
#bx.text(2,0.34,'Green -- = With Memory Manager\nBlue -- = Without Memory Manager\n',bbox={'facecolor':'white','pad':10})

"""p=[2,4,6,8,10,12]
rtt=[0.04,0.08,0.11,0.14,0.18,0.22]
bx.plot(p,rtt,linestyle='--',marker='o',linewidth=1.5)
"""
plt.savefig('graph.png')
