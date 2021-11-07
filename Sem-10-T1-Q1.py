deposito = float(input(""))
taxa = float(input(""))
ano = 0
saldo = deposito
dobro = saldo * 2
while True :
    saldo = saldo + (saldo * (taxa / 100))
    ano = ano + 1
    if saldo >= dobro:
        print(ano)
        break
    
    
