class ConvertirMetreosAPulgadas:
    PULGADA_POR_METRO = 39.3701  # 1 metro = 39.3701 pulgadas

    metros = float(input("Ingrese la cantidad de metros de tela: "))

    pulgadas = metros * PULGADA_POR_METRO

    print(f"La cantidad de tela en pulgadas es: {pulgadas:.2f}")