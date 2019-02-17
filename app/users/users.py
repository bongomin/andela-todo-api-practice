import psycopg2
from app.database.connect import Database

dbInstance = Database()


class Users():
    def signup(self, username, password):
        sql = "INSERT INTO users(username,password) VALUES(%s,%s)"
        try:
            self.conn = dbInstance.connectToDatabase()
            cur = self.conn.cursor()
            cur.execute(sql, [username, password])
            self.conn.commit()
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
