qtdCasos = int(input())

for i in range(qtdCasos):
  ## 1 = Joao , 2 = Maria
  ptsJoao = 0
  ptsMaria = 0
  for i in range(3):
    listaJoao = input().split(" ")
    ptsJoao += int(listaJoao[0]) * int(listaJoao[1])

  for i in range(3):
    listaMaria = input().split(" ")
    ptsMaria += int(listaMaria[0]) * int(listaMaria[1])
  
  if ptsJoao < ptsMaria:
    print("MARIA")
  else:
    print("JOAO")
