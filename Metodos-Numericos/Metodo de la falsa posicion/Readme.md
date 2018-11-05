# Metodo de la falsa posición:
Este método es bastante parecido al de la bisección, lo único que cambia, es la forma de hallar la siguiente x, o xr.
Tenemos una f(x), definiremos un intervalo [x0,x1], para hallar la xr tenemos la siguiente fórmula.

<img src="http://chart.apis.google.com/chart?cht=tx&chl=%5Cfrac%7B(f(x1)-f(x0))%7D%7B(x1-x0)%7D%20%3D%20%20%5Cfrac%7B%20-f(x0)%7D%7B(xr-x0)%7D%20">

Despejando:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=xr-x0%3D%20%20%5Cfrac%7B%20-(fx0)(x1-x0)%7D%7B(f(x1)-f(x0))%7D%20%0A">

Tenemos finalmente:

<img src="http://chart.apis.google.com/chart?cht=tx&chl=xr%3D%20x0-%20%5Cfrac%7B%20(fx0)(x1-x0)%7D%7Bf(x1)-f(x0)%7D%20">

Una vez tengamos la xr, haremos lo mismo que en el método de la bisección, probaremos esta xr en la función, y si nos da un valor muy alejado del esperado, hallaremos el nuevo rango de la misma manera que en otro método.
