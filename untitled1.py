import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
plt.style.use('dark_background')
 
fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)
 
#Wave speed
c = 1
piw = np.exp
z= np.pi


 
#x axis
x0 = np.linspace(-pi/2,pi/2,1000)
 
#Initial time
t0 = 0
 
#Time increment
dt = 0.01
 
def phi(x):
    return np.cos(x)**2
 
#Wave
def u(x,t): 
    
    return  5*phi(6*z*t-2*z*x)-(5/2)
 
a = []
 
for i in range(500):
    value = u(x0,t0)
    t0 = t0 + dt
    a.append(value)
 
k = 0
def animate(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0,x,color='cyan')
    plt.grid(True)
    plt.ylim([-5,5])
    plt.xlim([0,2.2])
     
anim = animation.FuncAnimation(fig,animate,frames=360,interval=20)
plt.show()