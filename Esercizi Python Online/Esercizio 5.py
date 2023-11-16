#Scrivi un programma "moltiplicatore" che,
# data una lista di numeri, moltiplichi tra loro tutti gli elementi.

lista_numeri = input('Inserisci una lista di numeri separata dallo spazio: ').split()

moltiplicatore = 1

for i in lista_numeri:
    if i != 0:
        moltiplicatore *= int(i)


print('La moltiplicazione complessiva è: ', moltiplicatore)