# Metodo de Newton-Raphson:
En el método de Newton Raphson, tenemos una f(x), usaremos la derivada de f(x), para ayudarnos a calcular la siguiente x,
una vez tenemos esta f'(x), la fórmula es la siguiente:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=f'(x0)%3D%20%20%5Cfrac%7Bf(x0)%7D%7Bx0-xr%7D%20">

Despejando:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=x0-xr%3D%20%20%5Cfrac%7Bf(x0)%7D%7Bf'(x0)%7D%20">

Finalmente tenemos:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=xr%3Dx0-%20%5Cfrac%7Bf(x0)%7D%7Bf'(x0)%7D%20">

Elegimos una x0, el valor que sea, este será nuestro valor inicial.
Gracias a esta fórmula podremos calcular nuestra xr, una vez tengamos esta xr, debemos probarla en la función:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=f(xr)%3E0.0001">

Si f(xr) es mayor al error, entonces no puede ser un valor aceptado, en este caso, xr sería nuestra nueva x0, repetimos el proceso hasta encontrar un valor que se aproxime al esperado (en este caso, el 0).
