notas = []

print("Por favor, ingrese 3 notas.")
for i in range(3):
    nota_ingresada = float(input(f"Ingresa la nota {i + 1}: "))
    notas.append(nota_ingresada)

suma_total = sum(notas)
cantidad_elementos = len(notas)
promedio = suma_total / cantidad_elementos

print(f"Las notas ingresadas fueron: {notas}")
print(f"El promedio de las notas es: {promedio:.2f}")