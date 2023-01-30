import sqlite3
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id Int PRIMARY KEY, title TEXT, "
                    "author TEXT, year INTEGER,price INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year,price):
        #the NULL parameter is for the auto-incremented id
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,price))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows

    def search(self,title="", author="", year="", price=""):
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR price = ? ", (title, author, year,price))
        rows = self.cur.fetchall()
        #conn.close()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id, title, author, year, price):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, WHERE id = ?, price = ?", (title, author, year, price,id))
        self.conn.commit()

    #destructor-->now we close the connection to our database here
    def __del__(self):
        self.conn.close()
