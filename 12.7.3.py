per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int (input('Введите сумму вклада: '))
deposit = []
for dep in per_cent:
    deposit.append(per_cent[dep] * money / 100)
print(deposit)
print('Максимальная сумма, которую вы можете заработать:' + str (max(deposit)))
