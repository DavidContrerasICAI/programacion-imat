import pyjokes

"""
Almacenamiento de chistes
"""
SEPARADOR = "#"
chistes = ""
NUEVOS_CHISTES = False

if NUEVOS_CHISTES:
    i = 0
    while i < 10:
        chiste = pyjokes.get_joke()
        chistes += chiste 
        chistes += SEPARADOR
        i += 1
else:
    chistes = "There are 10 types of people: those who understand trinary, those who don't, and those who have never heard of it."
    chistes += "#You never finish a program, you just stop working on it."
    chistes += "#There are 10 types of people: those who understand hexadecimal and 15 others."
    chistes += "#How do you know whether a person is a Vim user? Don't worry, they'll tell you."
    chistes += "#Why do programmers prefer dark mode? Because light attracts bugs."
    chistes += "#!false, (It's funny because it's true)"
    chistes += "#There are three kinds of people: those who can count and those who can't."
    chistes += "#Those who can, do. Those who cannot, teach. Those who cannot teach, HACK!"
    chistes += "#Programming is 10% science, 20% ingenuity, and 70% getting the ingenuity to work with the science."
    chistes += "#What do you call a parrot that says \"Squawk! Pieces of nine! Pieces of nine!\"? A parrot-ey error."

print("Chistes generados!")

"""
Recuperación
"""
topic = input("¿De qué topic quieres el chiste?: ")
contador_chiste = 1
i = 0
while i < len(chistes) - len(topic):
    chiste = ""
    chiste_valido = False
    while chistes[i] != "#" and i < len(chistes) - len(topic):
        chiste += chistes[i]
        if chistes[i:i+len(topic)].upper() == topic.upper(): 
            chiste_valido = True
        i += 1
    if chiste_valido:
        print(f"{contador_chiste}.- {chiste}")
        contador_chiste += 1
    i += 1