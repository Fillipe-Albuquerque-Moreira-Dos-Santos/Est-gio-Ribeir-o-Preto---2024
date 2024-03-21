def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a

numero = int(input("Digite um número: "))

if fibonacci(numero) == numero:
  print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
