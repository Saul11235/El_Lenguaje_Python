import  xml.etree.ElementTree as ET
from    xml.dom               import minidom

# Diccionario original
miDiccionario = {
    'hola'      : [1,   2,  3],
    'contenido' : [11, 22, 33]
}

# Función para convertir el diccionario a un árbol XML
def dict_a_xml(diccionario):
    root = ET.Element('root')
    for clave, valores in diccionario.items():
        item = ET.SubElement(root, clave)
        for valor in valores:
            elemento      = ET.SubElement(item, 'valor')
            elemento.text = str(valor)
    return root


# Codificar: dict → XML string
xml_root   = dict_a_xml(miDiccionario)
xml_str    = ET.tostring(xml_root, encoding='utf-8')
xml_pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")


# Escribir XML en archivo
with open('archivo.xml', 'w', encoding='utf-8') as file:
    file.write(xml_pretty)
    print('archivo.xml --> generado')


# Leer XML del archivo
with open('archivo.xml', 'r', encoding='utf-8') as file:
    xml_leido = file.read()
    print('archivo.xml --> leído')


# Decodificar: XML string → dict
def xml_a_dict(xml_str):
    tree      = ET.fromstring(xml_str)
    resultado = {}
    for elem in tree:
        resultado[elem.tag] = [int(sub.text) for sub in elem]
    return resultado

decodificado = xml_a_dict(xml_leido)


# Comparación
print("Original:", miDiccionario)
print("Recuperado:", decodificado)
