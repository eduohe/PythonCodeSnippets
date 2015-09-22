#! /usr/bin/python3
import sqlite3

class CustomerCRUD:
    def __init__(self):
        self._db = sqlite3.connect('db.sqlite')
        self._db.row_factory = sqlite3.Row
        self._db.execute('DROP TABLE IF EXISTS customer')
        self._db.execute('CREATE TABLE customer(id int, name text)')

    def create(self, row):
         self._db.execute('INSERT INTO customer(id, name) VALUES (?,?)', (row['id'],row['name']))
         self._db.commit()

    def retrieve(self, id):
        cursor = self._db.execute('SELECT id, name FROM customer order by id')
        return dict(cursor.fetchone())

    def update(self, row):
        self._db.execute('UPDATE customer SET name = ? WHERE id = ?', (row['name'],row['id']))
        self._db.commit()

    def delete(self,id):
         self._db.execute('DELETE FROM customer WHERE id = ?', (id,))
         self._db.commit()

    def all(self):
        cursor = self._db.execute('SELECT id, name FROM customer order by id')
        for row in cursor:
            print('{}:{}'.format(row['id'], row['name'].upper()))

def main():

    print("Init")
    c = CustomerCRUD();
    print("Create")
    c.create(dict(id=1,name='João'))
    c.create(dict(id=2,name='Maria'))
    c.all()
    print("Retrive")
    print(c.retrieve(1))
    print("Update")
    c.update(dict(id=1,name='João da Silva'))
    c.update(dict(id=2,name='Maria de Souza'))
    c.all()
    print("Delete")
    c.delete(1)
    c.delete(2) 
    c.all()
    print('End')
    
if __name__ == '__main__': main()