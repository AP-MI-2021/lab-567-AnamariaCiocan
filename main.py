
from Logic.crud import create
from Tests.test_adunare_val import test_adunare_valoare
from Tests.test_crud import test_crud
from Tests.test_max_tip import test_max_tip_cheltuiala
from Tests.test_ordonare import test_ordonare_descrescatoare
from Tests.test_stergere_cheltuieli import test_stergere_cheltuieli
from Tests.test_sume_lunare import test_sum_lunare
from Tests.test_undo_redo import test_undo_redo
from UserInterface.command_line_console import run_clc
from UserInterface.console import run_ui


def main():
    cheltuieli=[]
    undo_list = []
    redo_list = []
    cheltuieli= create(cheltuieli, 6, 23, 200, '29.09.2009', 'intretinere',[],[])
    cheltuieli= create(cheltuieli, 2, 33, 150, '11.11.2020', 'canal',[],[])
    cheltuieli=create(cheltuieli, 3, 23, 170, '12.08.2004', 'alte cheltuieli',[],[])
    cheltuieli=create(cheltuieli, 1, 24, 270, '29.07.2002', 'intretinere',[],[])
    cheltuieli=create(cheltuieli, 5, 23, 400, '28.04.2017', 'alte cheltuieli',[],[])
    cheltuieli=run_ui(cheltuieli, undo_list, redo_list)




if __name__=='__main__':
    test_crud()
    test_stergere_cheltuieli()
    test_adunare_valoare()
    test_ordonare_descrescatoare()
    test_max_tip_cheltuiala()
    test_sum_lunare()
    main()