from Domain.cheltuiala import creeaza_cheltuiala, get_data, get_id, get_numar_apartament, get_suma, get_tip_alte_cheltuieli, get_tip_canal, get_tip_intretinere


def adunare_valoare(lst_cheltuieli, data, val:int):
    '''
    Adunarea unei valori tuturor cheltuilelior dintr-o data citita
    param: lst_cheltuieli - lista cheltuielilor
           data - data cheltuileii pentru care se aduna o valoare
           val-valoarea care trebuie adaugata
    return: lista modificata
    '''
    result=[]
    for cheltuiala in lst_cheltuieli:
        if data in get_data(cheltuiala):
            suma_noua = val + int(get_suma(cheltuiala))
            result.append(creeaza_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala), suma_noua, get_data(cheltuiala), get_tip_intretinere(cheltuiala), get_tip_canal(cheltuiala), get_tip_alte_cheltuieli(cheltuiala))) 
        else:
            result.append(cheltuiala)
    return result

