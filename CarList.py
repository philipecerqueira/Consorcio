ICar = list[dict[str, int]]


def carList(optionsCar: ICar):
    for idx, item in enumerate(optionsCar):
        car, value = next(iter(item.items()))
        print(f'[{idx}] {car} - R$ {value} / dia.')
    print('\n')
