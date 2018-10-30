import math
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1-(  (400/(9.81*(A(x)**3))) * B(x))
def A(x):
    return 3*x + ((x**2)/2)
def B(x):
    return 3+x

def Grafico():
    #Elegir valores iniciales x0 y x1
    #Donde haya un cambio de signo
    xarray=np.linspace(1,10,100)
    yarray=np.zeros(100)

    for i in range(100):
        yarray[i]=f(xarray[i])
    plt.plot(xarray,yarray)
    plt.grid()