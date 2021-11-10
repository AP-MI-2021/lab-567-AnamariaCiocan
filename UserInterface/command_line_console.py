from Domain.cheltuiala import get_str
from Logic.crud import create, delete
from Logic.max_tip_cheltuieli import get_max_tip_intretinere



def show_menu():
    print('Separatorul ";" va fi utilizat pentru a separa comenzile iar "," va fi utilizat pentru a separa datele aferente fiecarei comenzi.')
    print('1. Pentru stergerea tuturor cheltuielilor unui apartament dat introduceti comanda "delete" urmata de parametrii "cheltuieli" si id-ul cheltuielii')
    print('2. Pentru adaugarea unei valori la o cheltuiala dintr-o anumita data introduceti comanda "add" urmata de parametrii reprezentand id-numar intreg (trebuie sa fie unic), numarul apartamentului-numar intreg, suma cheltuielii-numar intreg, data(de forma "DD.MM.YYYY"), tipul cheltuielii-string (se poate alege dintre: intretinere, canal, alte cheltuieli)')
    print('Pentru a vizualiza maximul fiecarui tip de cheltuiala introduceti comanda "max" ')
    print('x. Exit')
    
def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))



def run_clc(cheltuieli):
    while True:
        show_menu()
        comanda=input('Alegeti comenzile: ')
        comenzi=comanda.split(';')
        for optiune in comenzi:
            param=optiune.split(',')
            if param[0] == 'show_all':
                handle_show_all(cheltuieli)
            elif param[0] == 'add':
                cheltuieli=create(cheltuieli, param[1], param[2], param[3], param[4], param[5])
            elif param[0] == 'delete':
                id=param[1]
                cheltuieli=delete(cheltuieli, id)
            elif param[0] == 'exit':
                break
            else:
                print('Optiune invalida')
        return cheltuieli



