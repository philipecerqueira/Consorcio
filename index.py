import os

from CarList import ICar, carList
from RentCar import rentCar
from ReturnCar import returnCar

optionsCar: ICar = [
    {"Chevrolet Onix": 90},
    {"Chevrolet Spin": 150},
    {"Hyundai HB20": 85},
    {"Hyundai Tucson": 120},
    {"Fiat Uno": 60},
    {"Fiat Mobi": 70},
    {"Renault Kiwid": 50},
    {"Renault Sandero": 70},
]
rentedCars: ICar = []
menu = 0

print('************************************')
print('* Bem vindo á locadora de carros! *')
print('************************************')
print('\n')
while (menu == 0):
    print('O que deseja fazer ? ')
    print('0 - Mostrar o portifólio | 1 - Alugar um carro'
          '| 2 - Devolver carro | 3 - Fechar App')
    option = int(input('Digite uma das opções acima:  '))
    print('\n')
    match option:
        case 0:
            carList(optionsCar)

        case 1:
            rentCar(optionsCar, rentedCars)

        case 2:
            returnCar(optionsCar, rentedCars)

        case 3:
            os.system('clear')
            print('Tem certaza que deseja sair? [0 - Não | 1 - Sim]')
            menu = int(input('Digite uma das opções acima:  '))
            os.system('clear')

        case _:
            os.system('clear')
            print('Por favor digite um dos numeros listados')
            print('****************************************')
            print('\n')
