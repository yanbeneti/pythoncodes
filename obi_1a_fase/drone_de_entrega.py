altura_pacote_A = int(input())
largura_pacote_B = int(input())
comprimento_pacote_C = int(input())
altura_janela_H = int(input())
largura_janela_L = int(input())

# A = 30
# B = 50
# c = 80

# H = 80
# l = 60

# A B x H L -> B A x H L
# A C x H L -> C A x H L
# B C x H L -> C B x H L

if altura_pacote_A <= altura_janela_H and largura_pacote_B <= largura_janela_L:
    print("S")
elif largura_pacote_B <= altura_janela_H and altura_pacote_A <= largura_janela_L:
    print("S")
elif altura_pacote_A <= altura_janela_H and comprimento_pacote_C <= largura_janela_L:
    print("S")
elif comprimento_pacote_C <= altura_janela_H and altura_pacote_A <= largura_janela_L:
    print("S")
elif largura_pacote_B <= altura_janela_H and comprimento_pacote_C <= largura_janela_L:
    print("S")
elif comprimento_pacote_C <= altura_janela_H and largura_pacote_B <= largura_janela_L:
    print("S")
else:
    print("N")