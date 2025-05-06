altura, comprimento, largura, massa = input().split()

altura = int(altura)
comprimento = int(comprimento)
largura = int(largura)
massa = int(massa)
pacote = 2 
volume = altura * comprimento * largura
classe = 2

#bulky = 0
#heavy = 1

#classes:
#standard = 0
#special = 1
#rejected = 2

if altura >= 150 or comprimento >= 150 or largura >= 150:
    if massa >= 20:
        pacote = 3
    else:
        pacote = 0
elif massa >= 20 and volume >= 1000000:
    pacote = 3
elif massa >= 20:
    pacote = 1
elif volume >= 1000000:
    pacote = 0

    
if pacote == 1:
    classe = 1
elif pacote == 2:
    classe = 0
elif pacote == 3:
    classe = 2
elif pacote == 0:
    classe = 1
    
if classe == 0:
    print("standard")
elif classe == 1:
    print("special")
elif classe == 2:
    print("rejected")
