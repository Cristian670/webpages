#Scrivi una funzione che, dato in ingresso un valore espresso in metri,
# mandi in print l'equivalente in miglia terrestri, iarde,
# piedi e pollici. Come risolverai questo esercizio?

metri = input('Inserisci una lunghezza espressa in metri: ')

iarde = int(metri) * 1.09361
print('Iarde: ', iarde)

miglia = int(metri) * 0.000621371
print('Miglia: ', miglia)

piedi = int(metri) * 3.28
print('Piedi: ', piedi)

pollici = int(metri) * 39.370
print('Pollici: ', pollici)
