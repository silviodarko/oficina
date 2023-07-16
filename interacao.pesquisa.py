import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('oficina.db')

# Criar o cursor
cursor = conn.cursor()

# Executar o script SQL para criar as tabelas
cursor.executescript('''
    -- Código SQL para a criação das tabelas...
''')

# Persistir os dados para realização de testes
# ...

# Exemplo de consulta utilizando SELECT
cursor.execute('SELECT * FROM Cliente')
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)

# Exemplo de consulta utilizando JOIN e filtros
cursor.execute('''
    SELECT Pedido.ID_Pedido, Cliente.Nome, Entrega.Status
    FROM Pedido
    JOIN Cliente ON Pedido.ID_Cliente = Cliente.ID_Cliente
    JOIN Entrega ON Pedido.ID_Pedido = Entrega.ID_Pedido
    WHERE Pedido.ID_Pedido = 1
''')
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)

# Fechar a conexão com o banco de dados
conn.close()

