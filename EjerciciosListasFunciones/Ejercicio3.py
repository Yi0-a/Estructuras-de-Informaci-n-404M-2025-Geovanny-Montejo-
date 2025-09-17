def fibonacci(cantidad):
    lista = []
    a, b = 0, 1
    for i in range(cantidad):
        lista.append(a)
        a, b = b, a + b
    return lista

cantidad = int(input("Ingrese la cantidad de numeros de la serie Fibonacci: "))
resultado = fibonacci(cantidad)
print("Serie Fibonacci:", resultado)
