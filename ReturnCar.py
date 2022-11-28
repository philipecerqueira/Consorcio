import os

from CarList import ICar, carList


def returnCar(optionsCar: ICar, rentedCars: ICar):
    os.system('clear')
    if rentedCars != []:
        continueOrOut = 0
        while (continueOrOut == 0):
            carList(rentedCars)
            print('****************************************')
            print('Selecione o numero do veiculo que deseja devolver')
            vehicle = int(input('Digite uma das opções acima:  '))
            if vehicle < len(rentedCars):
                print('\n')
                selectedCar = rentedCars[vehicle].items()
                for car, value in selectedCar:
                    print(
                        'Você selecionou o Nº '
                        f'{vehicle} - {car}. Valor total R$ {value}')
                print('*************************')
                print('0 - Cancelar | 1 - Confirmar')
                continueOrOut = int(input())
                if continueOrOut == 1:
                    optionsCar.append(rentedCars[vehicle])
                    del rentedCars[vehicle]
                    os.system('clear')
            else:
                os.system('clear')
                print('Por favor digite um dos numeros listados')
                print('****************************************')
                print('\n')
    else:
        os.system('clear')
        print('****************************************')
        print('Nenhum carro alugado')
        print('\n')
