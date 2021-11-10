from Domain.cheltuiala import get_suma
from Logic.ordonare import get_ordonare
from Tests.test_crud import get_data


def test_ordonare_descrescatoare():
    cheltuieli=get_data()
    new_cheltuieli= get_ordonare(cheltuieli,[],[])
    assert len(new_cheltuieli)==len(cheltuieli)
    assert get_suma(new_cheltuieli[0]) == 2300
    assert get_suma(cheltuieli[0]) == 2100
    assert get_suma(new_cheltuieli[3]) == 1300
    assert get_suma(cheltuieli[3]) == 1300