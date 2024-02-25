import numpy as np
import matplotlib.pyplot as plt
g = 9.8

m = float(input("Ingrese el valor de peso: "))
c = float(input("Ingrese el valor de resistencia: "))

for t in range (0,15,1):
    v = g*m/c*(1-np.exp((-c/m)*t))
    print (t,v)

t = np.arange(0,50,.5)
v = g*m/c*(1-np.exp((-c/m)*t))

plt.plot(t,v)
plt.grid('on')
plt.axis
plt.grid
plt.plot(t,v,color = "red")
plt.xlabel("t")
plt.ylabel("v")
plt.title("v = g*m/c*(1-np.exp((-c/m)*t))")
plt.show()