ticket_count = int (input("Внимание: При покупке от 4х билетов действует скидка 10% от суммы заказа. \n"
                          " Введите количество билетов: "))
total = 0
for i in range (ticket_count):
    age = int (input("Введите возраст: "))
    if 18<age<25:
        total +=990
    elif age > 25:
        total += 1390
if ticket_count >= 4:
    total_dicount = total * 0.90
else:
    total_dicount = total

if total_dicount != total:
    print('Цена без скидки:',  total, "рублей")
    print('Цена со скидкой в 10%:', total_dicount, "рублей")
else:
    print('Цена билетов:', total, "рублей")