import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
x1=[6,7,8,9,10]
y1=[2,3,5,7,11]
plt.plot(x,y,marker='o',linestyle='--',color='b',label='prime Number')
plt.plot(x1,y1,marker='o',linestyle='--',color='r',label='Number')
plt.xlabel('x Axis')
plt.ylabel('y Axis')
plt.title('prime numbers plot')
plt.legend()
plt.show()

