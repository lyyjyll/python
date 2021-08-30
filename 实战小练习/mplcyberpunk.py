from matplotlib import colors
import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np


#添加样式
plt.style.use('cyberpunk')

a = np.array([x for x in range(10000)])
x = 10*(16*np.sin(a)**3)
y = 10*(13*np.cos(a)-5*np.cos(2*a)-2*np.cos(3*a)-np.cos(4*a))


#plt.plot([i**2 for i in range(6)], marker = 'o')
#mplcyberpunk.add_glow_effects()

plt.plot(x,y)
plt.show()
