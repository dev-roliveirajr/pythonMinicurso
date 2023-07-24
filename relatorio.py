import pandas as pd
import utils_email

# importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
#print(tabela_vendas)


tabela_vendas['Ticket Medio Produto'] = tabela_vendas.groupby('Produto')['Valor Final'].transform('mean')
tabela_vendas['Ticket Medio Produto Loja'] = tabela_vendas.groupby(['Produto', 'ID Loja'])['Valor Final'].transform('mean')
#print(tabela_vendas)

report = tabela_vendas[['Produto', 'Ticket Medio Produto', 'ID Loja', 'Ticket Medio Produto Loja']].loc[tabela_vendas['Produto'] == 'Bermuda'].groupby(['Produto', 'Ticket Medio Produto', 'ID Loja']).mean()

#print(report)


# enviar email com o relatório
email = utils_email.Email()
destinatario = "cihadak356@muzitp.com"
mensagem = f"<P>Olá,</P><P>Segue o relatório semanal de vendas:</P>{report.to_html()}<P>Obrigado.</P>"
email.enviar_email("", destinatario, "Relatório Semanal de Vendas", mensagem)