import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D

vis_filename = "Desktop\\accelerometer\\Acc_202012101759.csv"

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax2 = ax.twinx()

plotcolors=['red', 'blue', 'green', 'orange','magenta', 'goldenrod']

#data_Acc=int(response[2])
#data_totalSensors=int(response[3])
#print(data_THSensors)

file=open(vis_filename,"r")

header = file.readline()

data_t=[]
data_x=[]
data_y=[]
data_z=[]
RH_lines=[]
temp_lines=[]

while True:

   line = file.readline()

   if line == "\n":
      continue

   parts = line.split(",")

   print(parts)

   if len(parts) == 1:
      break

   data_t.append(float(parts[0].strip()))
    
   data_x.append(float(parts[1].strip()))
   data_y.append(float(parts[2].strip()))
   data_z.append(float(parts[3].strip()))

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
plt.show() 
ser.close