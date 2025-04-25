import funciones


def main():
    id_tweet = 0
    lista_tweets = {}
    modo = ""
    while modo != "4":
        modo = funciones.mostrar_menu()
        if modo == "4":
            break
        id_tweet = funciones.seleccionar_modo(modo, id_tweet, lista_tweets)


    return


# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()