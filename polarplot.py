import matplotlib.pyplot as plt
import numpy as np

#sample data
theta = np.linspace(0, 2*np.pi, 100)
r = np.sin(3*theta)

#create a polar plot 
plt.polar(theta,r)
plt.title("Polar Plot Eample")
plt.show()