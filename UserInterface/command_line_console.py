from Domain.cheltuiala import get_str
from Logic.crud import create, delete




def show_menu():
    print('Separatorul ";" va fi utilizat pentru a separa comenzile iar "," va fi utilizat pentru a separa datele aferente fiecarei comenzi.')
    print('Pentru stergerea tuturor cheltuielilor unui apartament dat introduceti comanda "delete" urmata de parametrii "cheltuieli" si id-ul cheltuielii')
    print('Pentru adaugarea unei valori la o cheltuiala dintr-o anumita data introduceti comanda "add" urmata de parametrii reprezentand id-numar intreg (trebuie sa fie unic), numarul apartamentului-numar intreg, suma cheltuielii-numar intreg, data(de forma "DD.MM.YYYY"), tipul cheltuielii-string (se poate alege dintre: intretinere, canal, alte cheltuieli)')
    print('Pentru a vizualiza maximul fiecarui tip de cheltuiala introduceti comanda "max" ')
    print('Pentru a vizualiza toate cheltuielile inregistrate introduceti:  show_all')
    print('Pentru Exit scrieti x')
    

def run_clc(cheltuieli, undo_list, redo_list):
    while True:
        show_menu()
        optiune=input('Introduceti comenzile: ')
        comanda=optiune.split(';')
        for elem in comanda:
            param=elem.split(',')
            if param[0] == 'show_all':
                for opt in cheltuieli:
                    print(get_str(opt))
            elif param[0] == 'add':
               try:
                   cheltuieli=create(cheltuieli, int(param[1]), int(param[2]), int(param[3]), param[4], param[5], undo_list, redo_list)
               except ValueError as ve:
                    print('Eroare ', ve)
            elif param[0] == 'delete':
                try:
                    cheltuieli=delete(cheltuieli, int(param[1]), undo_list, redo_list)
                except ValueError as ve:
                    print('Eroare ', ve)
            elif param[0] == 'exit':
                break
            else:
                print('Optiune invalida')
        



