# >>> my_str = "spam, eggs, bacon, spam"
# >>> my_list = ["spam", "spam", "spam"]
# >>> len(my_str)
# 23
# >>> len(my_list)
# 3

# Scrivi una funzione che restituisca
# la lunghezza di una stringa o lista passata come parametro

# lista = list('abcdefghilmnopqrst')
# print('Nella lista ci sono tot elementi: ', len(lista))

lista = [9, 7, 5, 2, 1, 4, 6, 8]

def lunghezza(elemento):
    count = 0
    for i in lista:
        count += 1
    return count
    print('Lunghezza: ', count)

#non ho idea del perchè non va