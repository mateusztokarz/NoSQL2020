import string
import random
import mysql.connector
from pymongo import MongoClient

#połączenie mongo
client=MongoClient('10.100.100.2:27017')
baza=client['up']
kolekcja=baza.big

#połączenie maria
mariadb_connection = mysql.connector.connect(host='10.100.100.3', user='admin', password='test', database='database')
cursor = mariadb_connection.cursor()

#wielkość tabeli w maria db
N=2000

for i in range(N):
    cursor.execute('SELECT name FROM tabela WHERE id="%s"',(i,))
    myresult = cursor.fetchone()
    print(myresult[0])
    kolekcja.insert_one({"_id" : i, "name": myresult[0]})