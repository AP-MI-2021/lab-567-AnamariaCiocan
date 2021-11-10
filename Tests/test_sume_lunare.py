from Logic.afisare_sume_apartament import get_suma_apartament
from Tests.test_crud import get_data


def test_sum_lunare():
    cheltuieli=get_data()
    new_cheltuieli= get_suma_apartament(cheltuieli)
    assert len(new_cheltuieli) == 4
    assert new_cheltuieli[23] == 2100
    assert new_cheltuieli[22] == 2300
    