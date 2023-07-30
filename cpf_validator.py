lista =[]
d1 = d2 = 0

while True:
    cpf = input('Digite seu cpf (somente números): ou [S]air: ').upper().replace(' ','')
    if cpf in '':
        continue
    if cpf == 'S':
        break
    try:
        int(cpf) 
    except:
        print('Digite somente números!')
        continue   
    if cpf[0] * 9 == cpf[:9]:
        print('Por favor digite uma sequencia válida')
        continue
    if len(cpf) < 11:
        print('Caracteres insuficientes')
        continue
    if len(cpf) > 11:
        print('Caracteres em excesso')
        continue
    soma1 = 0
    cont = 10
    if len(cpf) == 11:
        for i in cpf:
            lista.append(i)
    for v in lista:         
        if cont == 1:
            break
        soma1 += int(v) * cont
        cont -= 1

    lista.clear()
    if soma1 % 11 == 0 or soma1 % 11 == 1:
        d1 = 0
    else:
        d1 = 11 - (soma1 % 11)
    cpfd1_int = int(cpf[-2])
    if d1 == cpfd1_int:
        soma1 =0
        cont = 11

        for j in cpf:
            lista.append(j)
        for k in lista:            
            if cont == 1:
                break
            soma1 += int(k) * cont
            cont -= 1

        lista.clear()
        if soma1 % 11 == 0 or soma1 % 11 == 1:
            d2 = 0
        else: 
            d2 = 11 - (soma1 % 11)
        cpfd2_int = int(cpf[-1])
        if d2 == cpfd2_int:
            print(f'CPF {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} \033[32mVALIDO\033[m')
        else:
            print(f'CPF {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} \033[31mINVALIDO\033[m')
    else:
        print(f'CPF {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} \033[31mINVALIDO\033[m')
        continue

print('-='*30)
print('Fim do programa')
