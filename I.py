a = int(input())
c = 0
b = 0

for _ in range(a):
    sexo = input().split(" ")[1]
    if sexo == 'F':
        b+=1
    else:
        c+=1
print(c,"carrinhos")
print(b,"bonecas")
