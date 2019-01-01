'''

  Install an external package:

  * https://code.visualstudio.com/docs/python/python-tutorial
  * python -m pip install matplotlib

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

# install maplotlib with 'python -m pip install matplotlib'

print(dir(np))