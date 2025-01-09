meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso.",
    "LOL": "Una respuesta común a algo gracioso.",
    "BRB": "Vuelvo en un momento.",
    "GG": "Buen juego, usado después de un partido.",
    "AFK": "Lejos del teclado.",
}

print("¡Bienvenido al Diccionario de Memes!")
print("Escribe una palabra en mayúsculas y te diré lo que significa.")
print("Tienes 5 oportunidades para buscar palabras.")

for _ in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(word + ": " + meme_dict[word])
    else:
        print("Lo siento, esa palabra no está en el diccionario. 😢")

print("¡Gracias por usar el Diccionario de Memes! Vuelve pronto. 😊")
