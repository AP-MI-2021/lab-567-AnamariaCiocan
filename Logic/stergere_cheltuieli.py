from Domain.cheltuiala import get_nr_primit, get_numar_apartament


def stergere_cheltuieli_pentru_un_apartament(lst_cheltuieli, numar_apartament, undo_list, redo_list):
    '''
    Stergerea cheltuielilor pentru un apartament dat
    param: lst_cheltuieli - lista cheltuielilor
            numar_apartament - numarul apartamentului pentru care se efectueaza stergerea
    return: lista modificata
    '''
    if numar_apartament == ' ':
        raise ValueError('Numarul nu poate fi un spatiu.')
    if get_nr_primit(lst_cheltuieli, numar_apartament) is False:
        raise ValueError('Numarul apartamentului nu exista in baza de date ')
    result=[]
    for cheltuiala in lst_cheltuieli:
        if numar_apartament != get_numar_apartament(cheltuiala):
             result.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return result

