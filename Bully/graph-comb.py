# code for plotting performance measurement
import matplotlib.pyplot as plt


rtt=[28,26,24,22,20,18,16,14,12,10]
p=[1,2,3,4,5,6,7,8,9,10]
bx=plt.subplot(111)
bx.plot(p,rtt,linestyle='--',marker='o',linewidth=1.5)
bx.grid()
bx.set_xlim(1,12)
bx.set_ylim(1,35)
bx.set_title('Messages v/s ID',color='#000000',weight="bold",size="large")
bx.set_ylabel('Number of messages sent')
bx.set_xlabel('Process initiating the election')
bx.text(10.2,0.21,'Green -- = Heap\nBlue -- = Bully\nRed -- = Ring',bbox={'facecolor':'white','pad':10})

rtt=[13,13,12,13,12,12,11,12,11,10]
p=[1,2,3,4,5,6,7,8,9,10]
bx.plot(p,rtt,linestyle='--',marker='o',linewidth=1.5)

rtt=[29,28,27,26,25,24,23,22,21,20]
p=[1,2,3,4,5,6,7,8,9,10]
bx.plot(p,rtt,linestyle='--',marker='o',linewidth=1.5)

plt.savefig('graph-comb-all.png')
