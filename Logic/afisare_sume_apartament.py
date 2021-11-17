from Domain.cheltuiala import get_data, get_numar_apartament, get_suma

def get_suma_apartament(lst_cheltuieli):
    '''
    Determina sumele lunare pentru fiecare apartament
    :param:lst_cheltuieli-lista cheltuielilor
    :return:un dictionar in care cheia este luna si valoarea este suma cheltuielilor lunare pentru toate apartamentele.
    '''
    result={}
    for cheltuiala in lst_cheltuieli:
        date=get_data(cheltuiala)
        luna=date.split('.')[1]
        suma=get_suma(cheltuiala)
        if luna not in result:
             result[luna]=suma
        else:
             result[luna]+=suma
    return result