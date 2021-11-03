from Domain.cheltuiala import creeaza_cheltuiala, get_id


def create(lst_cheltuieli, id_cheltuiala:int, numar_apartament, suma, data:str, tip_intretinere, tip_canal, tip_alte_cheltuieli):
    '''
    :return: o lista noua si formata din cea precedenta si noua cheltuiala
    '''
    if read(lst_cheltuieli,id_cheltuiala) is not None:
        raise ValueError(f'exista deja o cheltuiala cu id-ul {(id_cheltuiala)}')
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, numar_apartament, suma, data, tip_intretinere, tip_canal, tip_alte_cheltuieli)
    return lst_cheltuieli + [cheltuiala]

def read(lst_cheltuieli, id_cheltuiala: int=None):
    '''
    Citeste o cheltuiala din 'baza de date'
    :return: lista cu toate cheltuielile daca id_apartament=None
            cheltuiala cu id-ul id_cheltuiala daca exista
            None, daca nu exista o cheltuiala cu id_cheltuiala
    '''
    if not id_cheltuiala:
        return lst_cheltuieli
    cheltuiala_cu_id = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_cu_id=cheltuiala

    if cheltuiala_cu_id:
        return cheltuiala_cu_id
    return None
    

def delete(lst_cheltuieli, id_cheltuiala:int):
    '''
    :return: lista de cheltuieli fara cheltuiala cu id-ul apartamentului id_apartament
    '''
    if read(lst_cheltuieli,id_cheltuiala) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {get_id(id_cheltuiala)} pe care sa o stergem')
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
    if read(lst_cheltuieli, get_id(new_cheltuiala)) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {get_id(new_cheltuiala)} pe care sa o actualizam')
    new_cheltuieli=[]
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)

    return new_cheltuieli

    

