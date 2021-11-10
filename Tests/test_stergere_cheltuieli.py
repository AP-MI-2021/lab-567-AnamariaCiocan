from Logic.crud import create, read
from Logic.stergere_cheltuieli import stergere_cheltuieli_pentru_un_apartament
from Tests.test_crud import get_data


def test_stergere_cheltuieli():
    cheltuieli=get_data()

    new_cheltuieli=stergere_cheltuieli_pentru_un_apartament(cheltuieli, 22,[],[])

    assert len(new_cheltuieli)==len(cheltuieli)-1
    assert read(new_cheltuieli, 3) is None
    assert read(cheltuieli, 3) is not None
    try:
        new_cheltuieli=stergere_cheltuieli_pentru_un_apartament(cheltuieli, 28, [],[])
        assert False
    except ValueError:
        assert True

    