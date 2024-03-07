# <- Modelo booleano difuso ->

### Autores:

#

- Yonatan Jose Guerras C411
- Jose Miguel Perez Perez C411

#

El `modelo booleano difuso` es un enfoque que se utiliza en la `lógica difusa` y la `inteligencia artificial` para manejar la incertidumbre y la ambigüedad en la toma de decisiones. A diferencia de la `lógica booleana tradicional`, que solo permite valores de verdad (verdadero o falso), el modelo booleano difuso permite grados de verdad que pueden variar entre 0 y 1. Esto permite representar la incertidumbre y la ambigüedad de manera más precisa . Aunque retorna documentos mas precisos con respecto a la `query` del usuario , requiere mas cómputo para generar la base de datos correspondiente por lo que requiere mejor gestion de memoria y de los recursos en general

#

En este trabajo se implementó el modelo boleano difuso con una mejora extra en el cálculo del ranking de los documentos . En escencia se calcula la expresion  $\mu_{q,j} =1 - \Pi_{k_l\in q }(1 -\mu_{cc_i,j} )$ donde $\mu_{q,j}$ es el peso de peso de la query en el documento $d_j$ para suavizar las transiciones entre un documento malo para recomendar y uno bueno , a diferencia del modelo tradicional difuso en el que se utilizan las expresion 

* $\mu_{\overline{A}}(u) =1 -\mu_A$ 
* $\mu_{A \cup B}(u) =max(\mu_A(u),\mu_Bu)$
* $\mu_{A \cap B}(u)=min(\mu_A(u),\mu_Bu)$

La desventaja de la mejora anterior es que para calcular los vecotres referentes a los documentos de la query es necesario resolver un poblema NP con complejidad $2^n$ donde $n$ es la cantidad de términos en la query.

El término  $\mu_{i,j} =\Pi_{k_l\in d_j }(1-c_{i,l})$ , dado $c_{ij}=\frac{n_{i,j}}{ n_i + n_j - n_{i,j}}$ , y $n_i$ el número de documentos en los que aparece el término $i$ y además $n_{i,j}$ el número de documentos en los que aparece el término $i$ y $j$ , calcular el peso del término $k_l$ de la base de datos en el documento $j$. En el término $c_{ij}$ se calcula el grado de membresía de los término $i$ y $j$, que como ya dijimos es un valor entre $[0,1]$

En el directorio `src` se encuentra el script `tok.py` que `tokeniza` los documentos de entrada .

El script `core.py` hace el cálculo del la matriz que se utiliza para encontrar las `relaciones de membresía` entre palabras y documentos

El script `entry.py` somete a la query a un parser para estar seguros que la query esta correcta , ademas que tokeniza la misma

`nota:` Los `parentésis` en la query deben estar separados por espacios , en caso contrario el parser no permitirá dicha `query`

Luego esta el script `suggestion.py` que se encarga de determinar los documentos para la sugerencia de los mismos.

## Deficiencias

A este modelo le falto implementar el modelo estandar difuso de procesamiento de la query dado que no es capaz de calcular mas de 23 términos en una . Tampoco se utilizo lematizacion o tecnicas avanzadas de tokenizacion dado que dichas tecnicas usadas de manera basica , estropeaban la escructura semantica de la query
