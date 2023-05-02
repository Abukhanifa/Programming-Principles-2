#!/usr/bin/python

import psycopg2
from config import config

def update_phonebook(id, username):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE phonebook
                SET username = %s
                WHERE id = %s
                """
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (username, id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    update_phonebook(1, "Mikhail Lomonosov")

