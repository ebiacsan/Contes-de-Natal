qtd = int(input())

for i in range(qtd):
    requisitos = list(map(int,input().split(" ")))
    if ((requisitos[0] >= 200) and (requisitos[0] <= 300)):
        if((requisitos[1] >= 50)):
            if((requisitos[2] >= 150)): 
                print("Sim")
            else:
                print("Nao")
        else:
            print("Nao")
    else: 
        print("Nao")
