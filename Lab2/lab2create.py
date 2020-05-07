import string
import random

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

from pymongo import MongoClient

client1=MongoClient('10.100.100.2:27017')
baza1=client1['up1']
kolekcja1=baza1.big1

N=2000

for i in range(N):
    kolekcja1.insert_one({"_id" : i, "name": id_generator()})

 