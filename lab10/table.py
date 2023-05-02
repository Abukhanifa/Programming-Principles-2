import psycopg2
from config import config


def create_tables():
    """create tables in PostgreSQL database"""
    commands = (
        """
        CREATE TABLE PHONEBOOK (
            id SERIAL PRIMARY KEY,
            Username VARCHAR(255),
            Phone BIGINT 
        )
        """
    )
    
    conn = None
    try:
        params = config()
        
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute(commands)
           
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
            
if __name__ == '__main__':
    create_tables()
        
        
        
            
        
