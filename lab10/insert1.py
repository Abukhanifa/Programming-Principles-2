import psycopg2 
from config import config


def insert_username(user_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO phonebook(username, phone) VALUES(%s, %s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,user_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
if __name__ == '__main__':
     insert_username([
        ('Michael Lomonosov', 7606535301,),
        ('George Orwell', 7608588185,),
        ('Denzel Washington', 7607567569,),
        ('Simon Black', 7606480202,),
        ('George Jeff', 7606468588,)
     ])
     
    
    
        
    
  
   