
def tokenizar(tweet):
    token_por_pal = []
    token_x_seg = []
    for palabra in tweet:
        token_por_pal.append(palabra)
        for c in palabra:
           print(palabra[0]) 

tweet = input("ingrese twit")
respuesta = tokenizar(tweet)
print(tweet)