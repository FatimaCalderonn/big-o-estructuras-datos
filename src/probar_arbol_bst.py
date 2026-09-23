"""
Prueba y medición de src/arbol_bst.py
Tarea 2.3 y 2.4 - Integrante 2 (Estructuras de Datos Avanzadas)

Coloca este archivo dentro de la carpeta src/ y ejecútalo desde la raíz
del proyecto con:

    python src/probar_arbol_bst.py
"""
import csv
import random
import sys
import time
from pathlib import Path

from arbol_bst import ArbolBST

BASE = Path(__file__).resolve().parent.parent
RUTA_CSV = BASE / "data" / "estudiantes.csv"

with RUTA_CSV.open(encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    estudiantes = list(lector)

print(f"OK: {len(estudiantes):,} registros cargados desde CSV\n")

MUESTRA = 3_000
muestra_ordenada = estudiantes[:MUESTRA].copy()  # los carnets ya vienen ordenados

# ---------------------------------------------------------------------------
# 1. Árbol SIN mezclar -> demuestra el caso degenerado (para la Tarea 2.3)
# ---------------------------------------------------------------------------
print("== Árbol SIN random.shuffle (carnets ya ordenados) ==")
sys.setrecursionlimit(10_000)  # subimos el límite solo para poder observar el problema
arbol_degenerado = ArbolBST()
try:
    inicio = time.perf_counter()
    for estudiante in muestra_ordenada:
        arbol_degenerado.insertar(estudiante)
    fin = time.perf_counter()
    print(f"Construcción ({MUESTRA:,} nodos ordenados): {fin - inicio:.6f} s")

    carnet_buscado = muestra_ordenada[-1]["carnet"]
    inicio = time.perf_counter()
    resultado = arbol_degenerado.buscar(carnet_buscado)
    fin = time.perf_counter()
    print(f"Buscar último carnet insertado ({carnet_buscado}): "
          f"{fin - inicio:.6f} s -> encontrado: {resultado is not None}")
    print("  -> El árbol quedó como una lista: cada nodo solo tiene hijo derecho.")
    print("     La búsqueda se comporta como O(n), no como O(log n).\n")
except RecursionError:
    print("RecursionError: el árbol se degeneró tanto (una rama de profundidad")
    print(f"{MUESTRA:,}) que Python no pudo seguir insertando de forma recursiva.")
    print("Esto EN SÍ MISMO es evidencia de por qué un BST sin balanceo es")
    print("peligroso con datos ya ordenados.\n")

# ---------------------------------------------------------------------------
# 2. Árbol CON random.shuffle -> el que pide la Tarea 2.3
# ---------------------------------------------------------------------------
print("== Árbol CON random.shuffle (orden aleatorio antes de insertar) ==")
muestra_mezclada = estudiantes[:MUESTRA].copy()
random.shuffle(muestra_mezclada)

arbol = ArbolBST()
inicio = time.perf_counter()
for estudiante in muestra_mezclada:
    arbol.insertar(estudiante)
fin = time.perf_counter()
print(f"Construcción ({MUESTRA:,} nodos mezclados): {fin - inicio:.6f} s")

carnet_existente = muestra_mezclada[-1]["carnet"]
inicio = time.perf_counter()
resultado = arbol.buscar(carnet_existente)
fin = time.perf_counter()
print(f"Buscar carnet existente ({carnet_existente}): "
      f"{fin - inicio:.6f} s -> encontrado: {resultado is not None}")

# ---------------------------------------------------------------------------
# 3. Carnet inexistente (Tarea 2.4) -> peor caso real en este árbol
# ---------------------------------------------------------------------------
inicio = time.perf_counter()
resultado = arbol.buscar("EST999999")
fin = time.perf_counter()
print(f"Buscar carnet inexistente (EST999999): "
      f"{fin - inicio:.6f} s -> encontrado: {resultado is not None}")

print("\nConclusión esperada: con shuffle, la búsqueda debe sentirse mucho más")
print("rápida y estable que en el árbol degenerado, porque cada comparación")
print("descarta aproximadamente la mitad de las opciones restantes (~O(log n)).")
print("Sin embargo, este BST NO se autobalancea: con mala suerte al insertar,")
print("todavía podría degradarse. Por eso se dice 'se aproxima' a O(log n),")
print("no que lo garantice.")