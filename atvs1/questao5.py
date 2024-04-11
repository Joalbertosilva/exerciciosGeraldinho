

numeros = (1, 21)  
par = []
impar = []
for i in range(numeros[0], numeros[1]):  
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Esses são os numeros pares: {par}')
print(f'Esses são os números impares: {impar}')