from Domain.cheltuiala import get_data, get_numar_apartament, get_str, get_suma, get_tip_alte_cheltuieli, get_tip_canal, get_tip_intretinere
from Logic.crud import create, read


def show_menu():
    print('1. CRUD')
    print('2. Stergereatuturor cheltuielilor pentru un apartament dat')
    print('x. Exit')

def handle_add(cheltuieli):
    id_cheltuiala=int(input('Dati id-ul apartamentului: '))
    numar_apartament=int(input('Dati numarul apartamentului: '))
    suma=int(input('Dati suma cheltuielii: '))
    data=int(input('Dati data: '))
    tip_intretinere=int(input('Dati cheltuielile intretinerii: '))
    tip_canal=int(input('Dati cheltuielile de tip canal: '))
    tip_alte_cheltuieli=int(input('Dati alte cheltuieli: '))
    return create(cheltuieli, id_cheltuiala, suma, data, tip_intretinere, tip_canal, tip_alte_cheltuieli)

def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))

def handle_show_details(cheltuieli):
    id_cheltuiala= int(input('Dati id-ul pentru care doriti detalii: '))
    cheltuiala = read(cheltuieli, id_cheltuiala)
    print(f'Numar apartament: {get_numar_apartament(cheltuiala)})')
    print(f'Suma: {get_suma(cheltuiala)})')
    print(f'data: {get_data(cheltuiala)})')
    print(f'tip intretinere: {get_tip_intretinere(cheltuiala)})')
    print(f'tip canal: {get_tip_canal(cheltuiala)})')
    print(f'tip alte cheltuieli: {get_tip_alte_cheltuieli(cheltuiala)})')

def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modificare')
        print('a. Afisare')
        print('b. Revenire')
        print('d. Detalii cheltuiala')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune =='d':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else: 
            print('Optiune invalida.')
    return cheltuieli


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            handle_crud(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return cheltuieli

