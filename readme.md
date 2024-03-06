# <- Modelo booleano difuso ->


El `modelo booleano difuso` es un enfoque que se utiliza en la `lógica difusa` y la `inteligencia artificial` para manejar la incertidumbre y la ambigüedad en la toma de decisiones. A diferencia de la `lógica booleana tradicional`, que solo permite valores de verdad (verdadero o falso), el modelo booleano difuso permite grados de verdad que pueden variar entre 0 y 1. Esto permite representar la incertidumbre y la ambigüedad de manera más precisa . Aunque retorna documentos mas precisos con respecto a la `query` del usuario , requiere mas cómputo para generar la base de datos correspondiente por lo que requiere mejor gestion de memoria y de los recursos en general

# 

En este trabajo se implementó el modelo boleano difuso con una mejora extra en el cálculo del ranking de los documentos . En escencia se calcula la expresion < poner expresion > para suavizar las transiciones entre un documento con malo para recomendar y uno bueno , a diferencia del modelo tradicional difuso en el que se utilizan las expresion <poner expresiones>

La desventaja de la mejora anterior es que para calcular los vecotres referentes a los documentos de la query es necesario resolver un poblema NP con complejidad $2^n$ donde $n$ es la cantidad de términos en la query.

En el directorio `src` se encuentra el script `tok.py` que `tokeniza` los documentos de entrada .

El script `core.py` hace el cálculo del la matriz que se utiliza para encontrar las `relaciones de membresía` entre palabras y documentos 

El script `entry.py` somete a la query a un parser para estar seguros que la query esta correcta , ademas que tokeniza la misma

`nota:` Los `parentésis` en la query deben estar separados por espacios , en caso contrario el parser no permitirá dicha `query`

Luego esta el script `suggestion.py` que se encarga de determinar los documentos para la sugerencia de los mismos.
