from matplotlib import pyplot as plt
weekdays=['mon','tues','wed','thurs','fri']

office=[5,8,7.5,6,5.5]
sleep=[8,7,6,6.5,7.5]
eat=[2,3,4,1,2]
binge=[2,1,3,4,1]

plt.plot([],[],color='b',label='office',linewidth=2)
plt.plot([],[],color='g',label='sleep',linewidth=3)
plt.plot([],[],color='y',label='eat',linewidth=4)
plt.plot([],[],color='r',label='binge',linewidth=5)

plt.stackplot(weekdays,office,sleep,eat,binge, colors=['b','g','y','r'])
plt.title('Activity Monitor Chart')
plt.xlabel('Days')
plt.ylabel('No. of hours spent')
plt.legend()
plt.show()