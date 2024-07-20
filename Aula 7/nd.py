import sqlite3 


conexao = sqlite3.connect('meu_banco_de_dados.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL,
    idade INTERGER NOT NULL,
    cidade TEXT NOT NULL
    )
''')

#inserir dados na tabela

nome = "Pedro"
idade = 26
cidade = "Guarulhos"

cursor.execute ('''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidade))

conexao.commit()

cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()

#mostrar os dados consultados

for pessoa in pessoas:
    print (f''' ID: {pessoa [0]}, Nome: {pessoa [1]}, Idade: {pessoa [2]}, Cidade: {pessoa [3]}''')

#fechar conexão

conexao.close()