from Domain.cheltuiala import creeaza_cheltuiala, get_data, get_numar_apartament, get_str, get_suma, get_tip
from Logic.adunare_valori import adunare_valoare
from Logic.afisare_sume_apartament import get_suma_apartament
from Logic.crud import create, delete, read, update
from Logic.max_tip_cheltuieli import  get_max_tip_intretinere
from Logic.ordonare import get_ordonare
from Logic.stergere_cheltuieli import stergere_cheltuieli_pentru_un_apartament
from Logic.undo_redo import do_redo, do_undo


def show_menu():
    print('1. CRUD')
    print('2. Stergerea tuturor cheltuielilor pentru un apartament dat')
    print('3. Adunarea unei valori la  toate cheltuielile dintr-o data citita')
    print('4. Maximul cheltuielilor pentru fiecare tip dat.')
    print('5. Ordonarea cheltuielilor descrescator dupa suma.')
    print('6. Afisarea sumelor lunare pentru fiecare apartament')
    print('a. Afisare')
    print('u. Undo')
    print('r. Redo')
    print('x. Exit')

def handle_add(cheltuieli,undo_list, redo_list):
    try:
        id_cheltuiala=int(input('Dati id-ul apartamentului: '))
        numar_apartament=int(input('Dati numarul apartamentului: '))
        suma=int(input('Dati suma cheltuielii: '))
        data=input('Dati data: ')
        tip_cheltuiala=input('Dati tipul cheltuielii(intretinere/alte cheltuieli/canal): ')
        return create(cheltuieli, id_cheltuiala, numar_apartament, suma, data, tip_cheltuiala, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare', ve)
    return cheltuieli

def handle_update(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala=int(input('Dati id-ul cheltuielii care sa se actualizeze: '))
        numar_apartament=int(input('Dati noul numar al apartamentului: '))
        suma=float(input('Dati noua suma: '))
        data=input('Dati noua data: ')
        tip_cheltuiala=input('Dati noul tip de cheltuiala: ')
        updated = creeaza_cheltuiala(id_cheltuiala, numar_apartament, suma, data, tip_cheltuiala)
        return update(cheltuieli, updated, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare ', ve)
    return cheltuieli

def handle_delete(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala=int(input('Dati id-ul pentru care se va sterge: '))
        cheltuieli=delete(cheltuieli, id_cheltuiala, undo_list, redo_list)
        print('Stergerea a fost realizata cu succes. ')
        return cheltuieli
    except ValueError as ve:
        print('Eroare ', ve)
    return cheltuieli

def handle_show_all(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))
        

def handle_show_details(cheltuieli):
    id_cheltuiala= int(input('Dati id-ul pentru care doriti detalii: '))
    cheltuiala = read(cheltuieli, id_cheltuiala)
    print(f'Numar apartament: {get_numar_apartament(cheltuiala)})')
    print(f'Suma: {get_suma(cheltuiala)})')
    print(f'data: {get_data(cheltuiala)})')
    print(f'tip cheltuiala: {get_tip(cheltuiala)})')
   

def handle_stergere_cheltuieli(cheltuieli, undo_list, redo_list):
    try:
        numar_apartament = int(input('Dati numarul apartamentului pentru care se vor sterge cheltuielile: '))
        cheltuieli= stergere_cheltuieli_pentru_un_apartament(cheltuieli, numar_apartament, undo_list,redo_list)
        print('Cheltuielile au fost sterse cu succes')
        return cheltuieli
    except ValueError as ve:
        print('Eroare ', ve)
    
    return cheltuieli

def handle_adaugare_valoare(cheltuieli, undo_list, redo_list):
    try:
        data = input('Dati data pentru care se va aduna o valoare cheltuilelior: ')
        val = int(input('Dati o valoare care sa fie adaugata cheltuilelior din data specificata: '))
        cheltuieli=adunare_valoare(cheltuieli, data, val,undo_list,redo_list)
        print('Cheltuielile au fost modificate cu succes.')
        return cheltuieli
    except ValueError as ve:
        print('Eroare ', ve)

def handle_crud(cheltuieli, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modificare')
        print('a. Afisare')
        print('u. Undo')
        print('r. Redo')
        print('b. Revenire')
        print('d. Detalii cheltuiala')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli=handle_delete(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli=handle_update(cheltuieli, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'u':
            cheltuieli=handle_undo(cheltuieli, undo_list, redo_list)
        elif optiune == 'r':
            cheltuieli=handle_redo(cheltuieli, undo_list, redo_list)
        elif optiune =='d':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else: 
            print('Optiune invalida.')
    return cheltuieli

def handle_max_tip_cheltuieli(cheltuieli):
    result= get_max_tip_intretinere(cheltuieli,[],[])
    for tip_cheltuiala in result:
        print(f'Tipul {tip_cheltuiala} are suma maxima: {result[tip_cheltuiala]}')
   
def handle_afisare_suma_lunara(cheltuieli):
     result=get_suma_apartament(cheltuieli)
     for numar_ap in result:
        print(f'Apartamentul cu numarul {numar_ap}, are cheltuielile lunare  de {result[numar_ap]}')
           


def handle_ordonare_descrescatoare(cheltuieli, undo_list, redo_list):
    ordonate=get_ordonare(cheltuieli,undo_list, redo_list)
    handle_show_all(ordonate)

def handle_undo(cheltuieli, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, cheltuieli)
    if undo_result is not None:
        return undo_result
    return cheltuieli


def handle_redo(cheltuieli, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, cheltuieli)
    if redo_result is not None:
        return redo_result
    return cheltuieli



def run_ui(cheltuieli, undo_list, redo_list):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli=handle_crud(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli=handle_stergere_cheltuieli(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_adaugare_valoare(cheltuieli, undo_list, redo_list)
        elif optiune == '4':
            handle_max_tip_cheltuieli(cheltuieli)
        elif optiune == '5':
            cheltuieli=handle_ordonare_descrescatoare(cheltuieli, undo_list, redo_list)
        elif optiune == '6':
            handle_afisare_suma_lunara(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'u':
            cheltuieli=handle_undo(cheltuieli, undo_list, redo_list)
        elif optiune == 'r':
            cheltuieli=handle_redo(cheltuieli, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return cheltuieli

