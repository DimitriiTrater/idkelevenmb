from scipy.signal import square
import numpy as np
import matplotlib.pyplot as plt


f = 1.0
d = 5.0
s = 1000

t = np.linspace(0, d, int(s * d), endpoint=False)
r = square(2 * np.pi * f * t)

plt.plot(t, r)
plt.show()
