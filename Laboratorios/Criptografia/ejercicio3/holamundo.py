def holamundo():
    print('Ingrese su Nombre: ')
    nombre = input()
    print ('Ingrese su Apellido: ')
    apellido = input()
    datos = nombre + ' ' + apellido
    print('Hola Mundo ', datos)
    return None

if __name__ == '__main__':
    holamundo()