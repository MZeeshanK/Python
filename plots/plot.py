import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]

plt.figure(figsize=(3,5))
plt.title('My Graph',fontsize=16, color="blue")
plt.xlabel('Days',fontsize=8,color='blue')
plt.ylabel('Sales',fontsize=8,color='blue')
plt.plot(x,y,color='red',linestyle='dashed',lw=10, label='Sales Graph')
plt.legend()
plt.show()
