import sqlite3
import os

def db_connect(db='bugsdb'):
    return sqlite3.connect(db)

def create_db(db=sqlite3.Connection, dbname='bugsdb', table='bugs'):
    cursor = db.cursor()
    cursor.execute('CREATE TABLE '+ table+'(id INTEGER PRIMARY KEY,note TEXT)')
    db.commit()
    
def del_db(db='bugsdb', table='bugs'):
    cursor = db.cursor()
    cursor.execute('DROP TABLE  '+table)
    db.commit()
    
def insert_bug(db, **kwargs):
    
    cursor = db.cursor()
    try:
        bugid = kwargs['id']
        print(bugid)
        bugnote = kwargs['note']
        print(bugnote)
        
        cursor.execute('INSERT INTO bugs VALUES(?, ?)', (bugid,bugnote))
        db.commit()
    except Exception:
        pass
    cursor.execute('SELECT id from bugs')
    cursor.fetchall()
    for obj in cursor:
        print(obj)
    
def remove_bug(idnum, db,table='bugs'):
    cursor = db.cursor()
    cursor.execute('DELETE FROM bugs WHERE id=?',(idnum,))
    db.commit()

def retrieve_bugs(db,table='bugs',*args):
    print(db)
    cursor = db.cursor()
    
    if len(args)==0:
        print('exe simple')
        cursor.execute('SELECT * FROM '+table)
    else:
        print('exec with id')
        idnum = args[1]
        cursor.execute('SELECT id FROM '+table+' WHERE id=:id',{id:idnum})
    return cursor.fetchall()
    

def closedb(db=sqlite3.Connection):
    db.close()
