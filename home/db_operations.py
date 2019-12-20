import mysql.connector
import random 


def gen_id():
    return random.randint(0, 10000)


def db_connect():
    conn = mysql.connector.connect(host="localhost", user="root", password="Anmol@1234")
    return conn


def create_database(name):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        cursor.execute(f'CREATE DATABASE {name}')
    except mysql.connector.errors.DatabaseError as e:
        if str(e)[-15:] == "database exists":
            print('Database Already Exists.')
        else:
            print(str(e))

    conn.commit()
    cursor.close()
    conn.close()


def create_table(db_name="PasteBin"):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f'USE {db_name}')
    sql = """
        CREATE TABLE LINKS(
        id text PRIMARY KEY,
        text_to_be_stored text NOT NULL
    )
    """
    try:
        cursor.execute(sql)
    except Exception as e:
        if str(e)[-14:] == "already exists":
            print("Table Already exists.")
        else:
            print(str(e))

    conn.commit()
    cursor.close()
    conn.close()


def get_results(table_name="LINKS", db_name="PasteBin"):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f'USE {db_name}')
    cursor.execute(f'SELECT * FROM {table_name}')
    res = cursor.fetchall()
    return res


def add_to_database(text, table_name="LINKS", db_name="PasteBin"):
    conn = db_connect()
    cursor = conn.cursor()

    temp_id = gen_id()

    cursor.execute(f'USE {db_name}')
    cursor.execute(f'INSERT INTO {table_name} VALUES("{temp_id}", "{text}")')

    conn.commit()
    cursor.close()
    conn.commit()

    return temp_id


def main():
    create_database("PasteBin")
    create_table()
    
    add_to_database("Anmol")
    get_results()


if __name__ == '__main__':
    main()