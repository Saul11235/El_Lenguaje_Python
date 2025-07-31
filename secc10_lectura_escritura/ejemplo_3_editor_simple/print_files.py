# probando codigo del enunciado

from os import listdir,path

def print_files():
    current_path = path.dirname(path.abspath( __file__ ))
    elements     = listdir(current_path)
    print('  \t'.join(elements)) 

# ejecutando funcion
if __name__=='__main__':
    print_files()

