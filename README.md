# Calculadora de Frete - Projeto de Automação

## Descrição

Este é um script em Python para **cálculo de frete** baseado no **peso do produto**, **distância de envio** e a **opção de frete** (básico ou expresso).

O programa solicita ao usuário as seguintes informações:
1. **Peso do produto** em quilogramas (kg).
2. **Distância para envio** em quilômetros (km).
3. **Opção de frete** entre "básico" e "expresso".

Com base nesses dados, o sistema calcula o valor do frete utilizando uma tabela de preços específica para cada condição e retorna o valor final.

## Funcionalidades

- **Cálculo do valor do frete**:
    - O valor do frete depende do peso do produto e da distância de envio.
    - Há duas opções de frete: *básico* (mais barato, com maior prazo) e *expresso* (mais caro, com prazo menor).
- **Validação de entradas**:
    - O peso não pode ultrapassar 10 kg.
    - A distância não pode ultrapassar 15 km.
- **Mensagens claras de erro**:
    - O script informa caso o usuário insira valores acima dos limites permitidos e encerra a execução.

## Como Usar

1. **Clone ou baixe o repositório** no seu computador.
2. Abra um terminal e navegue até a pasta onde o script foi salvo.
3. Execute o script com Python:
   ```bash
   python Calculadora_de_frete.py
