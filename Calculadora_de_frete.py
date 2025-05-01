print('=== Bem vindo ao sistema de calcular fretes do Wellington ===')
print('Limite Kg = 10Kg\nLimite Km = 15Km')


print('=== Solicitando informações do produto ===')
Peso_produto = float(input('Qual o peso bruto do produto?\n'))
Distancia = int(input('Qual a distância para envio?\n'))
Escolha_do_frete = input('Qual o modelo do frete?\n')
print('-'* 65)

print('=== Informação de peso e calculo KG ===')
if Peso_produto <= 1:
    Valor_kg = Peso_produto * 10
    print(f'O valor do peso é de R${Valor_kg:.2f}.')

elif Peso_produto <= 5:
    Valor_kg = Peso_produto * 4.90
    print(f'O valor do peso é de R${Valor_kg:.2f}.')

elif Peso_produto <= 10:
    Valor_kg = Peso_produto * 8.90
    print(f'O valor do peso é de R${Valor_kg:.2f}.')

else:
    print('Peso acima do permitido. Limite de 10Kg.')
    exit()
print('-'* 65)

print('=== Informação de distância (Km) ===')
if Distancia <= 5:
    Valor_Km = Distancia * 2
    print(f'O valor da distância ficou R${Valor_Km:.2f}')

elif Distancia <= 10:
    Valor_Km = Distancia * 4
    print(f'O valor da distância ficou R${Valor_Km:.2f}')

elif Distancia <= 15:
    Valor_Km = Distancia * 6
    print(f'O valor da distância ficou R${Valor_Km:.2f}')

else:
    print('Distância acima do permitido. Limite de 15Km.')
    exit()
print('-'* 65)

print('=== Escolha de modelo do frete ===')

if Escolha_do_frete == 'basico':
    preço_frete = 10.00 
    print(f'Preço da opção basica é de: R${preço_frete:.2f}, prazo de 3 a 7 dias uteis.')

elif Escolha_do_frete == 'expresso':
    preço_frete = 20.00
    print(f'Preço da opção expressa é de: R${preço_frete:.2f}, Prazo de 2 a 3 dias uteis.')

else:
    print('Opção invalida, tente novamente!')
    exit()
print('-'* 65)

print('=== Valor total do frete baseado nas opções listadas acima ===')
Total = Valor_kg + Valor_Km + preço_frete
print(f'O valor do frete será de: R${Total:.2f}.')