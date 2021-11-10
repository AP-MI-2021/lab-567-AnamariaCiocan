from Domain.cheltuiala import get_suma
from Logic.adunare_valori import adunare_valoare
from Tests.test_crud import get_data


def test_adunare_valoare():
    cheltuieli=get_data()
    valoare=20
    data='24.05.2020'
    cheltuieli=adunare_valoare(cheltuieli, data, valoare,[],[])
    assert len(cheltuieli) == 4
    assert get_suma(cheltuieli[0]) == 2120
    assert get_suma(cheltuieli[1]) == 1900


    