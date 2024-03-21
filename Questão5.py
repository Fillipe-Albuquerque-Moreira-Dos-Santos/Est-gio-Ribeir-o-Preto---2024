texto = "Olá, mundo!"
texto_invertido = ""
for i in range(len(texto)-1, -1, -1):
  texto_invertido += texto[i]

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
