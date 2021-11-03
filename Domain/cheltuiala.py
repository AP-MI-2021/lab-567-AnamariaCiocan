def creeaza_cheltuiala(id_cheltuiala:int, numar_apartament:int, suma, data, tip_intretinere, tip_canal, tip_alte_cheltuieli):
    '''
    Creeaza o cheltuiala.
    :param id_apartament: id-ul unei cheltuieli
    :param numar_apartament: numarul apartamentului
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tip_intretinere: cheltuiala de tip intretinere
    :param tip_canal: cheltuiala de tip canal
    :param tip_alte_cheltuieli: cheltuiala de alt tip
    :return: o cheltuiala
    '''
    return {
        'id': id_cheltuiala,
        'numar': numar_apartament,
        'suma': suma,
        'data': data,
        'intretinere': tip_intretinere,
        'canal': tip_canal,
        'alte_cheltuieli': tip_alte_cheltuieli,
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

def get_tip_intretinere(cheltuiala):
    '''
    Getter pentru cheltuielile corespunzatoare intretinerii apartamentului
    :param cheltuiala: cheltuiala
    :return: cheltuiala legata de intretinere
    '''
    return cheltuiala['intretinere']

def get_tip_canal(cheltuiala):
    '''
    Getter pentru cheltuielile necesare pentru canal
    :param cheltuiala: cheltuiala
    :return: cheltuiala pentru canal
    '''
    return cheltuiala['canal']

def get_tip_alte_cheltuieli(cheltuiala):
    '''
    Getter pentru cheltuielile suplimentare necesare unui apartament
    :param cheltuiala: cheltuiala
    :return: cheltuiala altor necesitati
    '''
    return cheltuiala['alte_cheltuieli']

def get_str(cheltuiala):
    return f'Apartamentul cu id-ul {get_id(cheltuiala)}, cu numarul de apartament {get_numar_apartament(cheltuiala)}, are o cheltuiala {get_suma(cheltuiala)}, in data de {get_data(cheltuiala)}, cheltuielile legate de intretinere de {get_tip_intretinere(cheltuiala)}, de canal de {get_tip_canal(cheltuiala)}, plus alte cheltuieli {get_tip_alte_cheltuieli(cheltuiala)}'