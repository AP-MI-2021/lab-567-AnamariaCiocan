from Domain.cheltuiala import creeaza_cheltuiala, get_id

def inverse_create(lst_cheltuieli, id_cheltuiala):
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli

def create(lst_cheltuieli, id_cheltuiala:int, numar_apartament, suma, data:str, tip_cheltuiala, undo_list: list, redo_list: list):
    '''
    :param lst_cheltuieli: lista de cheltuieli.
    :param id_cheltuiala:id-ul cheltuielii
    :param tip_cheltuiala:tipul cheltuielii
    :param numar_apartament:numarul apartamentului care are cheltuiala
    :param suma:suma cheltuielii
    :param data:data la care a fost efectuata cheltuiala
    :param undo_list:lista care se modifica in urma apelului unei functionalitati
    :param redo_list:lista care se modifica in urma apelarii undo
    :return: o lista noua si formata din cea precedenta si noua cheltuiala
    '''
    if read(lst_cheltuieli,id_cheltuiala) is not None:
        raise ValueError(f'exista deja o cheltuiala cu id-ul {(id_cheltuiala)}')
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, numar_apartament, suma, data, tip_cheltuiala)
    undo_list.append(
        (lambda lst: inverse_create(lst, id_cheltuiala),
         lambda lst: lst.append(cheltuiala))
     )
    # undo_list = [f_lambda1]
    redo_list.clear()
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
    

def delete(lst_cheltuieli, id_cheltuiala:int, undo_list, redo_list):
    '''
    :return: lista de cheltuieli fara cheltuiala cu id-ul apartamentului id_apartament
    '''
    if read(lst_cheltuieli,id_cheltuiala) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {get_id(id_cheltuiala)} pe care sa o stergem')
    new_cheltuieli=[]
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuieli.append(cheltuiala)
    undo_list.append(lst_cheltuieli)
    redo_list.clear()

    return new_cheltuieli

def update(lst_cheltuieli, new_cheltuiala, undo_list, redo_list):
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
    undo_list.append(lst_cheltuieli)
    redo_list.clear()

    return new_cheltuieli

    

