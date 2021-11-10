from Domain.cheltuiala import get_suma, get_tip


def get_max_tip_intretinere(lst_cheltuieli, undo_list, redo_list):
    '''
    Determina cea mai mare cheltuiala corespunzatoare fiecarui tip de cheltuiala.
    :param: lst_cheltuieli - lista cu cheltuielile
    return: un dictionar in care cheia este tipul cheltuielii si valoarea este cea mai mare valoare pentru tipul respectiv
    '''
    result={}
    for cheltuiala in lst_cheltuieli:
        tip_cheltuiala=get_tip(cheltuiala)
        suma=get_suma(cheltuiala)
        if tip_cheltuiala not in result:
            result[tip_cheltuiala]=suma
        else:
            if suma > result[tip_cheltuiala]:
                result[tip_cheltuiala]=suma
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return result

