import mysql.connector
import random 


def db_connect():
    conn = mysql.connector.connect(host="localhost", user="root", password="Anmol@1234")
    return conn


def if_exists(text_id):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('USE PasteBin')
    cursor.execute(f'SELECT EXISTS(SELECT * FROM LINKS WHERE id="{text_id}")')
    res = cursor.fetchall()[0][0]
    return res


def gen_id():
    while True:
        with open('nouns.txt') as f:
            nouns = f.readlines()

        nouns = [noun.strip('\n').capitalize() for noun in nouns]

        with open('adjs.txt') as f:
            adjs = f.readlines()

        adjs = [adj.strip('\n').capitalize() for adj in adjs]

        text_id = random.choice(nouns)+random.choice(adjs)

        if not if_exists(text_id):
            return text_id





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
    # create_database("PasteBin")
    # create_table()
    #
    # add_to_database("Anmol")
    # get_results()
    gen_id()

if __name__ == '__main__':
    main()