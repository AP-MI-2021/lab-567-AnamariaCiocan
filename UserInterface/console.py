from Domain.cheltuiala import get_data, get_numar_apartament, get_str, get_suma, get_tip_alte_cheltuieli, get_tip_canal, get_tip_intretinere
from Logic.adunare_valori import adunare_valoare
from Logic.afisare_sume_apartament import get_suma_apartament
from Logic.crud import create, delete, read
from Logic.max_tip_cheltuieli import get_max_tip_alte_cheltuieli, get_max_tip_canal, get_max_tip_intretinere
from Logic.stergere_cheltuieli import stergere_cheltuieli_pentru_un_apartament


def show_menu():
    print('1. CRUD')
    print('2. Stergerea tuturor cheltuielilor pentru un apartament dat')
    print('3. Adunarea unei valori la  toate cheltuielile dintr-o data citita')
    print('4. Maximul cheltuielilor pentru fiecare tip dat.')
    print('6. Afisarea sumelor lunare pentru fiecare apartament')
    print('x. Exit')

def handle_add(cheltuieli):
    try:
        id_cheltuiala=int(input('Dati id-ul apartamentului: '))
        numar_apartament=int(input('Dati numarul apartamentului: '))
        suma=int(input('Dati suma cheltuielii: '))
        data=input('Dati data: ')
        tip_intretinere=int(input('Dati cheltuielile intretinerii: '))
        tip_canal=int(input('Dati cheltuielile de tip canal: '))
        tip_alte_cheltuieli=int(input('Dati alte cheltuieli: '))
        return create(cheltuieli, id_cheltuiala, numar_apartament, suma, data, tip_intretinere, tip_canal, tip_alte_cheltuieli)
    except ValueError as ve:
        print('Eroare', ve)
    return cheltuieli

def handle_update(cheltuieli):
    try:
        id_cheltuiala=int(input('Dati id-ul cheltuielii care sa se actualizeze: '))
        numar_apartament=int(input('Dati noul numar al apartamentului: '))
        suma=int(input('Dati noua suma: '))
        data=input('Dati noua data: ')
        tip_intretinere=int(input('Dati noua cheltuiala de tip intretinere: '))
        tip_canal=int(input('Dati noua cheltuiala de tip canal: '))
        tip_alte_cheltuieli=int(input('Dati noua suma a altor cheltuieli: '))
    except ValueError as ve:
        print('Eroare ', ve)
    return cheltuieli

def handle_delete(cheltuieli):
    try:
        id_cheltuiala=int(input('Dati id-ul pentru care se va sterge: '))
        cheltuieli=delete(cheltuieli, id_cheltuiala)
        print('Stergerea a fost realizata cu succes. ')
    except ValueError as ve:
        print('Eroare ', ve)
    return cheltuieli

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

def handle_stergere_cheltuieli(cheltuieli):
    try:
        numar_apartament = input('Dati numarul apartamentului pentru care se vor sterge cheltuielile: ')
        cheltuieli= stergere_cheltuieli_pentru_un_apartament(cheltuieli, numar_apartament)
        print('Cheltuielile au fost sterse cu succes')
    except ValueError as ve:
        print('Eroare ', ve)
    return cheltuieli

def handle_adaugare_valoare(cheltuieli):
    data = input('Dati data pentru care se va aduna o valoare cheltuilelior: ')
    val = input('Dati o valoare care sa fie adaugata cheltuilelior din data specificata: ')
    cheltuieli=adunare_valoare(cheltuieli, data, val)
    print('Cheltuielile au fost modificate cu succes.')
    return cheltuieli

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
        elif optiune == '2':
            cheltuieli=handle_delete(cheltuieli)
        elif optiune == '3':
            cheltuieli=handle_update(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune =='d':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else: 
            print('Optiune invalida.')
    return cheltuieli

def handle_max_tip_cheltuieli(cheltuieli):
    result= get_max_tip_intretinere(cheltuieli)
    print(f'Pentru tipul intretinere:')
    for intretinere in result:
        print(f'{intretinere}: {get_str(result[intretinere])}')
    result1=get_max_tip_canal(cheltuieli)
    print(f'Pentru tipul canal: ')
    for canal in result1:
        print(f'{canal}: {get_str(result1[canal])}')
    result2=get_max_tip_alte_cheltuieli(cheltuieli)
    print(f'Pentru alt tip de cheltuieli: ')
    for alte_cheltuieli in result2:
        print(f'{alte_cheltuieli}: {get_str(result2[alte_cheltuieli])}')

def handle_afisare_suma_lunara(cheltuieli):
    result=get_suma_apartament(cheltuieli)
    for numar_apartament in result:
        print(f'{numar_apartament}: {get_str(result[numar_apartament])}')

def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli=handle_stergere_cheltuieli(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_adaugare_valoare(cheltuieli)
        elif optiune == '4':
            handle_max_tip_cheltuieli(cheltuieli)
        elif optiune == '6':
            handle_afisare_suma_lunara(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return cheltuieli

