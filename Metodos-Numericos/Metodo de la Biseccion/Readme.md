# Metodo de la Biseccion:

El método de la bisección funciona de la siguiente manera:

Para encontrar dónde converge una función, damos un rango [x0,x1]. Probaremos ambas variables con nuestra función, si hay un cambio de signo entre ambos resultados, quiere decir que en dicho rango se encuentra la raíz que buscamos.
Hallamos una x intermedia, de la siguiente forma:
$$
x=(x0+x1)/2
$$
Probaremos la función en esta nueva x, si hay un cambio de signo entre x0 y x, este será nuestro nuevo rango, sin embargo, si hay cambio entre x1 y x, el nuevo rango será [x,x1]

Este es un método iterativo, iteraremos hasta que nuestro valor de f(x) nos de 0 un número cercano. Entonces, esa es la respuesta final que daremos.
