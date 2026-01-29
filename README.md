# Análise de Vendas – Mini Projeto com Pandas, NumPy e Matplotlib
Este repositório contém meu primeiro mini-projeto de análise de dados, onde simulo um cenário real de e-commerce para gerar, explorar e visualizar dados de vendas utilizando Python, Pandas, NumPy, Matplotlib e Seaborn.

O objetivo é transformar dados fictícios em insights acionáveis, explorando produtos, categorias, comportamento ao longo do tempo e distribuição geográfica.

---

## ⚖️ Objetivo do Projeto

Criar uma base de vendas simulada e responder perguntas de negócio como:

- Quais produtos vendem mais?
- Quais categorias geram maior faturamento?
- Como as vendas evoluem ao longo do tempo?
- Quais cidades e estados concentram mais pedidos?

Tudo isso aplicando conceitos iniciais de Data Analytics com Python.

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Rich (para exibição de tabelas no terminal)

## 🏯 Estrutura do Projeto

```bash
Projeto
 ┣ main.py
 ┣ gd_dsa.py
 ┣ pro_table.py
 ┣ requirements.txt
 ┗ README.md
```

### 🔷 gd_dsa.py

Responsável por gerar os dados fictícios de vendas:

- Cria produtos com categorias e preços
- Gera pedidos com datas, cidades, estados e clientes
- Aplica descontos em produtos específicos
- Retorna tudo em um DataFrame Pandas

A função principal é:

```bash
dsa_gera_dados_ficticios()
```
Ela cria automaticamente centenas de registros simulando vendas reais.


### 🔷 pro_table.py

Contém uma função auxiliar que exibe qualquer DataFrame em formato de tabela bonita no terminal usando Rich:

```bash
print_pro_table(df)
```

Facilita a visualização dos dados diretamente no console.


### 🔷 main.py

Arquivo principal do projeto, onde:

- Os dados são gerados
- O DataFrame é explorado
- São feitas análises estatísticas
- São criados gráficos com Matplotlib e Seaborn
- São extraídos insights sobre vendas, produtos, categorias e localização

É aqui que toda a lógica de análise acontece.

### 🔷 requirements.txt

Lista todas as dependências necessárias:

- matplotlib
- numpy
- pandas
- seaborn
- watermark
- rich

## 🃏​ Como Executar
1. Clone o repositório:

```bash
git clone https://github.com/EnzoDiasDev/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual (opcional, recomendado):

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o projeto:

```bash
python main.py
```

## 👨‍💻 Autor

Enzo Gabriel Dias Perlato

Notion: https://www.notion.so/Mini-Projeto-registro-de-Desafios-2f671be945f5801ead6afd2fa034bc0d?source=copy_link \
LinkedIn: www.linkedin.com/in/enzodias07

Estudante de Engenharia de Software com foco em desenvolvimento e dados, construindo projetos práticos para evolução contínua 🚀
