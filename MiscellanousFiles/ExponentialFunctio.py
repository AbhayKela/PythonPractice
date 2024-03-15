import matplotlib.pyplot as plt
import numpy as np

#Generate some data
x = np.linspace(-5,15,100)
y = np.exp(x)

#Create exponential funciton graph
fig, ax = plt.subplots()
ax.plot(x,y)

#Add labels and a title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Exponential Function Graph')

#shot the plot
plt.show()


