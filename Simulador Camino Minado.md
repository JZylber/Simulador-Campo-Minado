# Simulador de Camino Minado
## Corporación A.C.M.E. 

### Origen
En el marco de las acciones de uno de nuestros principales clientes, *Wile E. Coyote*, nuestra corporación se ve obligada a diseñar un sistema de detección, desactivación y recuperación de minas. Esto se debe a que dicho cliente, con el objetivo de cazar a cierto ave no voladora, ha minado una infinidad de caminos, muchos de ellos usados por nuestra empresa. Es por eso que para evitar mayores pérdidas materiales a nuestra flota de transporte, hemos decidido limpiar de minas los caminos recorridos por nuestros camiones. A su vez, la recuperación del material explosivo nos permite revenderlo al cliente en cuestión, agigantando nuestras ganancias.

En este contexto, la corporación A.C.M.E. encarga el creado un simulador de limpieza de campo minado, como prueba de concepto antes de desarrollar una prueba de campo.

### Especificación del programa

#### Caminos
Los caminos se dividen en sectores llamados baldosas, y estos pueden contener **solo una** de las siguientes opciones:
- "B": Una baldosa sin carga explosiva.
- "M": Una mina armada, que explota si es recorrida.
- "D": Una mina desactivada, que es recuperada al recorrerla.

#### Detección
El sistema de detección es un sistema aéreo que sobrevuela al camino e identifica las posiciones en las que se encuentran minas armadas.

#### Desactivación/Neutralización
El sistema de neutralización toma las minas detectadas por el sistema anterior y las convierte en minas desactivadas.

#### Recuperación
Un vehículo recorre el camino en cuestión. Si se encuentra con una mina desactivada, debe recuperarla. Al finalizar su recorrida, debe hacer un registro de cuantas minas recuperó. En cambio, si se encuentra con una mina activada, debe explotar y **el simulador debe terminar abruptamente**.
