import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco de dados (será criado se não existir)
conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

# Criar a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor_vendido TEXT NOT NULL,
        vendedor INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')
conexao.commit()



#criar a extrutura que mostrara o banco de dados

def inserir_dados():
    valor_vendido = entrada_valor_vendido.get ()
    vendedor = entrada_vendedor.get()
    cidade = entrada_cidade.get ()
    if valor_vendido and vendedor.isdigit() and cidade:
        cursor.execute('''
            INSERT INTO vendas (valor_vendido, vendedor, cidade)
            VALUES (?, ?, ?)      
            ''', (valor_vendido, int (vendedor), cidade))

        conexao.commit ()
        messagebox.showinfo("showinfo","dados inseridos")
        entrada_valor_vendido.delete(0,tk.END)
        entrada_vendedor.delete(0,tk.END)
        entrada_cidade.delete(0,tk.END)
    else:
        messagebox.showwarning("showwarning", "Algo deu errado!")



# Função para exibir dados em um gráfico
def exibir_grafico():
    cursor.execute('SELECT valor_vendido, vendedor FROM vendas')
    dados = cursor.fetchall()
    
    if dados:
        valor_vendido = [dado[0] for dado in dados]
        vendedor = [dado[1] for dado in dados]

        plt.figure(figsize=(10, 5))
        plt.bar(valor_vendido, vendedor, color='skyblue')
        plt.xlabel('Valor Vendido')
        plt.ylabel('Vendedor')
        plt.title('Quantidade vendida por vendedor')
        plt.show()
    else:
        messagebox.showwarning("Erro", "Nenhum dado encontrado para exibir.")





# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de vendedor")

# Rótulos e campos de entrada
tk.Label(janela, text="Valor Vendido:").grid(row=0, column=0, padx=10, pady=5)
entrada_valor_vendido = tk.Entry(janela)
entrada_valor_vendido.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Vendedor:").grid(row=1, column=0, padx=10, pady=5)
entrada_vendedor = tk.Entry(janela)
entrada_vendedor.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Cidade:").grid(row=2, column=0, padx=10, pady=5)
entrada_cidade = tk.Entry(janela)
entrada_cidade.grid(row=2, column=1, padx=10, pady=5)

# Botões
btn_inserir = tk.Button(janela, text="Inserir Dados", command=inserir_dados)
btn_inserir.grid(row=3, column=0, columnspan=2, pady=10)

btn_grafico = tk.Button(janela, text="Exibir Gráfico", command=exibir_grafico)
btn_grafico.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da aplicação
janela.mainloop()

# Fechar a conexão ao banco de dados quando a janela for fechada
conexao.close()
