from numpy import append


lista_lenguajes = ["Python", "JavaScript", "Java", "C#", "C++"] # Definimos una lista llamada lista_lenguajes que contiene los nombres de algunos lenguajes de programación populares.
for lenguaje in lista_lenguajes: # Utilizamos un bucle for para iterar sobre cada elemento en la lista lista_lenguajes y mostrarlo al usuario.
    print(f"- {lenguaje}") # Dentro del bucle, utilizamos la función print para mostrar cada lenguaje de programación en una nueva línea, utilizando una cadena formateada (f-string) para incluir el valor de la variable lenguaje en el mensaje.
    print("Todos estos lenguajes requieren una base de logica solida") # Utilizamos la función print para mostrar un mensaje al usuario indicando que todos estos lenguajes de programación requieren una base de lógica sólida para ser aprendidos y utilizados de manera efectiva. Esto es importante para que los estudiantes comprendan que aprender a programar no solo implica memorizar sintaxis, sino también desarrollar habilidades de pensamiento lógico y resolución de problemas.

modulos_estudio = ["Sintaxis básica", "Estructuras de control", "Funciones", "Programación orientada a objetos", "Manejo de archivos"] # Definimos una lista llamada modulos_estudio que contiene los nombres de algunos modulos mencionados.
print("Los módulos que vamos a estudiar en esta etapa son:") # Utilizamos la función print para mostrar un mensaje al usuario indicando que se mostrarán los módulos que se van a estudiar en esta etapa.
for modulo in modulos_estudio: # Utilizamos un bucle for para iterar sobre cada elemento en la lista modulos_estudio y mostrarlo al usuario.
    print(f"- Estudio del modulo {modulo}") # Dentro del bucle, utilizamos la función print para mostrar cada módulo en una nueva línea, utilizando una cadena formateada (f-string) para incluir el valor de la variable modulo en el mensaje. Esto permitirá al usuario ver claramente los módulos que se van a estudiar en esta etapa del curso.
for i in range(len(modulos_estudio)):
    if i == 0: # Utilizamos un bucle for para iterar sobre el rango de la longitud de la lista modulos_estudio, lo que nos permitirá acceder a cada módulo por su índice.
        print(f"El módulo {modulos_estudio[i]} es fundamental para entender los conceptos básicos de la programación.") # Dentro del bucle, utilizamos la función print para mostrar un mensaje al usuario indicando que cada módulo es fundamental para entender los conceptos básicos de la programación. Utilizamos una cadena formateada (f-string) para incluir el valor del módulo actual en el mensaje, accediendo a él mediante su índice en la lista modulos_estudio. Esto ayudará a los estudiantes a comprender la importancia de cada módulo en su aprendizaje de la programación.
    elif i == 1:
        print(f"El módulo {modulos_estudio[i]} es esencial para controlar el flujo de nuestro programa y tomar decisiones basadas en condiciones.") # Utilizamos una estructura condicional (if-elif) para mostrar un mensaje específico para cada módulo. En este caso, si el índice es 1, mostramos un mensaje indicando que el módulo de estructuras de control es esencial para controlar el flujo del programa y tomar decisiones basadas en condiciones. Esto ayudará a los estudiantes a comprender la importancia de este módulo en su aprendizaje de la programación.
    elif i == 2:
        print(f"El módulo {modulos_estudio[i]} es crucial para organizar nuestro código en bloques reutilizables y mejorar la legibilidad de nuestro programa.") # Si el índice es 2, mostramos un mensaje indicando que el módulo de funciones es crucial para organizar el código en bloques reutilizables y mejorar la legibilidad del programa. Esto ayudará a los estudiantes a comprender la importancia de este módulo en su aprendizaje de la programación.
    elif i == 3:
        print(f"El módulo {modulos_estudio[i]} es importante para entender los conceptos de la programación orientada a objetos, como clases, objetos, herencia y polimorfismo.") # Si el índice es 3, mostramos un mensaje indicando que el módulo de programación orientada a objetos es importante para entender los conceptos relacionados con clases, objetos, herencia y polimorfismo. Esto ayudará a los estudiantes a comprender la importancia de este módulo en su aprendizaje de la programación.
    elif i == 4:
        print(f"El módulo {modulos_estudio[i]} es fundamental para aprender a manejar archivos, lo que nos permitirá leer y escribir datos en nuestros programas.") # Si el índice es 4, mostramos un mensaje indicando que el módulo de manejo de archivos es fundamental para aprender a manejar archivos, lo que permitirá a los estudiantes leer y escribir datos en sus programas. Esto ayudará a los estudiantes a comprender la importancia de este módulo en su aprendizaje de la programación.

for i in range(min(5, len(modulos_estudio))): # Se limita el rango a 5 para evitar errores si la lista tiene menos de 5 elementos.
    print(f"El módulo {modulos_estudio[i]} es fundamental para aprender a programar.") # Dentro del bucle, se muestra un mensaje indicando que cada módulo es fundamental para aprender a programar, utilizando una cadena formateada (f-string) para incluir el valor del módulo actual en el mensaje. Esto ayudará a los estudiantes a comprender la importancia de cada módulo en su aprendizaje de la programación.

#crearemos una tupla con los nombres de algunos lenguajes de programación populares y luego iteraremos sobre ella para mostrar cada lenguaje al usuario.
tupla_lenguajes = ("Python", "JavaScript", "Java", "C#", "C++") # Definimos una tupla llamada tupla_lenguajes que contiene los nombres de algunos lenguajes de programación populares.
for lenguaje in tupla_lenguajes: # Utilizamos un bucle for para iterar sobre cada elemento en la tupla tupla_lenguajes y mostrarlo al usuario.
    print(f"- {lenguaje}") # Dentro del bucle, utilizamos la función print para mostrar cada lenguaje de programación en una nueva línea, utilizando una cadena formateada (f-string) para incluir el valor de la variable lenguaje en el mensaje. Esto permitirá al usuario ver claramente los lenguajes de programación que se encuentran en la tupla tupla_lenguajes.
tupla_lenguajes_nueva = tupla_lenguajes + ("Ruby",) # Creamos una nueva tupla que incluye el nuevo lenguaje de programación "Ruby" junto con los elementos existentes en la tupla original.
for lenguaje in tupla_lenguajes_nueva: # Iteramos sobre la nueva tupla para mostrar cada lenguaje al usuario.
    print(f"- {lenguaje}") # Mostramos cada lenguaje de programación en una nueva línea, utilizando una cadena formateada (f-string) para incluir el valor de la variable lenguaje en el mensaje. Esto permitirá al usuario ver claramente los lenguajes de programación que se encuentran en la nueva tupla tupla_lenguajes_nueva.
tupla_lenguajes.append("Swift") # Intentamos agregar un nuevo lenguaje de programación "Swift" a la tupla tupla_lenguajes utilizando el método append, lo cual no es posible ya que las tuplas son inmutables y no pueden ser modificadas después de su creación. Esto resultará en un error, lo que demuestra la naturaleza inmutable de las tuplas en Python.
# El error que se generará al intentar ejecutar esta línea será un AttributeError, indicando que el objeto 'tuple' no tiene el atributo 'append'. Esto es porque las tuplas en Python no pueden ser modificadas después de su creación, a diferencia de las listas que sí permiten agregar, eliminar o modificar elementos.

# Bloque con errores intencionales:
metas = ['empleo', 'maestria', 'proyectos']
for meta in metas
print(f"Mi objetivo es: {meta}")

# En este bloque de código, hay un error de sintaxis en la línea del bucle for. Falta el signo de dos puntos (:) al final de la línea que inicia el bucle for. La línea correcta debería ser:
# Bloque con errores intencionales:
metas = ['empleo', 'maestria', 'proyectos']
for meta in metas: # Faltaba agregar los dos puntos al final del codigo for.
    print(f"Mi objetivo es: {meta}") # En este otro faltaba agregar el espacio al inicio de la linea para indicar que es parte del bloque del for.

