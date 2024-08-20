print("Registro")
produccionLitros = input("Digitar la producción en litros: ")
print("Conversión")
conversion = int(produccionLitros) * 3.785

print("Precio por galón")
costo = input("Poner valor: ")

print("Ganancias")
ganancias = conversion * float(costo)
print("La ganancia del producto es:", ganancias)
