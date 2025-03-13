import sqlite3  

class Database:  
    def __init__(self, db):  
        self.con = sqlite3.connect(db)  
        self.cur = self.con.cursor()  
        self.cur.execute("""  
            CREATE TABLE IF NOT EXISTS users (  
            radif INTEGER PRIMARY KEY,  
            fname TEXT,   
            lname TEXT,  
            email TEXT,  
            pass TEXT)  
            """)  
        self.con.commit()   

    def insert_record(self, fname, lname, email, pas):  
        self.cur.execute('INSERT INTO users VALUES (NULL,?,?,?,?)', (fname, lname, email, pas))  
        self.con.commit()  

    def select_record(self, email, pas):  
        self.cur.execute('SELECT * FROM users WHERE email = ? AND pass = ?', (email, pas))  
        return self.cur.fetchall()