# Metodo de la Biseccion:

El m�todo de la bisecci�n funciona de la siguiente manera:

Para encontrar d�nde converge una funci�n, damos un rango [x0,x1]. Probaremos ambas variables con nuestra funci�n, si hay un cambio de signo entre ambos resultados, quiere decir que en dicho rango se encuentra la ra�z que buscamos.
Hallamos una x intermedia, de la siguiente forma:
$$
x=(x0+x1)/2
$$
Probaremos la funci�n en esta nueva x, si hay un cambio de signo entre x0 y x, este ser� nuestro nuevo rango, sin embargo, si hay cambio entre x1 y x, el nuevo rango ser� [x,x1]

Este es un m�todo iterativo, iteraremos hasta que nuestro valor de f(x) nos de 0 un n�mero cercano. Entonces, esa es la respuesta final que daremos.
