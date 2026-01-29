# Bibliotecas
# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd  

# Importação da biblioteca NumPy para operações matemáticas e arrays
import numpy as np  

# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt  

# Importação da biblioteca Seaborn para visualização estatística de dados
import seaborn as sns  

# Importação da biblioteca random para geração de números aleatórios
import random  

# Importação das classes datetime e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta
from watermark import watermark


# Bibliotecas locais/fora do mini-projeto
import gd_dsa                   # Geração de dados
import pro_table as pt          # Mostrar em forma de tabela

#----------------------------------------------------------------------------------------------------------
# Registros

print(watermark(author="Enzo Gabriel Dias Perlato"))
print(watermark(iversions=True, globals_=globals()))

#----------------------------------------------------------------------------------------------------------
# Main
## 4. Gerar, Carregar e Explorar os Dados

df_vendas = gd_dsa.dsa_gera_dados_ficticios()
print(type(df_vendas))

"""
# Shape - Mostra o tamanho da tabela (linha x coluna)
print(df_vendas.shape)

# Exibe as 5 primeiras linhas do DataFrame
pt.print_pro_table(df_vendas.head())

# Exibe as 5 últimas linhas do DataFrame
pt.print_pro_table(df_vendas.tail())

# Exibe informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
print(df_vendas.info())

# Resumo estatístico (Apenas de números e datas por padrão)
pt.print_pro_table(df_vendas.describe())
print(df_vendas.dtypes)
"""

#----------------------------------------------------------------------------------------------------------

## 5. Limpeza, Pré-Processamento e Engenharia de Atributos


# Se a coluna 'Data_Pedido' não estiver como tipo datetime, precisamos fazer a conversão explícita
# A coluna pode ser usada para análise temporal
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

# Engenharia de atributos
# Criando a coluna 'Faturamento' (preço x quantidade)
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

# Engenharia de atributos
# Usando uma função lambda para criar uma coluna de status de entrega
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP', 'RJ', 'MG'] else 'Normal')

# pt.print_pro_table(df_vendas.head())
# pt.print_pro_table(df_vendas.tail())

#----------------------------------------------------------------------------------------------------------

## 6. Análise 1 - Top 10 Produtos Mais Vendidos


# Agrupa por nome do produto, soma a quantidade e ordena para encontrar os mais vendidos

# Este bloco de código retorna um tipo de dado diferente do pandas (Series), e a função para criar uma tabela só lê as variáveis do tipo DataFrame.
top_10_produtos = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending = False).head(10)

# Necessário converter para DataFrame
# pt.print_pro_table(top_10_produtos.reset_index())

# Define um estilo para os gráficos
sns.set_style("whitegrid")

# Cria a figura e os eixos
plt.figure(figsize = (12, 7))

# Cria o gráfico de barras horizontais
top_10_produtos.sort_values(ascending = True).plot(kind = 'barh', color = 'skyblue')

# Adiciona títulos e labels
plt.title('Top 10 Produtos Mais Vendidos', fontsize = 16)
plt.xlabel('Quantidade Vendida', fontsize = 12)
plt.ylabel('Produto', fontsize = 12)

# Exibe o gráfico
plt.tight_layout()
plt.savefig("top_10_produtos.png", dpi=150)
plt.close()

#----------------------------------------------------------------------------------------------------------

## 7. Análise 2 - Faturamento Mensal

pt.print_pro_table(df_vendas.head())

# Cria uma coluna 'Mes' para facilitar o agrupamento mensal
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')
pt.print_pro_table(df_vendas.head())

# Agrupa por mês e soma o faturamento
faturamento_mensal = df_vendas.groupby('Mes')['Faturamento'].sum()

# Converte o índice para string para facilitar a plotagem no gráfico
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

# Formata para duas casas decimais
faturamento_mensal.map('R$ {:,.2f}'.format)



# Cria uma nova figura com tamanho de 12 por 6 polegadas
plt.figure(figsize = (10, 6))

# Plota os dados de faturamento mensal em formato de linha
faturamento_mensal.plot(kind = 'line', marker = 'o', linestyle = '-', color = 'green')

# Define o título do gráfico com fonte de tamanho 16
plt.title('Evolução do Faturamento Mensal', fontsize = 16)

# Define o rótulo do eixo X e Y
plt.xlabel('Mês', fontsize = 12)
plt.ylabel('Faturamento (R$)', fontsize = 12)

# Rotaciona os valores do eixo X em 45 graus para melhor visualização
plt.xticks(rotation = 45)

# Adiciona uma grade com estilo tracejado e linhas finas
plt.grid(True, which = 'both', linestyle = '--', linewidth = 0.5)

# Ajusta automaticamente os elementos para evitar sobreposição
plt.tight_layout()

# Exibe o gráfico
plt.savefig("faturamento_mensal.png", dpi=150)
plt.close()

#----------------------------------------------------------------------------------------------------------

## 8. Análise 3 - Vendas Por Estado

# Agrupa por estado e soma o faturamento
vendas_estado = df_vendas.groupby('Estado')['Faturamento'].sum().sort_values(ascending = False)

# Formata para duas casas decimais
print(vendas_estado.map('R$ {:,.2f}'.format))


# Cria uma nova figura com tamanho de 12 por 7 polegadas
plt.figure(figsize = (12, 7))

# Plota os dados de faturamento por estado em formato de gráfico de barras
# Usando a paleta de cores "rocket" do Seaborn
vendas_estado.plot(kind = 'bar', color = sns.color_palette("husl", 7))

# Define o título do gráfico com fonte de tamanho 16
plt.title('Faturamento Por Estado', fontsize = 16)

# Define o rótulo do eixo X
plt.xlabel('Estado', fontsize = 12)

# Define o rótulo do eixo Y
plt.ylabel('Faturamento (R$)', fontsize = 12)

# Mantém os rótulos do eixo X na horizontal (sem rotação)
plt.xticks(rotation = 0)

# Ajusta automaticamente os elementos do gráfico para evitar sobreposição
plt.tight_layout()

# Exibe o gráfico
plt.savefig("faturamento_por_estado.png", dpi=150)
plt.close()

#----------------------------------------------------------------------------------------------------------

## 9. Análise 4 - Faturamento Por Categoria

# Agrupa por categoria, soma o faturamento e formata como moeda para melhor leitura
faturamento_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending = False)

# O .map('{:,.2f}'.format) é opcional, mas deixa a visualização do número mais clara
print()
print(faturamento_categoria.map('R$ {:,.2f}'.format))


# Importa a função FuncFormatter para formatar os eixos
from matplotlib.ticker import FuncFormatter

# Ordena os dados para o gráfico ficar mais fácil de ler
faturamento_ordenado = faturamento_categoria.sort_values(ascending = False)

# Cria a Figura e os Eixos (ax) com plt.subplots()
# Isso nos dá mais controle sobre os elementos do gráfico.
fig, ax = plt.subplots(figsize = (12, 7))

# Cria uma função para formatar os números
# Esta função recebe um valor 'y' e o transforma em uma string no formato 'R$ XX K'
def formatador_milhares(y, pos):
    """Formata o valor em milhares (K) com o cifrão R$."""
    return f'R$ {y/1000:,.0f}K'

# Cria o objeto formatador
formatter = FuncFormatter(formatador_milhares)

# Aplica o formatador ao eixo Y (ax.yaxis)
ax.yaxis.set_major_formatter(formatter)

# Plota os dados usando o objeto 'ax'
faturamento_ordenado.plot(kind = 'bar', ax = ax, color = sns.color_palette("viridis", len(faturamento_ordenado)))

# Adiciona títulos e labels usando 'ax.set_...'
ax.set_title('Faturamento Por Categoria', fontsize = 16)
ax.set_xlabel('Categoria', fontsize = 12)
ax.set_ylabel('Faturamento', fontsize = 12)

# Ajusta a rotação dos rótulos do eixo X
plt.xticks(rotation = 45, ha = 'right')

# Garante que tudo fique bem ajustado na imagem final
plt.tight_layout()

# Exibe o gráfico
plt.savefig("faturamento_por_categoria.png", dpi=150)
plt.close()