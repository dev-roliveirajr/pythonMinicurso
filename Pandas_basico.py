import pandas as pd
import utils_email

# importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
#print(tabela_vendas)


# faturamento por loja
#faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
# print(faturamento)

# qtd de produtos vendidos por loja
#quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(quantidade)

# ticket médio por produto, por loja
#ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
#print(ticket_medio)

# ticket médio por produto, por loja com subtotal
#ticket_medio_produto = tabela_vendas[['Produto', 'Valor Final']].groupby(['Produto']).mean()

#ticket_medio_produto_loja = tabela_vendas[['ID Loja', 'Produto', 'Valor Final']].groupby(['Produto', 'ID Loja']).mean()
#print(ticket_medio_produto_loja)

tabela_vendas['Ticket Medio Produto'] = tabela_vendas.groupby('Produto')['Valor Final'].transform('mean')
tabela_vendas['Ticket Medio Produto Loja'] = tabela_vendas.groupby(['Produto', 'ID Loja'])['Valor Final'].transform('mean')
#print(tabela_vendas)

report = tabela_vendas[['Produto', 'Ticket Medio Produto', 'ID Loja', 'Ticket Medio Produto Loja']].loc[tabela_vendas['Produto'] == 'Bermuda'].groupby(['Produto', 'Ticket Medio Produto', 'ID Loja']).mean()