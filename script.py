"1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares."

def numeros_impares():
    lista = list(map(int, input("Digite os números separados por espaço: ").split()))
    return [num for num in lista if num % 2 != 0]

# Exemplo de uso:
saida = numeros_impares()
print("Números ímpares:", saida)

"2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes."

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos():
    lista = list(map(int, input("Digite os números separados por espaço: ").split()))
    return [num for num in lista if eh_primo(num)]

# Exemplo de uso:
saida = numeros_primos()
print("Números primos:", saida)

"3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas."

def elementos_unicos():
    lista1 = list(map(int, input("Digite os números da primeira lista separados por espaço: ").split()))
    lista2 = list(map(int, input("Digite os números da segunda lista separados por espaço: ").split()))
    return list(set(lista1).difference(lista2)) + list(set(lista2).difference(lista1))

# Exemplo de uso:
saida = elementos_unicos()
print("Elementos únicos:", saida)

"4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista."

def segundo_maior():
    lista = list(map(int, input("Digite os números separados por espaço: ").split()))
    primeiro, segundo = float('-inf'), float('-inf')
    for num in lista:
        if num > primeiro:
            segundo = primeiro
            primeiro = num
        elif primeiro > num > segundo:
            segundo = num
    return segundo

# Exemplo de uso:
saida = segundo_maior()
print("Segundo maior valor:", saida)

"5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética."

def ordenar_por_nome():
    lista = []
    n = int(input("Quantas pessoas você quer adicionar? "))
    for _ in range(n):
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        lista.append((nome, idade))
    return sorted(lista, key=lambda x: x[0])

# Exemplo de uso:
saida = ordenar_por_nome()
print("Lista ordenada por nome:", saida)

"6. Observe os espaços sublinhados e complete o código."

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5), transform=axs[row, col].transAxes, ha='center', va='center', fontsize=18, color='darkgrey')
fig.suptitle('plt.subplots()')

"7. Observe os espaços sublinhados e complete o código."

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

"8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?"

import pandas as pd

df = pd.read_csv('nome_do_arquivo.csv')
print(df.head())

"9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?"

import pandas as pd

df = pd.read_csv('nome_do_arquivo.csv')
coluna_filtrada = input("Digite o nome da coluna que deseja filtrar: ")
valor = int(input("Digite o valor de comparação: "))
linhas_filtradas = df[df[coluna_filtrada] > valor]
print(linhas_filtradas)

"10.Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?"

import pandas as pd

df = pd.read_csv('nome_do_arquivo.csv')

# Substituir NaN por um valor específico
valor = int(input("Digite o valor para substituir os NaNs: "))
df.fillna(valor, inplace=True)

# Remover linhas com NaN
remover = input("Deseja remover linhas com NaNs? (s/n): ")
if remover.lower() == 's':
    df.dropna(inplace=True)

# Substituir NaN por média da coluna
coluna = input("Digite o nome da coluna para substituir os NaNs pela média: ")
df[coluna] = df[coluna].fillna(df[coluna].mean())

print(df)
