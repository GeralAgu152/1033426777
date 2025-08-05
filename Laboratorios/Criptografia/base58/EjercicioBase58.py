import string

# Definir el alfabeto base 54 (54 caracteres)
ALFABETO_BASE54 = string.ascii_letters + string.digits + '+/'

def EjercicioBase54():
    print('Ingrese Mensaje: ')
    mensaje = input()
    print('Cifrado Base54')
    mensajecifrado = cifrarBase54(mensaje)
    print(mensajecifrado)
    print('Descifrado Base54')
    mensajedescifrado = descifrarBase54(mensajecifrado)
    print(mensajedescifrado)
    return None

def cifrarBase54(textoplano):
    # Convertir el mensaje a bytes
    mensaje_bytes = textoplano.encode('utf-8')
    mensaje_numero = int.from_bytes(mensaje_bytes, 'big')  # Convertir los bytes a un número entero

    # Codificar el número en base 54
    texto_cifrado = ""
    while mensaje_numero > 0:
        texto_cifrado = ALFABETO_BASE54[mensaje_numero % 54] + texto_cifrado
        mensaje_numero //= 54
    
    return texto_cifrado

def descifrarBase54(textocifrado):
    # Decodificar el mensaje de base 54 a un número entero
    mensaje_numero = 0
    for i, char in enumerate(textocifrado):
        mensaje_numero = mensaje_numero * 54 + ALFABETO_BASE54.index(char)
    
    # Convertir el número de vuelta a bytes
    mensaje_bytes = mensaje_numero.to_bytes((mensaje_numero.bit_length() + 7) // 8, 'big')
    
    return mensaje_bytes.decode('utf-8')

if __name__ == '__main__':
    EjercicioBase54()
