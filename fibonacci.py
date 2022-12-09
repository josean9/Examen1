def fibonacci(numero):
    valor1 = 0
    valor2 = 1
    intentos = 0
    while True:
        intentos += 1
        valorTotal = valor1 + valor2
        valor2 = valorTotal
        valor1 = valor2
        if intentos == numero:
            print(valorTotal)
            break
        else:   
            print(valorTotal)
            continue
fibonacci(1000000)