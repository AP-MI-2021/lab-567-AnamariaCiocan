from Domain.cheltuiala import get_str
from Logic.crud import create, delete




def show_menu():
    print('Separatorul ";" va fi utilizat pentru a separa comenzile iar "," va fi utilizat pentru a separa datele aferente fiecarei comenzi.')
    print('Pentru stergerea tuturor cheltuielilor unui apartament dat introduceti comanda "delete" urmata de parametrii "cheltuieli" si id-ul cheltuielii')
    print('Pentru adaugarea unei valori la o cheltuiala dintr-o anumita data introduceti comanda "add" urmata de parametrii reprezentand id-numar intreg (trebuie sa fie unic), numarul apartamentului-numar intreg, suma cheltuielii-numar intreg, data(de forma "DD.MM.YYYY"), tipul cheltuielii-string (se poate alege dintre: intretinere, canal, alte cheltuieli)')
    print('Pentru a vizualiza maximul fiecarui tip de cheltuiala introduceti comanda "max" ')
    print('Pentru Exit scrieti x')
    
def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))

def handle_add(cheltuieli, param):
    id_cheltuiala=int(param[1])
    numar_apartament=int(param[2])
    suma=int(param[3])
    data=param[4]
    tip=param[5]
    print('Adaugarea s-a efectuat cu succes')
    return create(id_cheltuiala, numar_apartament, suma, data, tip)
    
def handle_delete(cheltuieli, param):
    new_cheltuieli=delete(cheltuieli, int(param[1]))
    print('Stergerea s-a efectuat cu succes')
    return new_cheltuieli

def run_clc(cheltuieli):
    while True:
        show_menu()
        optiune=input('Introduceti comenzile: ')
        optiuni=optiune.split(';')
        for optiune in optiuni:
            param=optiune.split(',')
            if param[0] == 'show_all':
                handle_show_all(cheltuieli)
            elif param[0] == 'add':
                handle_add(cheltuieli, param)
            elif param[0] == 'delete':
                cheltuieli=handle_delete(cheltuieli,param)
            elif param[0] == 'exit':
                break
            else:
                print('Optiune invalida')
        



