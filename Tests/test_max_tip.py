from Domain.cheltuiala import get_suma
from Logic.max_tip_cheltuieli import get_max_tip_intretinere
from Tests.test_crud import get_data


def test_max_tip_cheltuiala():
    cheltuieli=get_data()
    new_cheltuieli=get_max_tip_intretinere(cheltuieli,[],[])
    assert len(new_cheltuieli)==3
    assert new_cheltuieli['canal'] == 1900
    assert new_cheltuieli['intretinere']==2300
    