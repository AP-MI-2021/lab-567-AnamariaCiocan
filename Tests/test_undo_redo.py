from Domain.cheltuiala import creeaza_cheltuiala
from Logic.crud import create
from Logic.undo_redo import do_undo



def test_undo_redo():
    cheltuieli=[]
    undo_list = []
    redo_list = []
    cheltuieli = create(cheltuieli, 24, 18, 445, "08.04.2006", "intretinere", undo_list,redo_list)
    cheltuieli = create(cheltuieli, 37, 89, 1000, "10.11.2021", "canal", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 6, 3, 900, "03.12.2010", "alte cheltuieli", undo_list,redo_list)
    cheltuieli = do_undo(cheltuieli, undo_list,redo_list)
   