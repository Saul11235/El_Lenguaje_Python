# Ejemplo usando pyvisor
#
# pip install pyvisor
#

# 
# En este ejemplo analizaremos el objeto generado de la funcion open
#


from pyVisor import visor       

file=open("file","w")

v=visor(file,"file")      

v.run()    
