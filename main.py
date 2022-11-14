coupe_count = 99
seats_per_coupe = 4
number = int(input('Введите номер места: '))
print(f'Номер купе: {((number - 1) // seats_per_coupe) + 1}')
