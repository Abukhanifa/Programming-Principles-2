import psycopg2
from config1 import config


def get_parts(lim, off):
    """ offset and limit """
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
        
        cur.callproc('get_data_offset_limit', (lim,off))
        # process the result set
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

lim = int(input())
off = int(input())

if __name__ == '__main__':
        get_parts(lim,off)

 