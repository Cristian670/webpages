#Scrivi un programma che a partire da un elemento e
# una lista di elementi dica in output se l'elemento passato sia
# presente o meno nella lista.
# Qualora l'elemento sia presente nella lista,
# il programma dovrà comunicarci l'indice dell'elemento tramite
# il metodo index.

lista = ['Marco', 'Luigi', 'Paolo', 'Giuseppe', 'Maria']
el = input("Inserisci un nome da cercare: ")
trovato = False
for nome in lista:
    if nome == el:
        trovato = True
        break
if trovato:
    print(f"{el} è presente nella lista all'indice {lista.index(el)}")
else:
    print(f"{el} non è presente nella lista.")

#questo non sapevo farlo, l'ho messo lo stesso, sicuro servirà
