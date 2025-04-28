
def tokenizar(tweet):
    token_por_pal = tweet.split()
    token_x_seg = []
    segmento = ""
    caracter = 0
    for palabra in token_por_pal:
        if len(palabra) >= 3:
            for c in palabra:
                while len(segmento) < len(palabra):
                    segmento += palabra[caracter]
                    caracter += 1
                    if len(segmento) >= 3:
                        token_x_seg.append(segmento)
                caracter = 0
                segmento = ""


tweet = input("ingrese twit: ")
respuesta = tokenizar(tweet)
print(respuesta)

#########################################

def tokenizar(tweet):
    token_por_pal = tweet.split()
    token_x_seg = []
    
    for palabra in token_por_pal:
        if len(palabra) >= 3:
            i = 0
            while i <= len(palabra) - 3:
                j = i + 3
                while j <= len(palabra):
                    segmento = palabra[i:j]
                    token_x_seg.append(segmento)
                    j += 1
                i += 1
                
    return token_x_seg

# Ejecución
tweet = input("Ingrese tweet: ")
respuesta = tokenizar(tweet)
print(respuesta)
