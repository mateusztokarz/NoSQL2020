import string
import time
import random
import mysql.connector
from pymongo import MongoClient

#random int w zakresie 0-2000

#połączenie mongo1
client1=MongoClient('10.100.100.2:27017')
baza1=client1['up1']
kolekcja1=baza1.big1

#połączenie mongo2
client2=MongoClient('10.100.100.3:27017')
baza2=client2['up2']
kolekcja2=baza2.big2

#test
start = time.time()
licznik = 0
N=kolekcja1.estimated_document_count()
count_mongo2 = 0

while count_mongo2 < N:
  rand = random.randint(0, N-1)
  if kolekcja2.count_documents({ '_id': rand }, limit = 1) != 0:
    licznik=licznik+1
    print("istnieje")
  else:
    result = kolekcja1.find_one({ "_id": rand })
    kolekcja2.insert_one(result)
    count_mongo2 = kolekcja2.estimated_document_count()
    licznik=licznik+1
    print(result)

print(licznik)
print('It took', time.time()-start, 'seconds.')