def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Returneaza lista inaintea apelarii unei functionalitati care a returnat o noua lista
    :param undo_list:lista care se modifica in urma apelarii unei functionalitati
    :param redo_list:lista ce se modifica in urma apelarii functiei undo
    :param current_list:lista curenta
    :return:lista noua dupa apelarea undo
    """
    if undo_list:
        redo_list.append(current_list)
        return undo_list.pop()

    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Lista care se formeaza inaintea apelarii functiei undo, si se apeleaza doar daca undo a fost folosita macar o data
    :param undo_list:lista care se modifica in urma apelarii unei functionalitati
    :param redo_list:lista care se modifica in urma apelarii functiei redo
    :param current_list:lista curenta
    :return:lista dupa apelare
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo

    return None