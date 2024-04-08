import sqlite3

""" Criando Conexão """
try:
    conn = sqlite3.connect('bancodedados.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados: ", e)

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE cad_pessoal (
    id INT PRIMARY KEY,
    nome_pessoal Varchar(255) NOT NULL,
    email_pessoal VARCHAR(255) NOT NULL,
    ESTADO VARCHAR(50) NOT NULL,
    cidade VARCHAR(60) NOT NULL,
    NIVEL_FORMACAO VARCHAR(50) NOT NULL,
    INSTITUICAO_FORMACAO VARCHAR(300) NOT NULL,
    INSTITUICAO_ATUACAO VARCHAR(300) NOT NULL,
    VALIDACAO VARCHAR(50) NOT NULL,
    SENHA VARCHAR(255) NOT NULL,
    CODIGO VARCHAR(255) NOT NULL,
    NIVEL INT NOT NULL
);
        ) """)

        print("TABELA CAD_PESSOAL CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela CAD_PESSOAL ", e)


try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE cad_funcional (
    id INTEGER PRIMARY KEY,
    nome_funcional VARCHAR(255) NOT NULL,
    email_funcional VARCHAR(255) NOT NULL,
    ESTADO VARCHAR(50) NOT NULL,
    cidade VARCHAR(60) NOT NULL,
    NIVEL_FORMACAO VARCHAR(50) NOT NULL,
    INSTITUICAO_FORMACAO VARCHAR(300) NOT NULL,
    INSTITUICAO_ATUACAO VARCHAR(300) NOT NULL,
    VALIDACAO VARCHAR(50) NOT NULL,
    SENHA VARCHAR(255) NOT NULL,
    CODIGO VARCHAR(255) NOT NULL,
    area_atuacao VARCHAR(255) NOT NULL,
    subarea VARCHAR(255) NOT NULL,
    especialidade VARCHAR(255) NOT NULL,
    grupo_pesquisa VARCHAR(255) NOT NULL,
    posicao VARCHAR(100) NOT NULL,
    nome_coordenador VARCHAR(255) NOT NULL,
    email_coordenador VARCHAR(255) NOT NULL,
    nivel INT NOT NULL
);""")

        print("TABELA CAD_fUNCIONA CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela CAD_FUNCIONAL ", e)




login = input("Insira o Email de Login:")
senha = input("Insira Senha de Login: ")
