# Script de prueba en QGIS
# este script genera poligonos aleatorios dentro de 
# una capa de un plano

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsField,
    QgsFields,
    QgsRectangle,
    QgsPointXY
)
from PyQt5.QtCore import QVariant
import random

# 1. Limpiar el proyecto actual (elimina todas las capas)
QgsProject.instance().removeAllMapLayers()

# 2. Crear una capa vectorial temporal de tipo polígono
layer = QgsVectorLayer("Polygon?crs=EPSG:4326", "Rectángulos Aleatorios", "memory")
provider = layer.dataProvider()

# 3. Definir campos (opcional)
fields = QgsFields()
fields.append(QgsField("id", QVariant.Int))
fields.append(QgsField("ancho", QVariant.Double))
fields.append(QgsField("alto", QVariant.Double))
provider.addAttributes(fields)
layer.updateFields()

# 4. Crear 400 rectángulos aleatorios
features = []
for i in range(400):
    # Coordenadas aleatorias (latitud, longitud)
    x = random.uniform(-180, 180)     # Longitud
    y = random.uniform(-90, 90)       # Latitud
    width = random.uniform(1, 10)     # Grados
    height = random.uniform(1, 10)    # Grados

    # Crear rectángulo usando QgsRectangle
    rect = QgsRectangle(x, y, x + width, y + height)
    geom = QgsGeometry.fromRect(rect)

    # Crear feature
    feat = QgsFeature()
    feat.setGeometry(geom)
    feat.setAttributes([i + 1, width, height])
    features.append(feat)

# 5. Añadir los features a la capa
provider.addFeatures(features)
layer.updateExtents()

# 6. Añadir la capa al proyecto
QgsProject.instance().addMapLayer(layer)

print(" Se han generado 10 rectángulos aleatorios.")
