# ================================================
# Tarea Semana 7 - Introducción a Python
# Asignatura: Desarrollo de Algoritmos
# Profesor: Patricio Balboa
# Nombre: Edwin Rios
# Fecha: 22 de abril, 2025
# ================================================

# Objetivo: Escribir un programa que use entrada/salida,
# variables, operadores matemáticos y condicionales.

# Paso 1: Solicitar el nombre del usuario
# Usa input() para pedirlo y guárdalo en una variable llamada 'nombre'

nombre = str(input('Ingresa tu nombre: '))

# Paso 2: Saludar al usuario usando print()

print('hola', nombre)

# Paso 3: Pedir la edad del usuario y convertirla a entero

edad = int(input('ingresar edad: '))

# Paso 4: Calcular en qué año nació (asume año actual = 2025)

año_nacimiento = 2025 - edad
print(año_nacimiento)

# Paso 5: Mostrar si es mayor o menor de edad usando if / else

if edad >= 18:
    print(f'{nombre} es mayor de edad')
else:
    print(f'{nombre} no es mayor de edad el')

# Agrega comentarios donde sea necesario para explicar tu código
# Asegúrate de que el código esté ordenado e indentado correctamente