import numpy as np 
import matplotlib.pyplot as plt  

#cmputing cordinates
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plottting graph
plt.plot(x, y) 
plt.show() 
