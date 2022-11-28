import os

from CarList import ICar, carList


def rentCar(optionsCar: ICar, rentedCars: ICar):
    os.system('clear')
    continueOrOut = 0
    while (continueOrOut == 0):
        carList(optionsCar)
        print('****************************************')
        print('Selecione o numero do veiculo desejado')
        vehicle = int(input('Digite uma das opções acima:  '))
        if vehicle < len(optionsCar):
            vehicleDays = int(
                input('Selecione o numero dias'
                      ' que deseja ficar com o veiculo:  '))
            print('\n')
            selectedCar = optionsCar[vehicle].items()
            car, value = next(iter(selectedCar))
            valueTotal = vehicleDays * int(value)
            print(
                'Você selecionou o Nº'
                f'{vehicle} - {car}. Valor total R$ {valueTotal}')
            print('******************************')
            print('0 - Cancelar | 1 - Confirmar')
            continueOrOut = int(input())
        else:
            os.system('clear')
            print('Por favor digite um dos numeros listados')
            print('****************************************')
            print('\n')
    if continueOrOut == 1:
        optionsCar[vehicle][car] = valueTotal
        rentedCars.append(optionsCar[vehicle])
        del optionsCar[vehicle]
        os.system('clear')
