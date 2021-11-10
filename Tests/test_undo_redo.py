from Domain.cheltuiala import creeaza_cheltuiala
from Logic.crud import create, read
from Logic.undo_redo import do_redo, do_undo



def test_undo_redo():
    cheltuieli=[]
    undo_lst = []
    redo_lst = []
    cheltuieli=create(cheltuieli, 1, 22, 1000, '24.10.2020', 'intretinere', undo_lst, redo_lst)
    cheltuieli=create(cheltuieli, 2, 11, 2400, '25.09.2019', 'alte cheltuieli', undo_lst, redo_lst)
    cheltuieli=create(cheltuieli, 3, 26, 500, '29.09.2011', 'canal', undo_lst, redo_lst)
    if len(undo_lst)!=0:
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
    assert read(cheltuieli, 1) is None
    assert read(cheltuieli, 2) is None
    assert read(cheltuieli, 3) is None
    cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
    assert read(cheltuieli, 1) is None
    cheltuieli=create(cheltuieli, 1, 22, 2400, '21.10.2014', 'intretinere', undo_lst, redo_lst)
    cheltuieli=create(cheltuieli, 2, 24, 100, '25.02.2021', 'canal', undo_lst, redo_lst)
    cheltuieli=create(cheltuieli, 3, 12, 200, '22.10.2020', 'alte cheltuieli', undo_lst, redo_lst)
    if len(redo_lst)!=0:
        cheltuieli=do_redo(undo_lst, redo_lst, cheltuieli)
    assert cheltuieli[0] == [1, 22, 2400, '21.10.2014', 'intretinere']
    if len(undo_lst)>0:
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
    assert read(cheltuieli, 3) is None
    assert cheltuieli[1]==[2, 24, 100, '25.02.2021', 'canal']
    if len(undo_lst)>0:
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
    assert read(cheltuieli, 1) is None
    if len(redo_lst)>0:
        cheltuieli=do_redo(undo_lst, redo_lst, cheltuieli)
    assert cheltuieli[1]==[2, 24, 100, '25.02.2021', 'canal']
    assert read(cheltuieli, 3) is None
    if len(redo_lst)>0:
        cheltuieli=do_redo(undo_lst, redo_lst, cheltuieli)
    assert cheltuieli[2]==[3, 12, 200, '22.10.2020', 'alte cheltuieli']
    if len(undo_lst)>0:
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
    assert read(cheltuieli, 2) is None
    assert read(cheltuieli, 3) is None
    cheltuieli=create(cheltuieli, 4, 21, 100, '25.05.2005', 'intretinere', undo_lst, redo_lst)
    if len(undo_lst)>0:
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
        cheltuieli=do_undo(undo_lst, redo_lst, cheltuieli)
    assert read(cheltuieli, 1) is None
    if len(redo_lst)>0:
        cheltuieli=do_redo(undo_lst, redo_lst, cheltuieli)
    assert cheltuieli[0]==[1, 22, 2400, '21.10.2014', 'intretinere']
    if len(redo_lst)>0:
        cheltuieli=do_redo(undo_lst, redo_lst, cheltuieli)