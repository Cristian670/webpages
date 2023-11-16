#Scrivi un programma che chieda all'utente una stringa
# composta da un solo carattere e dica se
# si tratta di una vocale oppure no

vocali = 'a', 'e', 'i', 'o', 'u'
consonanti = list('bcdfghlmnpqrstvz')
numeri = list('123456789')

carattere = input('Inserisci una lettera: ')

if carattere in vocali:
    print('Hai scritto una vocale')

elif carattere in consonanti:
    print('Hai scritto una consonante')

elif carattere in numeri:
    print('Hai scritto un numero')
