Memoria sobre la práctica 1 de Fundamentos de
los Sistemas Inteligentes.
Autores:
Itamar Rey Rodríguez
Ángel Hernández Ojeda
En nuestro programa, hemos añadido diferentes variables y formas de visualizar en
la ejecución del mismo toda la información que necesitamos analizar. Gracias a
esto, hemos podido hacer una tabla comparativa de los diferentes métodos de
búsqueda desarrollados en el propio programa.
A raíz de la gráfica comparativa que hemos hecho, se pueden ver claras diferencias.
En amplitud y profundidad la diferencia reside en el costo total del camino y en la
cantidad de nodos que se visitan. Como vemos, la búsqueda por profundidad puede
llegar a ser mucho menos eficiente si la solución del problema no se encuentra en
las primeras ramas del árbol de búsqueda.
Con Branch and Bound, sin embargo, se ve un resultado mucho más similar al que
obtenemos con la Amplitud. Tanto el costo total como los nodos visitados y
generados nos ofrecen un análisis igualitario, sin mayor diferencia destacable.
No obstante, si al Branch and Bound le añadimos una heurística(o subestimación),
somos capaces de mejorar muchísimo la eficacia del programa. Tanto en nodos
visitados como generados, se puede observar que el método con subestimación
tiene una mayor facilidad de encontrar la solución, buscando caminos cortos.
En conclusión, aprovechar una condición como la es la distancia entre el nodo inicial
y el final del camino resulta en unos mejores resultados. Aunque es cierto que la
heurística no siempre va a ser favorable, para nuestro problema se aplica de forma
muy adecuada.
