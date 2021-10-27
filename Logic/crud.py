from Domain.cheltuiala import creeaza_cheltuiala, get_id


def create(lst_cheltuieli, id_cheltuiala:int, numar_apartament, suma, data, tip_intretinere, tip_canal, tip_alte_cheltuieli):
    '''
    :return: o lista noua si formata din cea precedenta si noua cheltuiala
    '''
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, numar_apartament, suma, data, tip_intretinere, tip_canal, tip_alte_cheltuieli)
    return lst_cheltuieli + [cheltuiala]

def read(lst_cheltuieli, id_cheltuiala=None):
    '''
    Citeste o cheltuiala din 'baza de date'
    :return: cheltuiala apartamentului cu id_apartament sau lista cu toate cheltuielile daca id_apartament=None
    '''
    cheltuiala_cu_id = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_cu_id=cheltuiala

    if cheltuiala_cu_id:
        return cheltuiala_cu_id
    return lst_cheltuieli

def delete(lst_cheltuieli, id_cheltuiala:int):
    '''
    :return: lista de cheltuieli fara cheltuiala cu id-ul apartamentului id_apartament
    '''
    new_cheltuieli=[]
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuieli.append(cheltuiala)

    return new_cheltuieli

def update(lst_cheltuieli, new_cheltuiala):
    '''
    Actualizeaza o cheltuiala
    :param lst_cheltuieli: lista cheltuielilor
    :param new_cheltuiala: cheltuiala care se va actualiza, avand un id existent
    :return: o lista cu cheltuiala actualizata
    '''
    new_cheltuieli=[]
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

    

