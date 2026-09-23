"""
Prueba y medición de src/lista_enlazada.py
Tarea 2.2 - Integrante 2 (Estructuras de Datos Avanzadas)

Coloca este archivo dentro de la carpeta src/ y ejecútalo desde la raíz
del proyecto con:

    python src/probar_lista_enlazada.py
"""
import csv
import time
from pathlib import Path

from lista_enlazada import ListaEnlazada

BASE = Path(__file__).resolve().parent.parent
RUTA_CSV = BASE / "data" / "estudiantes.csv"

# 1. Cargar los estudiantes desde el CSV ya generado y publicado
with RUTA_CSV.open(encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    estudiantes = list(lector)

print(f"OK: {len(estudiantes):,} registros cargados desde CSV\n")

# 2. Construir la lista enlazada con una muestra (10,000 para no tardar demasiado)
MUESTRA = 10_000
sub_estudiantes = estudiantes[:MUESTRA]

inicio = time.perf_counter()
lista = ListaEnlazada()
for estudiante in sub_estudiantes:
    lista.insertar_inicio(estudiante)
fin = time.perf_counter()
print(f"Construcción (insertar_inicio x {MUESTRA:,}): {fin - inicio:.6f} s")
print("  -> Cada inserción es O(1); el tiempo total crece de forma lineal")
print("     solo porque repetimos la operación MUESTRA veces.\n")

# 3. Buscar un carnet que quedó CERCA DEL FINAL de la lista enlazada
# (como insertamos al inicio, el primer estudiante insertado terminó al final)
carnet_al_final = sub_estudiantes[0]["carnet"]
inicio = time.perf_counter()
resultado = lista.buscar(carnet_al_final)
fin = time.perf_counter()
print(f"Buscar carnet cercano al final   ({carnet_al_final}): "
      f"{fin - inicio:.6f} s -> encontrado: {resultado is not None}")

# 4. Buscar un carnet que quedó CERCA DEL INICIO de la lista enlazada
carnet_al_inicio = sub_estudiantes[-1]["carnet"]
inicio = time.perf_counter()
resultado = lista.buscar(carnet_al_inicio)
fin = time.perf_counter()
print(f"Buscar carnet cercano al inicio  ({carnet_al_inicio}): "
      f"{fin - inicio:.6f} s -> encontrado: {resultado is not None}")

# 5. Buscar un carnet que NO existe (peor caso real - sirve también para Tarea 2.4)
inicio = time.perf_counter()
resultado = lista.buscar("EST999999")
fin = time.perf_counter()
print(f"Buscar carnet inexistente        (EST999999): "
      f"{fin - inicio:.6f} s -> encontrado: {resultado is not None}")

print("\nConclusión esperada: la búsqueda cercana al inicio de la lista")
print("(que en la memoria es el ULTIMO insertado) debe ser mucho más rápida")
print("que la búsqueda cercana al final o la del carnet inexistente, porque")
print("buscar() recorre nodo por nodo: O(n) en el peor caso.")