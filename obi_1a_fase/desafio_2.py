def is_bulky(altura, comprimento, largura):
    volume = altura * comprimento  * largura
    return altura >= 150 or comprimento >= 150 or largura >= 150 or volume >= 1000000
    
def is_heavy(massa):
    return massa >= 20
    
    
def sort(altura, comprimento, largura, massa):
    if is_bulky(altura, comprimento, largura) and is_heavy(massa):
        print("REJECTED")
    elif is_bulky(altura, comprimento, largura) or is_heavy(massa):
        print("SPECIAL")
    else:
        print("STANDARD")