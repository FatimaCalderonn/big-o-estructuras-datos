# Resultados del laboratorio

## Integrantes
- Nombre / carnet: Fatima Esmeralda Calderon Rivas 202401123
- Nombre / carnet: Andrea Yamilette Aguilera Recinos 202400664
- Nombre / carnet: Otto Alexander Hernandez Arevalo 202400674

## URL RAW utilizada
https://raw.githubusercontent.com/FatimaCalderonn/big-o-estructuras-datos/refs/heads/main/data/estudiantes.csv

## Mediciones

| n | List O(n) | Set O(1) promedio | Dict O(1) promedio |
|---:|---:|---:|---:|
| 100 | | | |
| 1,000 | | | |
| 10,000 | | | |
| 50,000 | | | |
| 100,000 | | | |

## Lista enlazada y Árbol BST

### Lista enlazada (src/lista_enlazada.py)

Se insertaron 10,000 estudiantes con `insertar_inicio` (O(1) por inserción) y se
midieron tres búsquedas con `buscar` (O(n) en el peor caso):

| Búsqueda | Tiempo | Resultado |
|---|---:|---|
| Carnet cercano al inicio de la lista (último insertado) | 0.000002 s | Encontrado |
| Carnet cercano al final de la lista (primero insertado) | 0.000899 s | Encontrado |
| Carnet inexistente (EST999999) | 0.000694 s | No encontrado |

**Observación:** como `insertar_inicio` agrega cada nodo en la cabeza, el
elemento insertado más recientemente queda primero en la lista y el más
antiguo queda al final. Por eso buscar un carnet "viejo" (al final) es
notablemente más lento que buscar uno "reciente" (al inicio): `buscar()`
recorre los nodos uno por uno hasta encontrar coincidencia o llegar a
`None`. Buscar un carnet inexistente obliga a recorrer la lista completa,
confirmando el peor caso O(n).

### Árbol binario de búsqueda (src/arbol_bst.py)

Se probó con una muestra de 3,000 estudiantes, comparando insertar en el
orden original del CSV (carnets ya ordenados) contra insertar tras aplicar
`random.shuffle()`.

| Prueba | Sin shuffle (degenerado) | Con shuffle |
|---|---:|---:|
| Construcción (3,000 nodos) | 1.468545 s | 0.008036 s |
| Búsqueda de un carnet existente | 0.000427 s | 0.000007 s |
| Búsqueda de un carnet inexistente | — (no probado en este árbol) | 0.000006 s |

**Observación:** al insertar los carnets en su orden original (ya
ordenados), el árbol se degenera en una estructura equivalente a una lista
enlazada: cada nodo solo tiene hijo derecho. Esto hace que tanto la
búsqueda como la propia construcción se comporten como O(n) en vez de
O(log n) — de hecho la construcción resultó 183 veces más lenta.

Al mezclar la muestra con `random.shuffle()` antes de insertar, el árbol
queda razonablemente balanceado y tanto la búsqueda de un carnet existente
como la de uno inexistente (EST999999) toman un tiempo prácticamente
idéntico y mucho menor, evidenciando el comportamiento O(log n) esperado.

**Importante:** este BST no se autobalancea. El comportamiento O(log n)
depende del orden de inserción; con datos ya ordenados puede degradarse
hasta O(n), como se demostró arriba.

## Preguntas

1. ¿Por qué List crece aproximadamente de forma lineal?
   Porque `buscar_lista` compara el carnet contra cada elemento, uno por
   uno, hasta encontrarlo o llegar al final. No hay forma de "saltar"
   posiciones, así que el trabajo crece proporcionalmente a n: en
   promedio se revisan n/2 elementos, y en el peor caso, n.
2. ¿Por qué Set y Dict se comportan de forma distinta?
   Porque usan tablas hash: calculan la posición del carnet directamente
   en vez de recorrer los elementos en orden. Por eso su tiempo de
   búsqueda se mantiene casi constante (O(1) promedio) sin importar
   cuántos registros haya.
3. ¿Medir tiempo es lo mismo que demostrar Big O? Explique.
   No. El tiempo medido depende del CPU, la carga del sistema y otros
   factores externos, mientras que Big O describe cómo crece el número
   de operaciones en función de n, independientemente del hardware. Medir
   tiempo solo ayuda a observar una tendencia que respalda la teoría.
4. ¿Qué estructura elegiría para búsquedas por carnet y por qué?
   Un Dictionary, usando el carnet como llave: ofrece búsqueda O(1) en
   promedio y devuelve el registro completo del estudiante de inmediato,
   sin pasos adicionales.
5. ¿Qué cambia cuando el carnet buscado no existe?
   En List y en la lista enlazada, hay que recorrer toda la estructura
   para concluir que no existe (peor caso O(n) garantizado). En Set,
   Dict y en un BST balanceado, el costo de una búsqueda fallida sigue
   siendo bajo (O(1) o O(log n)): nuestras mediciones lo confirman,
   pues buscar EST999999 en el árbol mezclado tardó casi lo mismo
   (0.000006 s) que buscar un carnet existente (0.000007 s).

## Conclusión

Escriba entre 8 y 12 líneas.

[PENDIENTE - conclusión del equipo]