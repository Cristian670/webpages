#Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
#Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.



n = int(input('Inserisci il primo numero: '))

m = int(input('Inserisci il secondo numero: '))

if n < m:
    print('Il primo numero è più piccolo')

elif n == m:
    print('I numeri sono identici')

else:
    print('Il primo numero è più grande')


# Soluzione in forma alternativa con particolare attenzione a dove inserire
#str o come ho fatto io con int

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")

if a == b:
    print("I numeri sono identici")
elif a > b:
    print("Il numero più grande tra i due è " + str(a))
else:
    print("Il numero più grande tra i due è " + str(b))