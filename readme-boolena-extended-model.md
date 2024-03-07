# Modelo Booleano Extendido

El modelo booleano extendido es una variante del modelo booleano difuso. Este agrega caracteristicas del modelo vectorial al modelo booleano para asi conseguir un mejor ranking en cuanto a que se puedo computar la similitud de un documento sin excluir demasiados de estos, de forma que algunos documentos que antes no se consideraban relevantes, ahora si lo seran.
El funcionamiento es el siguiente:

Dada una consulta $q = k_1 \land k_2$, se consideran el punto (1;1) en el plano y calculamos el complemento de la distancia del vector documento $d$, cuyas componentes seran los pesos de los terminos $k_1$ y $k_2$ en dicho documento. En el caso de que la consulta sea $k_1 \lor k_2$, se calcula la distancia al punto (0;0). Esto se explica debido a que estamos intentando maximizar la distancia al punto que hace falsa la expresion, dando asi una idea de la relevancia del documento con respecto a la consulta.

La distancia puede ser calculada siguiendo cualquier criterio, esto solo afectara el nivel sesgo del modelo a la hora de escoger que documento es relevante y cual no; dicho esto, la distancia se calcula usando las normas. Vale la pena aclarar que el modelo booleano extendido no obliga a usar la misma norma para una consulta completa, sino que se pueden combinar varias normas para modificar el resultado de la busqueda. Aunque hayan muchas menciones de esto que tengan relevancia, es un dato a tomar en cuenta.

Para ejecutar una consulta del tipo $q = k_1 \land k_2 \land \dots \land k_n$, la formula empleada seria:
<br>
$sim(q,d_j) = 1 - \sqrt[p]{\frac{(1 - x_1)^p + (1 - x_2)^p + \dots + (1 - x_n)^p}{n}}$
<br>
En el caso de que la consulta este compuesta por operadores or's, cada termino de la suma se sustituye por $x_i$ y no se considera el complemento:
<br>
$sim(q,d_j) =  \sqrt[p]{\frac{x_1^p + x_2^p + \dots + x_n^p}{n}}$
<br>
Cada $x_i$ representa el peso del termino i en el documento j.
Por ultimo, si una consulta es mixta, esto es que tiene ambos operadores, la similitud se calcula a traves de una combinacion de estas formulas. Ejemplo:
<br>
Para la consulta $k_1 \land k_2 \lor k_3$, la similitud seria:
<br>
$sim(q,d_j) = 1 - \sqrt[p]{\frac{(1 - \sqrt[p]{\frac{x_1^p + x_2^p}{2}})^p + x_3^p}{2}}$
