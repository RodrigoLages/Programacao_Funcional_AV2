import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="67538194",
    database="q4_db"
)
cursor = db.cursor()

#Tabelas
cursor.execute("CREATE TABLE IF NOT EXISTS USUARIOS (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), console VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS JOGOS (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), data_lancamento DATE)")

#Funçoes CRUD
insert = lambda table, data: cursor.execute(f"INSERT INTO {table} VALUES (NULL, %s, %s)", data)
remove = lambda table, id: cursor.execute(f"DELETE FROM {table} WHERE id = %s", (id,))
consult = lambda table: cursor.execute(f"SELECT * FROM {table}")

#Ações

#insert("USUARIOS", ("Edu", "Nintendo"))
#insert("JOGOS", ("Outer Wilds", "2019-05-28"))

consult("USUARIOS")
print(cursor.fetchall())
consult("JOGOS")
print(cursor.fetchall())

#remove("USUARIOS", 1)
#remove("JOGOS", 1)

db.commit()
cursor.close()
db.close()
