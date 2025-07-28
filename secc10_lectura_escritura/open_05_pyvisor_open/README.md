# Traducción de open.--doc--

Abre el archivo y devuelve un flujo. En caso de error, se lanza un error OSError.
El archivo es una cadena de texto o byte que indica el nombre (y la ruta si el archivo no se encuentra en el directorio de trabajo actual) del archivo que se va a abrir, o un descriptor de archivo entero del archivo que se va a encapsular. (Si se proporciona un descriptor de archivo, se cierra cuando se cierra el objeto de E/S devuelto, a menos que closefd se establezca en Falso).
El modo es una cadena opcional que especifica el modo en que se abre el archivo. Su valor predeterminado es 'r', que significa abrir para leer en modo texto. Otros valores comunes son 'w' para escribir (truncando el archivo si ya existe), 'x' para crear y escribir en un nuevo archivo, y 'a' para añadir (que en algunos sistemas Unix significa que todas las escrituras se añaden al final del archivo, independientemente de la posición de búsqueda actual). En modo texto, si no se especifica la codificación, la utilizada depende de la plataforma: se llama a locale.getencoding() para obtener la codificación regional actual. (Para leer y escribir bytes sin procesar, utilice el modo binario y deje la codificación sin especificar). Los modos disponibles son:

|Char | Significado                                                    |                   
|-----|----------------------------------------------------------------|
| 'r' | abre para lectura (predeterminado)                             |
| 'w' | abre para escritura, truncando el archivo primero              |
| 'x' | crea un nuevo archivo y lo abre para escritura                 |
| 'a' | abre para escritura, añadiendo al final del archivo si existe  |
| 'b' | modo binario                                                   |
| 't' | modo texto (predeterminado)                                    |
| '+' | abre un archivo de disco para actualizar (lectura y escritura) |

El modo predeterminado es 'rt' (abrir para leer texto). Para el acceso aleatorio binario, el modo 'w+b' abre y trunca el archivo a 0 bytes, mientras que 'r+b' lo abre sin truncarlo. El modo 'x' implica 'w' y genera un error `FileExistsError` si el archivo ya existe.
Python distingue entre archivos abiertos en modo binario y de texto, incluso cuando el sistema operativo subyacente no lo hace. Los archivos abiertos en modo binario (añadiendo 'b' al argumento de modo) devuelven el contenido como objetos bytes sin decodificación. En modo texto (predeterminado, o cuando se añade 't' al argumento de modo), el contenido del archivo se devuelve como cadenas, cuyos bytes se decodifican previamente utilizando una codificación dependiente de la plataforma o la codificación especificada, si se proporciona.
El búfer es un entero opcional que se utiliza para establecer la política de almacenamiento en búfer.
Pase 0 para desactivar el búfer (solo se permite en modo binario), 1 para seleccionar el búfer de línea (solo disponible en modo texto) y un entero > 1 para indicar el tamaño de un búfer de fragmentos de tamaño fijo. Cuando no se proporciona el argumento de búfer, la política de almacenamiento en búfer predeterminada funciona de la siguiente manera:

- Los archivos binarios se almacenan en búfer en fragmentos de tamaño fijo; el tamaño del búfer se elige mediante una heurística que intenta determinar el tamaño de bloque del dispositivo subyacente y recurre a `io.DEFAULT_BUFFER_SIZE`.
  En muchos sistemas, el búfer suele tener una longitud de 4096 u 8192 bytes.
- Los archivos de texto "interactivos" (archivos para los que isatty() devuelve "True") utilizan búfer de línea. Otros archivos de texto utilizan la política descrita anteriormente para archivos binarios.

"encoding" es el nombre de la codificación utilizada para decodificar o codificar el archivo. Solo debe usarse en modo texto. La codificación predeterminada depende de la plataforma, pero se puede pasar cualquier codificación compatible con Python. Consulte el módulo de códecs para ver la lista de codificaciones compatibles.
"errors" es una cadena opcional que especifica cómo se gestionarán los errores de codificación; este argumento no debe utilizarse en modo binario. Utilice "strict" para generar una excepción ValueError si hay un error de codificación (el valor predeterminado "Ninguno" tiene el mismo efecto) o "ignore" para ignorar los errores. (Tenga en cuenta que ignorar los errores de codificación puede provocar la pérdida de datos).
Consulte la documentación de codecs.register o ejecute "help(codecs.Codec)" para obtener una lista de las cadenas de error de codificación permitidas.
El salto de línea controla el funcionamiento de los saltos de línea universales (solo se aplica al modo texto). Puede ser Ninguno, '', '\n', '\r' y '\r\n'. Funciona de la siguiente manera:

- En la entrada, si el salto de línea es Ninguno, se habilita el modo de salto de línea universal. Las líneas de la entrada pueden terminar en '\n', '\r' o '\r\n', y estas se traducen a '\n' antes de devolverse al emisor. Si es '', se habilita el modo de salto de línea universal, pero los finales de línea se devuelven al emisor sin traducir. Si tiene alguno de los otros valores permitidos, las líneas de entrada solo terminan con la cadena dada, y el final de línea se devuelve al emisor sin traducir.
- En la salida, si el salto de línea es Ninguno, cualquier carácter '\n' escrito se traduce al separador de línea predeterminado del sistema, os.linesep. Si el salto de línea es '' o '\n', no se realiza ninguna traducción. Si la nueva línea es cualquiera de los otros valores legales, cualquier carácter '\n' escrito se traduce a la cadena dada.

Si closefd es Falso, el descriptor de archivo subyacente se mantendrá abierto al cerrar el archivo. Esto no funciona cuando se proporciona un nombre de archivo y debe ser Verdadero en ese caso.
Se puede usar un abridor personalizado pasando un invocable como *opener*. El descriptor de archivo subyacente para el archivo

# archivo -io.TextIOWrapper 

Capa basada en caracteres y líneas sobre un objeto BufferedIOBase, buffer.
La codificación indica el nombre de la codificación con la que se decodificará o codificará el flujo. Su valor predeterminado es locale.getencoding().
Los errores determinan la rigurosidad de la codificación y la decodificación (consulte help(codecs.Codec) o la documentación de codecs.register) y su valor predeterminado es "strict".
El salto de línea controla cómo se gestionan los finales de línea. Puede ser "Ninguno", "\n", "\r" y "\r\n". Funciona de la siguiente manera:

- En la entrada, si el salto de línea es "Ninguno", se habilita el modo de salto de línea universal. Las líneas de la entrada pueden terminar en "\n", "\r" o "\r\n", y estas se traducen a "\n" antes de devolverse al emisor. Si es "", se habilita el modo de salto de línea universal, pero los finales de línea se devuelven al emisor sin traducir. Si tiene alguno de los otros valores legales, las líneas de entrada solo terminan con la cadena dada, y el final de línea se devuelve al llamador sin traducir.
- En la salida, si newline es None, cualquier carácter '\n' escrito se traduce al separador de línea predeterminado del sistema, os.linesep. Si newline es '' o '\n', no se realiza la traducción. Si newline es cualquiera de los otros valores legales, cualquier carácter '\n' escrito se traduce a la cadena dada.

Si line_buffering es True, se implica una llamada a flush cuando una llamada a write contiene un carácter de nueva línea.


