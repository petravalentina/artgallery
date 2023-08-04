import psycopg2

instance_name = "sat-kapita-selekta-b:asia-southeast2:training-kapita-selekta"
port = 5432
db = "postgres"
user = "postgres"
password = "FwF6qfEA5AzlztzG"

# param = f"host='localhost' port={port} dbname='{db}' user='{user}' password='{password}'"
param = f"host='/cloudsql/{instance_name}' port={port} dbname='{db}' user='{user}' password='{password}'"


def select(query=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query)

        data = curs.fetchall()
        curs.close()
        del(conn)
        return data
    
    except Exception as e:
        print(e)
        return False,str(e)
    
def insert(query="", paramm=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query, paramm)
        conn.commit()
        curs.close()
        del(conn)
        return True
        
        
    except Exception as e:
        print(e)
        return False,str(e)
    
def selectcollection(query="", paramm=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query, paramm)

        data = curs.fetchall()
        curs.close()
        del(conn)
        return data
    
    except Exception as e:
        print(e)
        return False,str(e)
    
def selectexhibition(query="", paramm=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query, paramm)

        data = curs.fetchall()
        curs.close()
        del(conn)
        return data
    
    except Exception as e:
        print(e)
        return False,str(e)
    
def update(query="", paramm=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query, paramm)
        conn.commit()
        curs.close()
        del(conn)
        return True
        
        
    except Exception as e:
        print(e)
        return False,str(e)
    
def delete(query="", paramm=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query, paramm)
        conn.commit()
        curs.close()
        del(conn)
        return True
        
        
    except Exception as e:
        print(e)
        return False,str(e)
    

def delete2(query="", paramm=""):
    try:
        conn = psycopg2.connect(param)

        curs = conn.cursor()

        curs.execute(query, paramm)
        conn.commit()
        curs.close()
        del(conn)
        return True
        
        
    except Exception as e:
        print(e)
        return False,str(e)
    
