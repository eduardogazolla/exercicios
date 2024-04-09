def fibonacci(n):
    fib = [0, 1] 
    while fib[-1] <= n: 
        fib.append(fib[-1] + fib[-2]) 
    return fib

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
sequencia_fibonacci = fibonacci(numero)
mensagem = verifica_pertence(numero, sequencia_fibonacci)

print(mensagem)