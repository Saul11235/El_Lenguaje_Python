# compilando de C a DLL

En este caso hemos compilado el archivo de ejemplo
C hacia DLL

                                             
    gcc -shared -o milib.dll -fPIC milib.c   
                                             

en este caso estamos usando gcc la coleccion de compiladores
GNU, y convertimos el archivo milib.c hacia milib.dll
