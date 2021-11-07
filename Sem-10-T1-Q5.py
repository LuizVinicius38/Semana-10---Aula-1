salario = float(input(""))
divida = float(input(""))
mes = 10
ano = 2016
while True:
    divida = divida +(divida * (15 / 100))
    mes = mes + 1
    if mes == 3:
        salario = salario +(salario *(5/100))
    if mes == 12: 
        mes = 0
        ano = ano + 1
    if divida > salario:
        print(f'{mes}/{ano}')
        break
    
