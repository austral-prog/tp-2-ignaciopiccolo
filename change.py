def change():
        gasto = 23.75
        pago = 100.00

        print("Ingresar gasto:")
        print(gasto)
        print("Dinero recibido")
        print(int(pago))
        print()
        print("Vuelto")
        print()
        vuelto = pago - gasto
        pesos = int(vuelto)
        centavos = int(round((vuelto - pesos) * 100))
        print("Pesos:")
        print(pesos)
        print("Centavos:")
        print(centavos)
change() 

