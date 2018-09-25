import math
def f(x):
    return (x**3)-(7*(x**2))+(14*x)-6
#probar con 3 rangos x0,x1 ; y0,y1; z0,z1

def Biseccion(x0,x1):
    print("Usando de rango " +str(x0) + " y " +str(x1))
    for i in range(100):
        fx0=f(x0)
        fx1=f(x1)
        if(fx0*fx1>0):
            #Checa, si la multiplicación da arriba de 0 es porque o ambos son positivos, o ambos son negativos, entonces en ningún momento         te da la raíz
            print("No hay raíz en el rango dado")
            break
        xr=(x1+x0)/2
        fxr=f(xr)
        if(fxr*fx1>0):
            x1=xr
        elif(fxr*fx0>0):
            x0=xr
        if(abs(fxr)<0.001):
            print("La raíz es "+str(xr))
            break
x0=0
x1=1
y0=1
y1=3.2
z0=3.2
z1=4
Biseccion(x0,x1)
Biseccion(y0,y1)
Biseccion(z0,z1)
