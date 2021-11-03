from Domain.cheltuiala import get_numar_apartament, get_suma


def get_suma_apartament(lst_cheltuieli):
    '''
    return: un dictionar in care cheia este numarul apartamentului si valoarea este cheltuiala cu suma de cheltuieli maxima
    '''
    result={}
    for cheltuiala in lst_cheltuieli:
        numar= get_numar_apartament(cheltuiala)
        suma = get_suma(cheltuiala)
        if numar not in result:
            result[numar]=cheltuiala
        else:
            if suma > get_suma(result[numar]):
                result[numar]=cheltuiala
    return result
