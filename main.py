# Importamos las bibliotecas necesarias
import string
import random

# Módulo para la generacion de contraseñas
def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
  # Creamos una lista vacía para almacenar los caracteres de la contraseña
  caracteres = list(string.ascii_lowercase)

  #Si se desea incluir mayusculas, las agregamos a la lista de caracteres
  if incluir_mayusculas:
    caracteres.extend(list(string.ascii_uppercase))

  if incluir_numeros:
    caracteres.extend(list(string.digits))

  if incluir_simbolos:
    caracteres.extend(list(string.punctuation))

  contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
  return contrasena

# Script principal para interactuar con el usuario

if __name__ == '__main__':
  longitud = int(input('Ingrese la longitud de la contraseña: '))
  incluir_mayusculas = input('Incluir mayúsculas (S/N): ').lower() == 's'
  incluir_numeros = input('Incluir numeros (S/N): ').lower() == 's'
  incluir_simbolos = input('Incluir símbolos (S/N): ').lower() == 's'
  contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)

print(f'Su contraseña es: {contrasena}')