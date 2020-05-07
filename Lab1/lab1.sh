#!/bin/bash 
echo "Start skryptu"
docker-compose -f lab1.yml up -d
echo "Uruchomione kontenery"
docker ps
echo "Poczekaj 30sekund na postawienie baz danych"
sleep 30
echo "Generowanie 2000 rekordów mariaDB"
docker exec -it python bash -c "cd PY3 && source bin/activate && python sql.py"
echo "Kopiowanie rekordów z mariaDB do mongoDB"
docker exec -it python bash -c "cd PY3 && source bin/activate && python lab1.py"
echo "Rekordy zostały przepisane z mariaDB do mongoDB"