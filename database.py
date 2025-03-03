import sqlite3

class Database:
    def __init__(self, dbName="jobs.db"):
        self.conn = sqlite3.connect('jobs.db')
        self.cursor = self.conn.cursor()
        self.createTables()


    #Create a table

    def createTables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs ( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         title TEXT,
          companyName TEXT,
          location TEXT,
           timePosted TEXT,
           salary TEXT,
            jobType TEXT
        )
        """)
        self.conn.commit()




    def insertJob(self, job):
        self.cursor.execute("""INSERT INTO jobs (title, companyName, location, timePosted, salary, jobType) VALUES (?,?,?,?,?,?)""",
                       (job["title"], job["companyName"], job["location"], job["timePosted"], job["salary"], job["jobType"]))
        self.conn.commit()

    def fetchJobs(self):
        self.cursor.execute("""SELECT * FROM jobs""")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
