#Instrucciones: Dada la siguiente lista de lenguajes de programación, realiza las siguientes operaciones de slicing y muestra los resultados:

list_lenguajes = ["C", "Java", "Python", "C++", "JavaScript", "Ruby", "Go", "Swift", "Kotlin", "Rust"]
# Imprime el primer elemento de la lista
print(list_lenguajes[0])  # Salida: C
# Imprime el último elemento de la lista
print(list_lenguajes[-1])  # Salida: Rust
# Imprime los elementos desde el índice 2 hasta el índice 5 (excluyendo el índice 5)
print(list_lenguajes[2:5])  # Salida: ['Python', 'C++', 'JavaScript']
# Imprime los elementos desde el inicio hasta el índice 3 (excluyendo el índice 3)
print(list_lenguajes[:3])  # Salida: ['C', 'Java', 'Python']
# Imprime los elementos desde el índice 4 hasta el final de la lista
print(list_lenguajes[4:])  # Salida: ['JavaScript', 'Ruby', 'Go', 'Swift', 'Kotlin', 'Rust']
# Imprime los elementos desde el índice 1 hasta el índice 7 (excluyendo el índice 7) con un paso de 2
print(list_lenguajes[1:7:2])  # Salida: ['Java', 'C++', 'Ruby']
# Imprime los elementos desde el inicio hasta el final de la lista con un paso de 3
print(list_lenguajes[::3])  # Salida: ['C', 'C  ++', 'Go', 'Kotlin']
# Imprime los elementos desde el índice 5 hasta el índice 1 (excluyendo el índice 1) con un paso de -1
print(list_lenguajes[5:1:-1])  # Salida: ['Ruby', 'JavaScript', 'C++', 'Python']
# Imprime los elementos desde el índice 8 hasta el índice 2 (excluyendo el índice 2) con un paso de -2
print(list_lenguajes[8:2:-2])  # Salida: ['Kotlin', 'Swift', 'Go'] 

for i, lenguaje in enumerate(list_lenguajes):
    print(f"Índice {i}: {lenguaje}")
    if lenguaje == "Rust":
        break
for i in range(len(list_lenguajes)):
    print(f"Índice {i}: {list_lenguajes[i]}")
    if list_lenguajes[i] == "C":
        print("Comenzamos")
    elif list_lenguajes[i] == "Python":
        print("¡Encontré Python!")
    elif list_lenguajes[i] == "Rust":
        print("¡Finalizamos con Rust!")
        break

for i, lenguaje in enumerate(list_lenguajes):
    print(f"Índice {i}: {lenguaje}")
    if lenguaje == "C":
        print("Comenzamos")
    elif lenguaje == "Python":
        print("¡Encontré Python!")
    elif lenguaje == "Rust":
        print("¡Finalizamos con Rust!")
        break

empleados = ["Alice", "Bob", "Charlie", "David", "Eve"]
buscamos = "Charlie"
for i, empleado in enumerate(empleados):
    if empleado == buscamos:
        print(f"{buscamos} encontrado en el índice {i}.")
        break
    else:
        print(f"{buscamos} no esta en {i}.")
buscamos = "Zara"
for i, empleado in enumerate (empleados):
    if empleado == buscamos:
        print(f"{buscamos} encontrado en el índice {i}.")
        break
    else:        print(f"{buscamos} no esta en {i}.")
else:
    print(f"{buscamos} no se encontró en la lista de empleados.")

numeros = [1, 2, 3, 4, 5]
for i in numeros:
    if i % 2 == 0:
        print(f"{i} es un número par.")
    else:
        print(f"{i} es un número impar.")

for i in range(numeros[0], numeros[-1] + 1):
    if i % 2 == 0:
        print(f"{i} es un número par.")
    else:
        print(f"{i} es un número impar.")

#Vamos a probar a remover valores de una lista.
frutas = ["manzana", "banana", "naranja", "pera", "uva"]
# Remover la fruta "naranja" de la lista
frutas.remove("naranja")
print(frutas)  # Salida: ['manzana', 'banana', 'pera', 'uva']
# Remover la fruta en el índice 1 (banana)
frutas.pop(1)
print(frutas)  # Salida: ['manzana', 'pera', 'uva']
# Remover la última fruta de la lista
frutas.pop()
print(frutas)  # Salida: ['manzana', 'pera']
# Remover la fruta "manzana" de la lista
frutas.remove("manzana")
print(frutas)  # Salida: ['pera']
del frutas[0]  # Eliminar la fruta en el índice 0 (pera)
print(frutas)  # Salida: []
frutas = ["manzana", "banana", "naranja", "pera", "uva"]
# Remover la fruta "kiwi" de la lista (que no existe)
try:
    frutas.remove("kiwi")
except ValueError:
    print("La fruta 'kiwi' no está en la lista.")
added = frutas + ["kiwi"]
print(added)  # Salida: ['manzana', 'banana', 'naranja', 'pera', 'uva', 'kiwi']

if "kiwi" in added:
    added.remove("kiwi")
    print("La fruta 'kiwi' ha sido removida de la lista.")
else:    
    print("La fruta 'kiwi' no está en la lista.")

# Crearemos un bucle para remover todas las frutas de la lista.
frutas = ["manzana", "banana", "naranja", "pera", "uva"]
while frutas:
    fruta_removida = frutas.pop()
    print(f"Removiendo {fruta_removida} de la lista.")

print("La lista de frutas está ahora vacía.")
# Crearemos un bucle para remover todas las frutas de la lista utilizando un bucle for.
frutas = ["manzana", "banana", "naranja", "pera", "uva"]

for i in range(len(frutas) - 1, -1, -1):
    fruta_removida = frutas.pop(i)
    print(f"Removiendo {fruta_removida} de la lista.")

print("La lista de frutas está ahora vacía.")

#Agregaremos elementos a una lista utilizando el método append() y extend().
frutas = ["manzana", "banana", "naranja"]
# Agregar una fruta al final de la lista
frutas.append("pera")
print(frutas)  # Salida: ['manzana', 'banana', 'naranja', 'pera']
# Agregar varias frutas al final de la lista
frutas.extend(["uva", "kiwi"])
print(frutas)  # Salida: ['manzana', 'banana', 'naranja', 'pera', 'uva', 'kiwi']
# Agregar una fruta al final de la lista utilizando el operador +
frutas = frutas + ["mango"]
print(frutas)  # Salida: ['manzana', 'banana', 'naranja', 'pera', 'uva', 'kiwi', 'mango']
# Agregar una fruta al final de la lista utilizando el método insert() en el índice 0
frutas.insert(0, "fresa")
print(frutas)  # Salida: ['fresa', 'manzana', 'banana', 'naranja', 'pera', 'uva', 'kiwi', 'mango']
# Llenaremos una lista con un bucle for utilizando el método append().
numeros = []
for i in range(1, 11):
    numeros.append(i)
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 1 in numeros:
    print("Se Agrego el numero 1 a la lista. " \
    "Se Agrego el numero 2 a la lista. " \
    "Se Agrego el numero 3 a la lista. " \
    "Se Agrego el numero 4 a la lista. " \
    "Se Agrego el numero 5 a la lista. " \
    "Se Agrego el numero 6 a la lista. " \
    "Se Agrego el numero 7 a la lista. " \
    "Se Agrego el numero 8 a la lista. " \
    "Se Agrego el numero 9 a la lista. " \
    "Se Agrego el numero 10 a la lista. ")
else:
    print("No se pudo agregar el numero a la lista.")

