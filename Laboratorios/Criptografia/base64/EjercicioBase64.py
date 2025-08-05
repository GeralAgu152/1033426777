import base64

def EjercicioBase64():
    print('Ingrese Mnesaje: ')
    mensaje = input()
    print('Cifrado Base64')
    mensajecifrado = cifrarBase64(mensaje)
    print(mensajecifrado)
    print('Descifrado Base64')
    mensajecifrado = descifrarBase64(mensajecifrado)
    print(mensajecifrado)
    return None

def cifrarBase64(textoplano):
    mensaje_bytes = textoplano.encode('utf-8')
    textocifrado = base64.b64encode(mensaje_bytes)
    return textocifrado.decode('utf-8')

def descifrarBase64(textocifrado):
    textoplano_bytes = base64.b64decode(textocifrado)
    return textoplano_bytes.decode('utf-8')
if __name__ == '__main__':
    EjercicioBase64()