from rich.console import Console
from rich.table import Table
import pandas as pd

# Função para converter DataFrame em tabela 'Rich'
def print_pro_table(df):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    
    # Adiciona as colunas
    for col in df.columns:
        table.add_column(col)
    
    # Adiciona as linhas (convertendo tudo para string)
    for _, row in df.iterrows():
        table.add_row(*[str(val) for val in row])
        
    console.print(table)