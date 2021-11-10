def creeaza_cheltuiala(id_cheltuiala:int, numar_apartament:int, suma, data, tip_cheltuiala):
    '''
    Creeaza o cheltuiala.
    :param id_apartament: id-ul unei cheltuieli
    :param numar_apartament: numarul apartamentului
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tip: tipul cheltuielii
    :return: o cheltuiala
    '''
    return {
        'id': id_cheltuiala,
        'numar': numar_apartament,
        'suma': suma,
        'data': data,
        'tip': tip_cheltuiala
    }

def get_id(cheltuiala):
    '''
    Getter pentru id-ul cheltuielii
    :param cheltuiala: cheltuiala
    :return: id-ul cheltuielii
    '''
    return cheltuiala['id']

def get_numar_apartament(cheltuiala):
    '''
    Getter pentru numarul apartamentului
    :param cheltuiala: cheltuiala
    :return: numarul apartamentului corespunzator cheltuielii
    '''
    return cheltuiala['numar']

def get_suma(cheltuiala):
    '''
    Getter pentru suma reprezentand cheltuiala
    :param cheltuiala: cheltuiala
    :return: suma cheltuielii
    '''
    return cheltuiala['suma']

def get_data(cheltuiala)->str:
    '''
    Getter pentru data la care a fost efectuata cheltuiala
    :param cheltuiala: cheltuiala
    :return: data 
    '''
    return cheltuiala['data']

def get_tip(cheltuiala):
    '''
    Getter pentru cheltuielile corespunzatoare intretinerii apartamentului
    :param cheltuiala: cheltuiala
    :return: cheltuiala legata de intretinere
    '''
    return cheltuiala['tip']

def get_nr_primit(lst_cheltuieli, numar_apartament):
    '''
    Getter pentru a verifica daca un numar de apartament este sau nu in lista data
    :param:lst_cheltuieli - lista cheltuielilor
            numar_apartament- numarul apartamentului a carui verificare se face
    :return: True daca exista numarul apartamentului dat in lista, False in caz contrar
    '''
    for cheltuiala in lst_cheltuieli:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            return True
    return False

def get_str(cheltuiala):
    return f'Apartamentul cu id-ul {get_id(cheltuiala)}, cu numarul de apartament {get_numar_apartament(cheltuiala)}, are o cheltuiala {get_suma(cheltuiala)}, in data de {get_data(cheltuiala)}, cheltuielile legate de intretinere de {get_tip(cheltuiala)}'