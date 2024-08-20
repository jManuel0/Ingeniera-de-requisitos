class CalcularPagoConsumoAgua:
    # Solicitar al usuario las dimensiones de la alberca y el costo por metro cúbico
    A = float(input("Ingrese el valor de la altura (A) de la alberca en metros: "))
    L = float(input("Ingrese el valor del largo (L) de la alberca en metros: "))
    Ancho = float(input("Ingrese el valor del ancho de la alberca en metros: "))
    Costo_MetroCubico = float(input("Ingrese el costo por metro cúbico de agua: "))

    # Calcular el volumen de la alberca
    Volumen = A * L * Ancho

    # Calcular el pago total por el consumo de agua
    Pago = Volumen * Costo_MetroCubico

    # Mostrar el resultado
    print(f"El volumen de la alberca es: {Volumen:.2f} metros cúbicos")
    print(f"El pago total por llenar la alberca es: {Pago:.2f} moneda")