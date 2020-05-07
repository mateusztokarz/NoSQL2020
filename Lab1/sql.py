import string
import random
import mysql.connector

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

mariadb_connection = mysql.connector.connect(host='10.100.100.3', user='admin', password='test', database='database')
cursor = mariadb_connection.cursor()
cursor.execute("CREATE TABLE tabela (id int, name VARCHAR(255))")

N=2000

for i in range(N):
    cursor.execute("INSERT INTO tabela (id, name) VALUES (%s,%s)", (i, id_generator()))
    mariadb_connection.commit()

cursor.close()
mariadb_connection.close()