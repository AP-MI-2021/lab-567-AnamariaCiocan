from Domain.cheltuiala import get_suma, get_tip_alte_cheltuieli, get_tip_canal, get_tip_intretinere


def get_max_tip_intretinere(lst_cheltuieli):
    '''
    return: un dictionar in care cheia este tipul intretinerii si valoarea este cheltuiala cu suma de cheltuieli maxima
    '''
    result={}
    for cheltuiala in lst_cheltuieli:
        intretinere=get_tip_intretinere(cheltuiala)
        if intretinere not in result:
            result[intretinere]=cheltuiala
        else:
            if intretinere > get_tip_intretinere(result[intretinere]):
                result[intretinere]=cheltuiala
    return result

def get_max_tip_canal(lst_cheltuieli):
    '''
    return: un dictionar in care cheia este tipul intretinerii si valoarea este cheltuiala cu suma de cheltuieli maxima
    '''
    result={}
    for cheltuiala in lst_cheltuieli:
        canal=get_tip_canal(cheltuiala)
        if canal not in result:
            result[canal]=cheltuiala
        else:
            if canal > get_tip_canal(result[canal]):
                result[canal]=cheltuiala
    return result

def get_max_tip_alte_cheltuieli(lst_cheltuieli):
    '''
    return: un dictionar in care cheia este tipul intretinerii si valoarea este cheltuiala cu suma de cheltuieli maxima
    '''
    result2={}
    for cheltuiala in lst_cheltuieli:
        alte_cheltuieli=get_tip_alte_cheltuieli(cheltuiala)
        if alte_cheltuieli not in result2:
            result2[alte_cheltuieli]=cheltuiala
        else:
            if alte_cheltuieli > get_tip_alte_cheltuieli(result2[alte_cheltuieli]):
                result2[alte_cheltuieli]=cheltuiala
    return result2
