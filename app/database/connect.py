import psycopg2


class Database():
    def connectToDatabase(self):

        try:
            connectionString = "host='localhost' user='postgres' password='walter123@Andela!' dbname='todos' port='5432'"
            self.conn = psycopg2.connect(connectionString)
            print("Connection established")
            return self.conn

        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
