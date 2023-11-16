#Scrivi una semplice funzione che, data una lista di numeri,
# fornisca in output un
# istogramma basato su questi numeri,
# usando asterischi per disegnarlo.

lista = input('Inserisci numeri separati da spazio: '),split()

def istogramma(lista):
    for i in lista:
        print("*" * int(i))

#boh dovrebbe andare credo sia linux mint