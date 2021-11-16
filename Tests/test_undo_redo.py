
from Logic.crud import create
from Logic.undo_redo import do_redo, do_undo
from UserInterface.console import handle_redo, handle_undo



def test_undo_redo():
    cheltuieli=[]
    undo_lst = []
    redo_lst = []
    cheltuieli=create(cheltuieli, 1, 22, 1000, '24.10.2020', 'intretinere', undo_lst, redo_lst)#add o1 -2
    assert len(cheltuieli)==1
    cheltuieli=create(cheltuieli, 2, 11, 2400, '25.09.2019', 'alte cheltuieli', undo_lst, redo_lst)#add o2 -3
    cheltuieli=create(cheltuieli, 3, 26, 500, '29.09.2011', 'canal', undo_lst, redo_lst)#add o3 -4
    assert len(cheltuieli)==3
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [o1, o2] -5
    assert len(cheltuieli)==2
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [o1] -6
    assert len(cheltuieli)==1
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [] -7

    assert len(cheltuieli)==0
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [] -8
   # assert len(cheltuieli)==0
    cheltuieli=create(cheltuieli, 1, 22, 2400, '21.10.2014', 'intretinere', undo_lst, redo_lst)#add o1 -9
    cheltuieli=create(cheltuieli, 2, 24, 100, '25.02.2021', 'canal', undo_lst, redo_lst)#add o2-9
    cheltuieli=create(cheltuieli, 3, 12, 200, '22.10.2020', 'alte cheltuieli', undo_lst, redo_lst)#add o3-9
    
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo - nu se modifica lista-10
    assert len(cheltuieli)==3
    assert cheltuieli[0] == [1, 22, 2400, '21.10.2014', 'intretinere']
  
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo-11
    assert len(cheltuieli)==2
    assert cheltuieli[1]==[2, 24, 100, '25.02.2021', 'canal']
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [o1]-11
    assert len(cheltuieli)==1
    
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo -> [o1, o2]-12
    assert cheltuieli[1]==[2, 24, 100, '25.02.2021', 'canal']
    assert len(cheltuieli)==2
    
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo -> [o1, o2, o3]-13
    assert cheltuieli[2]==[3, 12, 200, '22.10.2020', 'alte cheltuieli']
    assert len(cheltuieli)==3
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo-14
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [o1]-14
    assert len(cheltuieli)==1
   
    cheltuieli=create(cheltuieli, 4, 21, 100, '25.05.2005', 'intretinere', undo_lst, redo_lst)#add o4 -15
    assert len(cheltuieli)==2
    
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo - nu se modifica nimic -16
    assert len(cheltuieli)==2
   
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [o1] -17
    assert len(cheltuieli)==1
    
    cheltuieli=handle_undo(cheltuieli, undo_lst, redo_lst)#undo -> [] -18
    assert len(cheltuieli)==0
   
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo -> [o1]-19.1
    
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo -> [o1,o2]-19.2
    assert  len(cheltuieli)==2
   
    cheltuieli=handle_redo(cheltuieli, undo_lst, redo_lst)#redo - nu modifica nimic -20