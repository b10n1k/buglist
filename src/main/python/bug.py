from bugzilladb import *
import os
import sys
import argparse

class bug():
    
    def __init__(self, db=sqlite3.Connection, dbname='bugsdb'):
        self.dbobj = db
        if not os.path.isfile(dbname):
            self.dbobj = db_connect()
            create_db(db=dbobj)
            closedb(dbobj)
            
        self.options = {'a':self.addbug,
               'd':self.listbugs,
               'r':self.delbug,
               'h':self.menu}
    
    def addbug(self, **kwargs):
        self.dbobj = db_connect()
        print('connected')
        if self.dbobj:
            
            insert_bug(self.dbobj,id=kwargs['id'],note=kwargs['note'])
        self.dbobj.close()

    def delbug(self, id):
        self.dbobj = db_connect()
        remove_bug(id, self.dbobj)
    
    def listbugs(self):
        idlist = []
        self.dbobj = db_connect()
        #print('connected '+str(self.dbobj))
        
        idlist = retrieve_bugs(db=self.dbobj)
        #print(idlist)
        if idlist:
            for bug in idlist:
                print(bug)
                
        self.dbobj.close()

    def menu(self):
        print('''Usage: bug [options] id
            
             d - display
             a - add
             r - remove

        ''')
    
if __name__ =="__main__":
    b = bug()
    print('list \n')
    b.listbugs()
    #menu()
    parser = argparse.ArgumentParser(prog="bug", description="add/list/delete a bug id")
    parser.add_argument('-a', nargs='+', type=int, help='Add one or more bug ids')
    parser.add_argument('-r', nargs='+', type=int, help='Delete one or more bug ids ')
    parser.add_argument('-d', nargs='?', help="list bugs ids")
    args = parser.parse_args()

    if args.d:
        b.options['d']()
    if args.a:
        for arg in args.a:
            noteb = raw_input('add a note for bug '+str(arg)+' :' )
            projb = raw_input(str(arg)+' project:' )
            b.options['a'](id=arg, note=noteb)
    if args.r:
        for arg in args.r:
            b.options['r'](arg)    
