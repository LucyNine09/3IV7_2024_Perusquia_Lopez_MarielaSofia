def decimal_a_binario(numero):
    if numero == 0:
        return "0"

    binario = ""
    negativo = False

    if numero < 0:
        negativo = True
        numero = -numero

    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    if negativo:
        binario = "-" + binario

    return binario

def binario_a_decimal(binario):
    negativo = binario[0] == '-'
    if negativo:
        binario = binario[1:]

    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)

    if negativo:
        decimal = -decimal

    return decimal

print("Elija una opción:")
print("1. Convertir decimal a binario")
print("2. Convertir binario a decimal")
opcion = input("Opción: ")

if opcion == "1":
    numero = int(input("Ingrese un número decimal: "))
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
elif opcion == "2":
    binario = input("Ingrese un número binario: ")
    decimal = binario_a_decimal(binario)
    print(f"El número {binario} en decimal es: {decimal}")
else:
    print("Opción no válida")
