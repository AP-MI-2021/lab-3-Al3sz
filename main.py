def get_longest_sorted_asc(lst: list[int]) -> list[int]:
    aux = []
    x = 0
    contor = 0
    maxi = 0
    lungime = len(lst)
    for i in range(lungime):
        if maxi < contor:
            maxi = contor
            lst_ret = aux
        if lst[i] > x:
            x = lst[i]
            contor += 1
            aux.append(int(x))
        else:
            contor = 0
            aux = []
    return lst_ret


# def test_get_longest_sorted_asc():
#      assert get_longest_sorted_asc()
#      assert get_longest_sorted_asc()
#      assert get_longest_sorted_asc()
#      assert get_longest_sorted_asc()

# def get_longest_equal_int_real(lst: list[float]) -> list[float]:
#
#
# def test_get_longest_equal_int_real():
#      assert get_longest_equal_int_real()
#      assert get_longest_equal_int_real()
#      assert get_longest_equal_int_real()
#      assert get_longest_equal_int_real()


# def get_longest_powers_of_k(lst: list[int], k: int) -> list[int]:

# def test_get_longest_powers_of_k()
#     assert get_longest_powers_of_k()
#     assert get_longest_powers_of_k()
#     assert get_longest_powers_of_k()
#     assert get_longest_powers_of_k()
#
def citire_lista():
    lista = []
    lista_string = input('Tastați lista: ')
    len_lista = lista_string.split(' ')
    for x in len_lista:
        lista.append(float(x))
    return(lista)


def menu():
    print('''
    1 -> Citire listă.
    2 -> Determinare cea mai lungă subsecvență cu proprietatea că numerele sunt ordonate crescător.
    3 -> Determinare cea mai lungă subsecvență cu proprietatea că toate numerele au partea întreagă egală cu partea fracționară.
    4 -> Determinare cea mai lungă subsecvență cu proprietatea că toate numerele au partea întreagă egală cu partea fracționară.
    x -> Ieșire.
    ''')


def main():
    # test_get_longest_sorted_asc()
    # test_get_longest_equal_int_real()
    while True:
        menu()
        optiune = input('Alegeți una dintre opțiunile de mai sus: ')
        if optiune == '1':
            l = citire_lista()
        elif optiune == '2':
            print(f'Cea mai lungă secvență de numere ordonate crescător este: {get_longest_sorted_asc(l)}.')
        elif optiune == '3':
            print(
                f'Cea mai lungă secvență de numere cu partea întreagă egală cu cea fracționară este: {get_longest_equal_int_real(l)}.')
        elif optiune == '4':
            print(
                f'Cea mai lungă secvență de numere se pot scrie ca x**k, k citit, x întreg pozitiv este: {get_longest_powers_of_k(l)}.')
        elif optiune == 'x':
            break
        else:
            print('Opțiune greșită! Reîncercați: ')


if __name__ == '__main__':
    main()
