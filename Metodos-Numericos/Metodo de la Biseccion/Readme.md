# Metodo de la Biseccion:

El metodo de la biseccion funciona de la siguiente manera:

Para encontrar donde converge una funcion, damos un rango [x0,x1]. Probaremos ambas variables con nuestra funcion, si hay un cambio de signo entre ambos resultados, quiere decir que en dicho rango se encuentra la raiz que buscamos.
Hallamos una x intermedia, de la siguiente forma:

$$

x=(x0+x1)/2

$$

Probaremos la funcion en esta nueva x, si hay un cambio de signo entre x0 y x, este sera nuestro nuevo rango, sin embargo, si hay cambio entre x1 y x, el nuevo rango sera [x,x1]

Este es un metodo iterativo, iteraremos hasta que nuestro valor de f(x) nos de 0 un numero cercano. Entonces, esa es la respuesta final que daremos.
