def decimal_a_binario():
    numeros_decimales = input("Ingrese los números decimales que desea convertir  separados por espacios: ").split()
    binarios = []

    for numero_decimal in numeros_decimales:
        numero_decimal = int(numero_decimal)
        pila = []

        # Manejo del caso especial para el número 0
        if numero_decimal == 0:
            binarios.append('0')
        else:
            while numero_decimal > 0:
                residuo = numero_decimal % 2
                pila.append(str(residuo))
                numero_decimal = numero_decimal // 2

            binario = ''
            while len(pila) > 0:
                binario += pila.pop()

            binarios.append(binario)

    return binarios

resultados_binarios = decimal_a_binario()
print("Los números binarios  son:", resultados_binarios)
