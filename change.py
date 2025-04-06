def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))
    print(expense)
    print(int(money))
    print(pesos)
    print(centavos)
