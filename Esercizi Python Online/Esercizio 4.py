#Scrivi un semplice programma che, data una lista di numeri,
# sommi tra loro tutti gli elementi.
# Suggerimento: anche se esiste la funzione sum() per risolvere
# l'esercizio potresti usare il ciclo for.

lista_numeri = input('Inserisci 5 numeri da 1 a 100: ').split()

somma = 0 # è semplicemente una varibile al momento fissa
#il succo del discorso è tra poco con l'operatore logico +=
#che appunto intende la somma

for i in lista_numeri: # se sto capendo bene, numero è il nuovo nome
    # dato a ciascuna variabile all'interno della lista
    somma += int(i)


print('La somma dei numeri è: ', somma)