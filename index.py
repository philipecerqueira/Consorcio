import os

print('************************************')
print('* Bem vindo á locadora de carros! *')
print('************************************')
print('\n')

optionsCar = [
    {"Chevrolet Onix": 90},
    {"Chevrolet Spin": 150},
    {"Hyundai HB20": 85},
    {"Hyundai Tucson": 120},
    {"Fiat Uno": 60},
    {"Fiat Mobi": 70},
    {"Renault Kiwid": 50},
    {"Renault Sandero": 70},
]

menu = 0
rentedCars: list = []

while (menu == 0):
    print('O que deseja fazer ? ')
    print('0 - Mostrar o portifólio | 1 - Alugar um carro'
          '| 2 - Devolver carro | 3 - Fechar App')
    option = int(input('Digite uma das opções acima:  '))
    print('\n')
    match option:
        case 0:
            for idx, item in enumerate(optionsCar):
                car, value = next(iter(item.items()))
                print(f'[{idx}] {car} - R$ {value} / dia.')
            print('\n')
        case 1:
            os.system('clear')
            continueOrOut = 0
            while (continueOrOut == 0):
                for idx, item in enumerate(optionsCar):
                    car, value = next(iter(item.items()))
                    print(f'[{idx}] {car} - R$ {value} / dia.')
                print('\n')
                print('****************************************')
                print('Selecione o numero do veiculo desejado')
                vehicle = int(input('Digite uma das opções acima:  '))
                if vehicle < len(optionsCar):
                    vehicleDays = int(
                        input('Selecione o numero dias que deseja ficar com o veiculo:  '))
                    print('\n')
                    selectedCar = optionsCar[vehicle].items()
                    car, value = next(iter(selectedCar))
                    print(
                        f'Você selecionou o Nº{vehicle} - {car}. Valor total R$ {vehicleDays * int(value)}')
                    print('******************************')
                    print('0 - Cancelar | 1 - Confirmar')
                    continueOrOut = int(input())
                else:
                    os.system('clear')
                    print('Por favor digite um dos numeros listados')
                    print('****************************************')
                    print('\n')
            if continueOrOut == 1:
                optionsCar[vehicle][car] = vehicleDays * int(value)
                rentedCars.append(optionsCar[vehicle])
                del optionsCar[vehicle]
                os.system('clear')
        case 2:
            os.system('clear')
            if rentedCars != []:
                continueOrOut = 0
                while (continueOrOut == 0):
                    for idx, item in enumerate(rentedCars):
                        car, value = next(iter(item.items()))
                        print(f'[{idx}] {car} - Valor total R$ {value}.')
                    print('\n')
                    print('****************************************')
                    print('Selecione o numero do veiculo que deseja devolver')
                    vehicle = int(input('Digite uma das opções acima:  '))
                    if vehicle < len(rentedCars):
                        print('\n')
                        selectedCar = rentedCars[vehicle].items()
                        for car, value in selectedCar:
                            print(
                                f'Você selecionou o Nº{vehicle} - {car}. Valor total R$ {value}')
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
