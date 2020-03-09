def is_primo(numero):
  for i in range(2, numero, 1):
    if numero % i == 0 :
      return False
  return True

qtd = int(input())
for i in range(qtd):
  numero_caso = int(input())
  valor_analisado = numero_caso + 1
  if valor_analisado % 7 == 0:
    if valor_analisado % 2 != 0:
      if is_primo(valor_analisado + 2):
        print("Yes")
      else:
        print("No")
    else:
      print("No")
  else:
    print("No")
