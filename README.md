# Laboratorio Big O y Estructuras de Datos

Este repositorio acompaña la guía autónoma del laboratorio.

## Integrantes

- Fátima Esmeralda Calderón Rivas — 202401123
- Andrea Yamilette Aguilera Recinos — 202400664
- Otto Alexander Hernández Arévalo — 202400674

## Descripción del problema

Una universidad administra miles de estudiantes. Cada registro contiene
carnet, nombre, carrera, departamento y promedio. El sistema consulta
constantemente si un estudiante existe y, en algunos casos, necesita
recuperar todos sus datos a partir del carnet.

Este proyecto evalúa qué estructura de datos ofrece un comportamiento más
adecuado cuando la cantidad de registros crece, comparando la complejidad
teórica (Big O) con mediciones reales de tiempo sobre cinco estructuras:
`List`, `Set`, `Dictionary`, una lista enlazada y un árbol binario de
búsqueda (BST).

## Flujo
1. Ejecutar `python src/generar_datos.py`.
2. Subir `data/estudiantes.csv` al repositorio de GitHub.
3. Abrir el CSV en GitHub, elegir **Raw** y copiar la URL.
4. Pegar la URL en `src/main.py`.
5. Ejecutar `python src/main.py`.
6. Completar `resultados/resultados.md` con sus mediciones y conclusiones.

Adicionalmente, para probar la lista enlazada y el árbol binario de
búsqueda:

```
python src/probar_lista_enlazada.py
python src/probar_arbol_bst.py
```

> No sustituya las mediciones por valores inventados. Los tiempos cambian según el equipo.

## Estructura del proyecto

```
├── data/
│   └── estudiantes.csv
├── resultados/
│   └── resultados.md
├── src/
│   ├── generar_datos.py
│   ├── main.py
│   ├── lista_enlazada.py
│   ├── arbol_bst.py
│   ├── probar_lista_enlazada.py
│   └── probar_arbol_bst.py
└── README.md
```