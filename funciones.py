MENSAJE_MENU = "1. Crear Tweet\n2. Buscar Tweet\n3. Eliminar Tweet\n4. Salir\n>>> "
NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
INPUT_INVALIDO = "Input invalido."
FIN = "Finalizando..."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"


def mostrar_menu():
    eleccion = input(MENSAJE_MENU)
    while eleccion not in "1 2 3 4":
        print(INPUT_INVALIDO)
        eleccion = input(MENSAJE_MENU)
    if eleccion == "4":
        print(FIN)
    return eleccion


def seleccionar_modo(eleccion, id_tweet, lista_tweets):
    if eleccion == "1":
        id_tweet = crear_tweet(id_tweet, lista_tweets)
    elif eleccion == "2":
        buscar_tweet(id_tweet, lista_tweets)
    else:
        print("eliminar_tweet()")
    return id_tweet


def crear_tweet(id_tweet, lista_tweets):
    invalido = True
    while invalido:
        tweet_normalizado = ""
        tweet = input("Ingrese el tweet a almacenar:\n>>>")
        for c in tweet.lower():
            if c == " " or c.isalnum():
                tweet_normalizado += c
        if not tweet_normalizado:
            print(INPUT_INVALIDO)
        else:
            lista_tweets[id_tweet] = {tweet, tweet_normalizado}
            id_tweet += 1
            print(f"OK {id_tweet}")
            invalido = False
    return id_tweet


def buscar_tweet(id, lista):
    entrada = input("Ingrese la/s palabra/s clave a buscar:")
    tk_seg, tk_pal = tokenizar(entrada)
    print(tk_pal,tk_seg)
    for s in tk_seg:
        if s in lista.values 
            print(f"Encontrado: ID {id_tweet}, Tweet original: {valores[0]}")
            break
        else:
            print("No se encontró ningún tweet con ese texto normalizado.")


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
    return token_x_seg, token_por_pal
