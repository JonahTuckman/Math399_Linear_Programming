import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, .1)
y = np.sin(np.power(x, 3))
plt.plot(x, y)
plt.show()
