from bugzilladb import *
import os
import sys

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
        print('connected '+str(self.dbobj))
        
        idlist = retrieve_bugs(db=self.dbobj)
        print(idlist)
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
    #menu()
    if len(sys.argv)>1:
        if sys.argv[1] in ['a','d','r','h']:
            if sys.argv[1] == 'd' or sys.argv[1] == 'h':
                b.options[sys.argv[1]]()
            if sys.argv[1] == 'a':
                if sys.argv[2]:
                    idb = sys.argv[2]
                    #idb = raw_input('id :')
                    noteb = raw_input('add a note :' )
                    b.options[sys.argv[1]]( id=idb, note=noteb)
            if sys.argv[1] == 'r':
                b.options[sys.argv[1]](sys.argv[2])
        else:
            print('no such an option (try \'h\')')
    else:
        b.options['h']()
        print('you need parameters dude!!')
        #argparse or click
    #option = raw_input(':: ')
    
    #if option.strip()=='a':
    #    idb = raw_input('id :')
    #    noteb = raw_input('note :' )
    #    b.options[option]( id=idb, note=noteb)
    #if option.strip()=='r':
    #    idb = raw_input('id :')
    #    b.options[option](idb)
    #if option.strip()=='d' or option.strip()=='h':
    #    b.options[option]()
    
