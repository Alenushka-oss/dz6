import json
import os

wallet = []
FILE_NAME = 'wallet.json'
if os.path.exists(FILE_NAME):
    with open (FILE_NAME, 'r') as f:
        wallet = json.load(f)

costs = {}
FILE_COSTS = 'costs.json'
if os.path.exists(FILE_COSTS):
    with open (FILE_COSTS, 'r') as f:
        costs = json.load(f)

income = 0
BILL = 'income.json'
if os.path.exists(BILL):
    with open (BILL, 'r') as f:
        income = json.load(f)

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. история пополнений')
    print('5. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        addition = int(input("Введите сумму пополнения: "))
        wallet.append(addition)
        income += addition
        continue

    elif choice == '2':
        purchase = int(input("Введите сумму покупки: "))
        if income >= purchase:
            name__purchase = input("Введите название покупки: ")
            costs[name__purchase] = purchase
            income -= purchase
            continue
        else:
            print("Денег не хватает!")
            continue

    elif choice == '3':
        for key, value in costs.items():
            print(key, value)
        continue

    elif choice == '4':
        print(*wallet)
        continue

    elif choice == '5':
        with open(FILE_NAME, 'w') as f:
            json.dump(wallet,f)

        with open(FILE_COSTS, 'w') as f:
            json.dump(costs, f)

        # на случай если денег не хватает. Считает количесво денег в кошельке.
        with open(BILL, 'w') as f:
            json.dump(income, f)

        break
    else:
        print('Неверный пункт меню!')