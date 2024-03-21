def descobrir_interruptores():
  
  # Ligar interruptor 1 por 5 minutos
  tempo_ligado_1 = 5

  # Desligar interruptor 1 e ligar interruptor 2 por 1 minuto
  tempo_ligado_2 = 1

  # Simular estado das lâmpadas
  lampadas = {
    "1": "Quente" if tempo_ligado_1 > 0 else "Fria",
    "2": "Acesa" if tempo_ligado_2 >= 1 else "Quente" if tempo_ligado_2 > 0 else "Fria",
    "3": "Fria"  # Lâmpada 3 só pode ser fria nesta situação
  }

  # Analisar estado das lâmpadas e determinar interruptor
  interruptores = {}
  for lampada, estado in lampadas.items():
    if estado == "Acesa":
      interruptores[f"Interruptor {lampada}"] = f"Lâmpada {lampada}"
    elif estado == "Quente":
      interruptores[f"Interruptor {3 - int(lampada)}"] = f"Lâmpada {lampada}"

  return interruptores

# Impressão do resultado
resultado = descobrir_interruptores()
for interruptor, lampada in resultado.items():
  print(f"{interruptor}: {lampada}")

