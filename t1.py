def simple_calc():
    x = float(input('Введите количество часов : '))
    y = float(input('Введите оплатуза 1 час : '))
    c = float(input('Укажите премию - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')
