import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def f(x):
    return 0*x + 1

Lx = np.pi
Ly = np.pi
N = 100
h = Lx/N

x = np.linspace(0, Lx, N+1)
y = np.linspace(0, Ly, N+1)

u = np.zeros((N+1, N+1))

u[-1, :] = f(x) # u(x, 1) 
u[:, 0] = 0 # u(0, y) 
u[0, :] = 0 # u(x, 0) 
u[:, -1] = 0 # u(1, y) 

iterations = 1000
for _ in tqdm(range(iterations)):
    for i in range(1, N):  
        for j in range(1, N):
            u[j, i] = (u[j+1, i] + u[j-1, i] + u[j, i+1] + u[j, i-1]) / 4

plt.contourf(x, y, u, 50, cmap = "viridis")
plt.colorbar()
plt.title("Laplaces likning 2D numerisk")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("Laplaces likning 2D numerisk")
plt.show()



