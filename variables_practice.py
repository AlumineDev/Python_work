persona = "Alberto"
print("Hello, " + persona + "!")
actividad = "Aprender"
print(f"{persona} te gustaria {actividad} Python?.")
#print("Hello, " + persona + "!") # Concatenación de cadenas
#print(f"{persona} te gustaria {actividad} Python?") # Formateo de cadenas con f-strings

edad = 30
print(f"{persona} tiene {edad} años y aun le interesa {actividad} Python.")
edad = 40
print(f"{persona} si llegas a los {edad} años, aun es tiempo de {actividad} Python.")

persona_2 = "Maria"
print(f"{persona} y {persona_2} son amigos y ambos quieren {actividad} Python.")
edad_persona2 = 25
print(f"{persona_2} tiene {edad_persona2} años y también le interesa {actividad} Python.")
print(f"{persona} y {persona_2} están emocionados por aprender Python juntos. {persona} tiene {edad} años y {persona_2} tiene {edad_persona2} años.")
