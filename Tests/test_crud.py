from Domain.cheltuiala import creeaza_cheltuiala, get_id
from Logic.crud import create, delete, read, update


def test_create():
    cheltuieli=get_data()
    params = (13, 12, 1500, '27.08.2020', 800, 300, 400)
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli=create(cheltuieli, *params)
    assert len(new_cheltuieli) == len(cheltuieli)+1
    found=False
    for cheltuiala in new_cheltuieli:
        if cheltuiala == c_new:
            found=True
    assert found


def get_data():
    return [
        creeaza_cheltuiala(1, 23, 2100, '24.05.2020', 1000, 500, 600),
        creeaza_cheltuiala(2, 11, 1900, '28.07.2021', 900, 300, 700),
        creeaza_cheltuiala(3, 22, 2300, '28.09.2021', 1100, 600, 600),
        creeaza_cheltuiala(4, 20, 1300, '21.10.2021', 800, 200, 300)
    ]

def test_read():
    cheltuieli=get_data()
    some_c=cheltuieli[1]
    assert read(cheltuieli, get_id(some_c)) == some_c
    assert read(cheltuieli, None) == cheltuieli


def test_update():
    cheltuieli = get_data()
    c_updated = creeaza_cheltuiala(1, 11, 2400, '31.09.2020', 1500, 400, 500)
    updated =update(cheltuieli, c_updated)
    assert c_updated in updated 
    assert c_updated not in cheltuieli
    assert len(updated) == len(cheltuieli)

def test_delete():
    cheltuieli=get_data()
    to_delete = 3
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()