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
