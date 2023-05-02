import psycopg2
from config1 import config

def add_part(name, phone_num):
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()

        # call a stored procedure
        cur.execute('CALL add_one(%s, %s)', (name, phone_num))

        # commit the transaction
        conn.commit()

        # close the cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

name = str(input())
phone_num = int(input())
if __name__ == '__main__':
    add_part(name, phone_num)
    