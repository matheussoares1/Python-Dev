import sqlite3
import csv

# Conectar ao banco de dados
conn = sqlite3.connect('nome_do_arquivo.db')
#O arquivo deve estar na mesma pasta e já deve estar criado

# Criar um cursor
cursor = conn.cursor()

# Executar uma consulta SQL para selecionar os dados da tabela que deseja exportar
cursor.execute("SELECT * FROM nome_tabela")

# Recuperar todos os registros da consulta
dados = cursor.fetchall()

# Definir o nome do arquivo CSV de saída
nome_arquivo_csv = 'nome_arquivo.csv'

# Escrever os dados no arquivo CSV
with open(nome_arquivo_csv, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrever o cabeçalho (nomes das colunas)
    escritor_csv.writerow([i[0] for i in cursor.description])
    
    # Escrever os dados
    escritor_csv.writerows(dados)

# Fechar a conexão com o banco de dados
conn.close()

print(f'Dados exportados para {nome_arquivo_csv}')
