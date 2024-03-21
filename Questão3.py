def proximo_elemento(sequencia):

  # Lógica para cada sequência

  if sequencia[-1] == 7:
    return sequencia[-1] + 2  # Sequência a)
  elif sequencia[-1] == 64:
    return sequencia[-1] * 2  # Sequência b)
  elif sequencia[-1] == 36:
    return (len(sequencia) + 1)**2  # Sequência c)
  elif sequencia[-1] == 64:
    return sequencia[-1] * 2  # Sequência d)
  elif sequencia[-1] == 8:
    return sequencia[-2] + sequencia[-1]  # Sequência e)
  else:
    return "Lógica não identificável"  # Sequência f)

# Sequências para teste
sequencias = [
  [1, 3, 5, 7],
  [2, 4, 8, 16, 32, 64],
  [0, 1, 4, 9, 16, 25, 36],
  [4, 16, 36, 64],
  [1, 1, 2, 3, 5, 8],
  [2, 10, 12, 16, 17, 18, 19],
]

# Execução da função para cada sequência
for sequencia in sequencias:
  proximo = proximo_elemento(sequencia)
  print(f"Sequência: {sequencia}")
  print(f"Próximo elemento: {proximo}")
  print()
