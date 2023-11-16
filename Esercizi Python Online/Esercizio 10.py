#un po' di esercizi sulle funzioni

# Esercizio 1: Definisci una funzione, nome max,
# che restituisce il numero più grande tra due numeri dati.

def max(a, b):

    if a > b:
        numero_maggiore = a
    else:
        numero_maggiore = b

    print("Il numero maggiore è: ", numero_maggiore)

a = input('Inserisci il primo numero: ')

b = input('Inserisci il secondo numero: ')

max(a,b)

#Definisci una funzione, nome max,
# che restituisce il numero più grande tra tre numeri dati.
# Utilizza l'if all'interno della funzione.

def max(a,b,c):

    if a > b > c:
        numero_maggiore = a

    elif b > c > a:
        numero_maggiore = b

    else:
        numero_maggiore = c

    print("Il numero maggiore è: ", numero_maggiore)

a = input('Inserisci il primo numero: ')

b = input('Inserisci il secondo numero: ')

c = input('Inserisci il terzo numero: ')

max(a,b,c)

#Definisci una funzione chiamata multi,
# che accetta come parametro un oggetto iterabile (lista, tupla)
# e restituisce il prodotto di tutti gli elementi della lista.

def multi(numbers):
   result = 1
   for number in numbers:
       result *= number
   return result

elenco_numeri = input('Inserisci dei numeri: ')
lista_numeri = elenco_numeri.split()

lista_numeri = [int(numero) for numero in lista_numeri]

risultato = multi(elenco_numeri)

print('Il risultato è: ', risultato)