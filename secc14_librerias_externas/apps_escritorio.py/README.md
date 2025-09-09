# convirtiendo un script a una app de escritorio

En este ejemplo compilaremos un **archivo.pyw** con  codigo python
a un ejecutable **programa.exe** para su distribución.

**Nota 1:** en este caso el código no estará protegido.

**Nota 2:**  los archivos .pyw no muestran la consola, esto es estpetico en apps de escritorio

## instalar pyinstaller

    pip install pyinstaller               

## compilar a .exe

    pyinstaller --onefile archivo.py      


