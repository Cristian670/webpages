
metri = input('Inserisci metri: ')

def metri_iarde(metri):
    iarde = int(metri) * 1.09361
    return iarde
print('Iarde: ', metri_iarde(metri))

def metri_miglia(metri):
    miglia = int(metri) * 0.000621371
    return miglia
print('Miglia: ', metri_miglia(metri))

def metri_piedi(metri):
    piedi = int(metri) * 3.28
    return piedi
print('Piedi: ', metri_piedi(metri))

def metri_pollici(metri):
    pollici = int(metri) * 39.370
    return pollici
print('Pollici: ', metri_pollici(metri))