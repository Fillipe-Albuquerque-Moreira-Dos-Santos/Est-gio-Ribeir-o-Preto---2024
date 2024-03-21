def descobrir_interruptores():

  # Simular estado das lâmpadas após 5 minutos com interruptor 1 ligado e 1 minuto com interruptor 2 ligado.
  lampadas = {
    "1": "Quente",
    "2": "Acesa" if 1 >= 1 else "Quente",
    "3": "Fria",
  }

  # Analisar estado das lâmpadas e determinar interruptor
  interruptores = {}
  for lampada, estado in lampadas.items():
    if estado == "Acesa":
      interruptores[f"Interruptor {lampada}"] = f"Lâmpada {lampada}"
    elif estado == "Quente":
      interruptores[f"Interruptor {3 - int(lampada)}"] = f"Lâmpada {lampada}"

  return interruptores

# Descobrir e imprimir a relação entre interruptores e lâmpadas
resultado = descobrir_interruptores()
for interruptor, lampada in resultado.items():
  print(f"{interruptor}: {lampada}")
