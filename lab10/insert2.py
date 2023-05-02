import psycopg2
from config import config

sql ='''COPY phonebook(id,username,\
phone)
FROM 'C:\\Users\\User\\Desktop\\pp2\\lab10\\example.csv'
DELIMITER ','
CSV HEADER;'''

conn = None
try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
        
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
        if conn is not None:
            conn.close()

     