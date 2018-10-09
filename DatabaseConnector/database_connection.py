import pymysql


class Database:
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "root", "scott")
        self.cur = self.conn.cursor()

    def execute_query(self, Query):
        self.cur.execute(Query)
        row = self.cur.fetchone()
        return row

    def execute_query1(self, Query):
        self.cur.execute(Query)
        row = self.cur.fetchone()
        #while row is not None:
            #self.cur.execute(Query)
            #row = self.cur.fetchone()
        return row

    def execute_query12(self, Query):
        self.cur.execute(Query)
        self.conn.commit()

    def __exit__(self):
        self.cur.close()
        self.conn.close()
