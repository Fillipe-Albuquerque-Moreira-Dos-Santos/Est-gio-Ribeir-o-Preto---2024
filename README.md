# Estágio Ribeirão Preto - 2024
- Segue abaixo as soluções. Eu escolhi a linguagem python pela falicidade e afinidade pessoal.



## Questão 1


INDICE = 13
SOMA = 0
K = 0

while K < INDICE:

  K += 1
  SOMA += K

print(SOMA)



- A saída será 91
-----------------

## Questão 2

def fibonacci(n):

if n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  else:
    fib_seq = [0, 1]
    for i in range(2, n + 1):
      fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq
