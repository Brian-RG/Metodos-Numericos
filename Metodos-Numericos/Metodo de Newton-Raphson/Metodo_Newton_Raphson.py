#f'(x0)= f(x0)/x0-xr
#x0-xr=f(x0)/f'(x0)
#xr=x0-f(x0)/f'(x0)
def g(x):
    return (x**4)-(8.6*(x**3))-(35.51*(x**2))+(464*x)-998.46

def gprima(x):
    return (4*(x**3))-(25.8*(x**2))-(71.02*x)+464

def Newton(x0):
    for e in range(100):
        xr=x0-(g(x0)/gprima(x0))
        if(abs(g(xr))<0.0001):
            print("La raíz es " + str(xr))
            break
        x0=xr
Newton(7)
