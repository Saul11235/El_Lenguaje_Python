# Script para blender
# este script debe ser ejecutado en la consola de Blender
# define 50 poliedros rectangulares aleatorios


import bpy
import random

# Limpiando escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Cantidad de cubos a crear
cantidad_cubos = 50

# Rango de posiciones aleatorias
rango_posicion = 10  # cubos se ubicarán entre -10 y 10 en x, y, z

for i in range(cantidad_cubos):
    # Dimensiones aleatorias
    width = random.uniform(0.5, 3.0)
    height = random.uniform(0.5, 3.0)
    depth = random.uniform(0.5, 3.0)
    
    # Posición aleatoria
    x = random.uniform(-rango_posicion, rango_posicion)
    y = random.uniform(-rango_posicion, rango_posicion)
    z = random.uniform(-rango_posicion, rango_posicion)
    
    # Crear cubo base
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))
    
    # Obtener el cubo recién creado
    cubo = bpy.context.active_object
    cubo.name = f"Cubo_{i+1}"
    
    # Ajustar escala para modificar dimensiones
    cubo.scale = (width / 2, depth / 2, height / 2)
    
    print(f"{cubo.name} → Dimensiones: {width:.2f}, {depth:.2f}, {height:.2f} | Posición: {x:.2f}, {y:.2f}, {z:.2f}")
