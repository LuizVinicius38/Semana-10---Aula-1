n = 1
lista = []
try:
    while True:
        entrada = int(input(""))
        lista.append(entrada)
        n = n + 1
        if entrada == 0:
            lista.remove(0)
            print(max(lista))
            print(min(lista))
            break
except:
    pass
    
