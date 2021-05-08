# first install mysql connector w/pip
import mysql.connector

try:
    # try to connect to a database
    connection = mysql.connector.connect(host = 'mysql',
        database = 'python-db',
        user = 'root',
        password = ''
    )

    query = '''
        CREATE TABLE IF NOT EXISTS test_table(
            id int(11),
            something varchar(55),
            otherthing varchar(65),
            PRIMARY KEY (id)
        )
    '''

    if connection.is_connected():
        cursor = connection.cursor() # create a cursor
        cursor.execute(query)
        print('Successefully created table')

except mysql.connector.Error as error:
    print(error)
