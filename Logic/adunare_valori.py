from Domain.cheltuiala import creeaza_cheltuiala, get_data, get_id, get_numar_apartament, get_suma, get_tip


def adunare_valoare(lst_cheltuieli, data, val:int, undo_list, redo_list):
    '''
    Adunarea unei valori tuturor cheltuilelior dintr-o data citita
    param: lst_cheltuieli - lista cheltuielilor
           data - data cheltuileii pentru care se aduna o valoare
           val-valoarea care trebuie adaugata
    return: lista modificata
    '''
    
    if val < 0:
        raise ValueError('Trebuie adaugata o valoare pozitiva ')
    if len(data)>10:
        raise ValueError('Data introdusa este invalida')
    result=[]
    
    for cheltuiala in lst_cheltuieli:
        if data == get_data(cheltuiala):
            suma_noua = val + int(get_suma(cheltuiala))
            result.append(creeaza_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala), suma_noua, get_data(cheltuiala), get_tip(cheltuiala))) 
        else:
            result.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    
    return result

