from Domain.cheltuiala import get_data, get_numar_apartament, get_suma

def get_suma_apartament(lst_cheltuieli):
    '''
    Determina sumele lunare pentru fiecare apartament
    :param:lst_cheltuieli-lista cheltuielilor
    :return:un dictionar in care cheia este numarul apartamentului si valoarea este suma cheltuielilor sale
    '''
    result={}
    for cheltuiala in lst_cheltuieli:
        numar_ap=get_numar_apartament(cheltuiala)
        suma=get_suma(cheltuiala)
        if numar_ap not in result:
             result[numar_ap]=suma
        else:
             result[numar_ap]+=suma
    return result