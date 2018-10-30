def f(x):
    return (x**2)-10
#probar con 3 rangos x0,x1 ; y0,y1; z0,z1

def Falsa(x0,x1):
    print("Usando de rango " +str(x0) + " y " +str(x1))
    for i in range(100):
        fx0=f(x0)
        fx1=f(x1)
        if(fx0*fx1>0):
            #Checa, si la multiplicación da arriba de 0 es porque o ambos son positivos, o ambos son negativos, entonces en ningún momento         te da la raíz
            print("No hay raíz en el rango dado")
            break
        xr=x0- ( (f(x0)*(x1-x0)) /(f(x1)-f(x0)))
        fxr=f(xr)
        if(fxr*fx1>0):
            x1=xr
        elif(fxr*fx0>0):
            x0=xr
        if(abs(fxr)<0.00000001):
            print("La raíz es "+str(xr))
            break
            
Falsa(3,3.2)
