import numpy as np
import matplotlib.pyplot as plt
import random

np.seterr(divide='ignore', invalid='ignore')

#Define the size of the electric field lines grid
N = 20
M = 25

#Set the x and y coordinates
x_coor = np.arange(0, M, 1)
y_coor = np.arange(0, N, 1)
x_coor, y_coor = np.meshgrid(x_coor, y_coor)

E_x = np.zeros((N, M))
E_y = np.zeros((N, M))

#Set the number of total charges to plot
nq = 3

#Create empty lists to store coordinates of charges
qq = [[], []] 
for dummy in range(nq): 
    q = random.choice([-1, 1])
    q_x, q_y = random.randrange(1, N), random.randrange(1, M)
    qq[0].append(q_y)
    qq[1].append(q_x)
    for i in range(N):
        for j in range(M):
            denom = ((i - q_x) ** 2 + (j - q_y) ** 2) ** 1.5
            if denom != 0: 
                E_x[i, j] += q * (j - q_y) / denom
                E_y[i, j] += q * (i - q_x) / denom


C = np.hypot(E_x, E_y)

E = (E_x ** 2 + E_y ** 2) ** .5
E_x = E_x / E
E_y = E_y / E


plt.figure(figsize=(12, 8))

#Plot charges
plt.plot(*qq, 'ms')
#Create 2D array
rr =plt.quiver(x_coor, y_coor, E_x, E_y, C, pivot='middle')

cbar = plt.colorbar()
cbar.ax.set_ylabel('Magnitude')

#Label graph
plt.title('Electric Field Lines in Python')
plt.axis('equal')
plt.axis('off')
plt.show()
