import serial
import re
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax2 = ax.twinx()

plotcolors=['red', 'blue', 'green', 'orange','magenta', 'goldenrod']
ser=serial.Serial('COM3', timeout=10)
print(ser)

now=datetime.now()
datestring=now.strftime("%Y%m%d%H%M")

val=ser.readline().decode()
response=val.split(" ")
#data_Acc=int(response[2])
#data_totalSensors=int(response[3])
#print(data_THSensors)

filename="Desktop\\accelerometer\\Acc_"+datestring+".csv"
print(filename)
file=open(filename,"a")
outstring='time(s), x(g), y(g), z(g)\n'
#for i in range(3):
#    outstring+=' temp(C), RH(%),'
#outstring+='\n'
file.write(outstring)
file.close()
    


data_t=[]
data_x=[]
data_y=[]
data_z=[]
RH_lines=[]
temp_lines=[]

while True:

    val=ser.readline().decode()

    print(val)
    response=val.split(" ")
 #   for  i in range(len(response)):
 #       print(i, response[i])
    data_t.append(float(response[1])/60)
    
    data_x.append(float(response[3]))
    data_y.append(float(response[5]))
    data_z.append(float(response[7]))
 #   for i in range(data_THSensors):
 #       data_temp[i].append(float(response[5+i*5]))
 #       data_RH[i].append(float(response[7+i*5]))
 #       print(i)
 #      print(data_temp[i])
#    for i in range(data_THSensors,data_totalSensors):
 #       print(data_THSensors*5+5+(i-data_THSensors)*2)

 #       data_temp[i].append(float(response[data_THSensors*5+4+(i-data_THSensors)*2]))
    file=open(filename,"a")
    outstring=response[1]+', '+response[3]+', '+response[5]+', '+response[7]+'\n'
 #   for i in range(data_THSensors):
 #           outstring=outstring+', '+response[5+i*5]+', '+response[7+i*5]
 #   for i in range(data_THSensors,data_totalSensors):
 #           outstring=outstring+', '+response[data_THSensors*5+5+(i-data_THSensors)*2]
 #   outstring+='\n'    
    file.write(outstring)
    file.close()
   # Draw x and y lists
    ax.clear()
#    ax2.clear()
#    for i in range(data_totalSensors):
 #       ax.plot(data_t, data_temp[i],linestyle='-',color=plotcolors[i],label='Temp '+ str(i+1))
 #   for i in range(data_THSensors):    
 #       ax2.plot(data_t,data_x,linestyle='--',color=plotcolors[i],label='RH '+str(i+1))
    #plt.ylabel('Temperature (deg C)')
    #plt.xlabel('Time (min)')
    ax.plot(data_t,data_x,linestyle='-',color=plotcolors[0],label="X")
    ax.plot(data_t,data_y,linestyle='-',color=plotcolors[1],label="Y")
    ax.plot(data_t,data_z,linestyle='-',color=plotcolors[2],label="Z")
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel("Acceleration (g)")
  #  ax2.set_ylabel('RH (%)')
   #ax.legend([Line2D([0],[0],linestyle='-'),Line2D([0],[0],linestyle='--')],['Temp','RH'],loc='upper left')
    #ax.legend(temp_lines)
   # ax.legend(loc='upper left')
    #ax2.legend(loc='lower left')
    ax.set(ylim=(-5,5))
#    ax2.set(ylim=(-5,5))
# Set up plot to call animate() function periodically
    #ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.pause(.02)
plt.show() 
ser.close