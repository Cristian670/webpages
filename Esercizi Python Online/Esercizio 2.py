#Scrivi un programma che chieda all'utente
# una lista di numeri e fornisca in output il maggiore tra tutti.


#script per seprare numeri
#txt = "2, 5, 7, 9, 3, 1, 8"
#x = txt.split(", ")
#print(x)

#come ordinare crescente o decrescente
#numeri_crescenti = ['9', '5', '2']
#numeri_crescenti.sort()
# in ordine decrescente bisogna mettere list.sort(reverse=True, key=myFunc)

lista_numeri = input('Inserisci 5 numeri casuali: ')

ordine_crescente = lista_numeri.split()

sorted(ordine_crescente)

n = max(ordine_crescente)

print('In ordine crescente: ', sorted(ordine_crescente))

print('Il numero più grande è: ', n)

#di seguito la soluzione del sito

lista_numeri = [42, 9, 23, 11, 17, 56, 3]
numero_maggiore = lista_numeri[0]
for numero in lista_numeri:
    if numero > numero_maggiore:
        numero_maggiore = numero
print("Il numero maggiore tra tutti è:", numero_maggiore)


#di seguito la soluzione del sito
