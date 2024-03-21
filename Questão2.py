def fibonacci(n):
  """
  Função que calcula a sequência de Fibonacci até o n-ésimo termo.

  Args:
    n: Número de termos da sequência.

  Returns:
    Lista com os n primeiros termos da sequência de Fibonacci.
  """
  if n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  else:
    fib_seq = [0, 1]
    for i in range(2, n + 1):
      fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq

def main():
  # Entrada do número pelo usuário
  numero = int(input("Digite um número: "))

  # Cálculo da sequência de Fibonacci
  fib_seq = fibonacci(numero)

  # Verificação se o número pertence à sequência
  if numero in fib_seq:
    print(f"O número {numero} pertence à sequência de Fibonacci!")
  else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()

