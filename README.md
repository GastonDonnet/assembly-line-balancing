# Balanceo de lineas de ensamble con multiples productos y operarios

El proyecto cuenta con algoritmos en Python y modelos matemáticos programados en GAMS.

El código presentado es de autoría propia y forma parte de mi proyecto final de carrera (Ing. Industrial) en el que se tenia entre otras cosas balancear una linea de ensambles.

El problema presentado es de minimization de TC dado el numero de estaciones de trabajo.

Ademas de las restricciones típicas de un problema de balanceo de lineas de ensamble, estos algoritmos tuvieron en cuenta las siguientes

- Hay un numero dado de operarios, todas las tareas requieren 1 o mas operarios, si una tarea es asignado a una estación, esa estación tendrá que tener asignado por lo menos la cantidad de operarios que requiere la tarea.

- Hay 5 productos, al ser similares muchas tareas poseen un tiempo dependiente del producto en la linea por lo que se tendrán 5 tiempos por estación y 5 tiempos de ciclos de la linea.

## Notas

El modelo matemático en GAMS puede ser corrido usando la version de prueba que se baja desde la pagina oficial ya que el numero de variables y restricciones no excede las restricciones de licencia.
