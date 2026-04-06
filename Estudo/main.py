import pyodbc
import pandas as pd

dados_conexao=(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)
try:
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão Bem Sucedida!")
except Exception as e:
    print("Deu erro: ", e)

cursor=conexao.cursor()

id=3
cliente='Jorge'
produto='Mareta'
data='26/08/2021'
preco=6520
quantidade=4

# commando = f"""
# INSERT INTO
#     Vendas(id_vendas, cliente, produto, data_venda, preco, quantidade)
# VALUES
# 	({id},'{cliente}','{produto}','{data}',{preco},{quantidade})
# """

# cursor.execute(commando)
# cursor.commit()

query="SELECT * FROM Vendas"
df=pd.read_sql(query, conexao)