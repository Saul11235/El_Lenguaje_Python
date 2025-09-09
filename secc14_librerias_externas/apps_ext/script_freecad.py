# ejemplo de Script para FreeCAD

import FreeCAD as App
import FreeCADGui as Gui
import Part
import random

# 1. Obtener o crear un documento
doc = App.ActiveDocument
if doc is None:
    doc = App.newDocument("Paralelepipedos")
else:
    # Limpiar todos los objetos del documento actual
    for obj in doc.Objects:
        doc.removeObject(obj.Name)

# 2. Crear 5 paralelepípedos con dimensiones y posiciones aleatorias
for i in range(5):
    # Dimensiones aleatorias entre 5 y 50 mm
    width = random.uniform(5, 50)
    height = random.uniform(5, 50)
    depth = random.uniform(5, 50)

    # Posición aleatoria en un rango determinado
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    z = random.uniform(0, 100)

    # Crear el cubo/paralelepípedo
    box = doc.addObject("Part::Box", f"Paralelepipedo_{i+1}")
    box.Length = width
    box.Width = depth
    box.Height = height

    # Establecer su posición
    box.Placement.Base = App.Vector(x, y, z)

# 3. Actualizar vista y recomputar
doc.recompute()
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()

print(" Se han creado 5 paralelepípedos aleatorios.")
