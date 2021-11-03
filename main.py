
from Logic.crud import create
from Tests.test_crud import test_crud
from UserInterface.console import run_ui


def main():
    cheltuieli=[]
    cheltuieli= create(cheltuieli, 1, 23, 200, '29.09.2009', 50, 30, 50)
    cheltuieli= create(cheltuieli, 2, 33, 150, '11.11.2020', 90, 40, 20)
    cheltuieli=create(cheltuieli, 3, 24, 170, '12.08.2004', 100, 30, 70)
    cheltuieli=run_ui(cheltuieli)




if __name__=='__main__':
    test_crud()
    main()