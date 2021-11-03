from Domain.cheltuiala import creeaza_cheltuiala, get_data, get_id, get_numar_apartament, get_suma, get_tip_alte_cheltuieli, get_tip_canal, get_tip_intretinere


def stergere_cheltuieli_pentru_un_apartament(lst_cheltuieli, numar_apartament):
    '''
    Stergerea cheltuielilor pentru un apartament dat
    param: lst_cheltuieli - lista cheltuielilor
            numar_apartament - numarul apartamentului pentru care se efectueaza stergerea
    return: lista modificata
    '''
    result=[]
    for cheltuiala in lst_cheltuieli:
        if numar_apartament == get_numar_apartament(cheltuiala):
            suma_noua = get_suma(cheltuiala)*0
            cheltuieli_tip_intretinere= 0
            cheltuieli_tip_canal= get_tip_canal(cheltuiala)*0
            alt_tip_de_cheltuieli=get_tip_alte_cheltuieli(cheltuiala)*0
            result.append(creeaza_cheltuiala(get_id(cheltuiala), get_numar_apartament(cheltuiala), suma_noua, get_data(cheltuiala), cheltuieli_tip_intretinere, cheltuieli_tip_canal, alt_tip_de_cheltuieli)) 
        else:
            result.append(cheltuiala)
    return result
