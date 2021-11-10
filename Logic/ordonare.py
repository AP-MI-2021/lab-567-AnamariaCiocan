from Domain.cheltuiala import get_suma


def get_ordonare(lst_cheltuieli,undo_list, redo_list ):
    '''
    Ordoneaza cheltuielile in functie de suma
    :param:lst_cheltuieli-lista cheltuielilor
    :return:lista ordonata
    '''
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return sorted(lst_cheltuieli, key=get_suma, reverse=True)