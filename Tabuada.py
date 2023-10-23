total = 0

numero = int(input('Digite um número para pesquisar a tabuada: '))
print(f'A Tabuada de Multiplicação: {numero}')
for contador in range(1, 11):
    print(f'{numero} X {contador} = {numero * contador}')