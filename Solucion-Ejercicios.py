# Condicionales:

# Sistema de clasificación de rendimiento: Solicita al usuario su nota (0-20) y su asistencia (%). Si la nota es mayor o igual a 11 y la asistencia es mayor o igual al 70%, se aprueba. De lo contrario, se desaprueba. Además, otorga menciones especiales para notas mayores a 17 con asistencia completa.


# Solución:

nota = int(input("Cual es tu nota del 0 al 20?: "))
asistencia = int(input("Cual es el porcentaje de tu asistencia?: "))

if nota >= 11 and asistencia >= 70:
    print("Estas Aprobado")
    if nota > 17 and asistencia == 100:
        print("Mención Especial")
else:
    print("Desaprobado")

# Validación de acceso: Solicita usuario, contraseña y rol (admin, editor, visitante). Verifica si las credenciales son válidas y muestra los permisos disponibles según el rol. Usa múltiples condicionales y lógica anidada.

# Solución:

usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")

if usuario == "admin" and contrasena == "1234":
    print("Acceso Permitido")
    rol = input("Ingresa tu rol, (admin, editor, visitante): ").lower()
    if rol == "admin":
        print("Acceso Total")
    elif rol == "editor":
        print("Puedes Editar")
    elif rol == "visitante":
        print("Solo Puedes Ver")
    else:
        print("Rol No Valido")
else:
    print("Acceso Denegado")

# Verificación de año bisiesto y edad legal: Pide el año de nacimiento y determina si es bisiesto. Luego calcula la edad del usuario y verifica si es mayor de edad (18+).

# Solución:

nacimiento = int(input("En que año naciste?: "))
anio_actual = 2026
edad = anio_actual - nacimiento

if (nacimiento % 4 == 0 and nacimiento % 100 != 0) or (nacimiento % 400 == 0):
    print("Es Bisiesto")
else:
    print("No Es Bisiesto")

if edad >= 18:
    print("Eres Mayor de Edad")
else:
    print("Eres Menor de Edad")

# Clasificación de productos: Pide nombre, precio y categoría (tecnología, alimentos, ropa). Dependiendo de la categoría y precio, aplica diferentes tipos de impuestos y clasificaciones (lujo, básico, etc.)

# Solución:

producto = input("Cual es el nombre del producto?: ")
precio = float(input("Cual es el precio?: "))
categoria = input("Cual es la categoria del producto?: ").lower()

if categoria == "tecnologia":
    if precio > 3000:
        print(f"{producto} Es un producto de lujo")
    else:
        print(f"{producto} Es un producto basico")
elif categoria == "alimentos":
    if precio >= 400:
        print(f"{producto} tiene un impuesto alto")
    else:
        print(f"{producto} tiene un impuesto bajo")
elif categoria == "ropa":
    if precio >= 500:
        print(f"{producto} Es Ropa de Lujo")
    else:
        print(f"{producto} Es Ropa Basica")
else:
    print("Categoria Incorrecta")

# Suma condicional de múltiplos: Pide un número N y suma solo los múltiplos de 3 o 5 hasta N. Muestra la suma y los múltiplos encontrados.

# Solución:

num = int(input("Introduce un número: "))
suma = 0

for numero in range(1, num + 1):
    if numero % 3 == 0 or numero % 5 == 0:
        print(numero)
        suma += numero

print(f"La suma total es: {suma}")

# Tablas cruzadas: Genera la tabla de multiplicar del 1 al 12 para los números del 1 al 10. Imprime cada tabla en bloques separados.

# Solución:

for tabla in range(1, 10 + 1):
    print(f"Tabla del {tabla}")
    for number in range(1, 12 + 1):
        resultado = tabla * number
        print(f"{tabla} x {number} = {resultado}")

# Contador de dígitos pares e impares: Solicita un número entero largo, y con un bucle determina cuántos dígitos son pares y cuántos impares.

# Solución:

numero = input("Ingresa un número: ")
pares = 0
impares = 0

for digito in numero:
    digit = int(digito)
    if digit % 2 == 0:
        print("Es un número par")
        pares += 1
    else:
        print("Es un número impar")
        impares += 1
print(f"Números Pares: {pares} \nNúmeros Impares: {impares}")

# Números primos dentro de un rango definido: Pide al usuario un número inicial y uno final. Luego, muestra todos los números primos dentro de ese rango usando una función que los verifique.

# Solución:

num_inicial = int(input("Introduce un Número: "))
num_final = int(input("Introduce otro Número: "))

for numero in range(num_inicial, num_final + 1):
    if numero < 2:
        continue
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero)

# Búsqueda avanzada de elementos: Crea un array de objetos con productos (nombre, categoría, precio). Solicita una categoría y muestra todos los productos de esa categoría ordenados por precio.

productos = [
    {"nombre": "laptop", "categoria": "tecnologia", "precio": 3500},
    {"nombre": "hamburguesa", "categoria": "alimentos", "precio": 15},
    {"nombre": "dentrifico", "categoria": "higiene", "precio": 12}
]

buscar_categoria = input("Que categoria buscas?: ").lower()

resultado = []

for producto in productos:
    if producto["categoria"] == buscar_categoria:
        resultado.append(producto)

resultado.sort(key=lambda x: x["precio"])

for precio in resultado:
    print(precio["nombre"], ":", precio["precio"])

# Filtrado y estadística de temperaturas: Dado un array de temperaturas de un mes, filtra los días con temperaturas mayores al promedio y muestra estadísticas como el mínimo, máximo y promedio general.

# Solución:
