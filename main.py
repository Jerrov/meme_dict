meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una respuesta para expresar risa",
            "VISAJES RAROS": "Usado para referirse a la serie de Stranger Things",
            "NONES": "Para dar negativo a algo",
            "APACHURRALE STARD": "Para referirse a que inicien",
                        }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("La palabra no se encuentra en este diccionario")
