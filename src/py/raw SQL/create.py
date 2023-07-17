from mysql.connector import connect, Error

def queryPrint(sql, commit=False):
    with connect(
            host="localhost",
            user="vpn",
            password="base12universe",
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        if commit:
            connection.commit()
        # Return
        return cursor

def createDb():
    create = "CREATE DATABASE yourdb"
    queryPrint(create, True)

def queryDb(func):
    with connect(
        host="localhost",
        user="vpn",
        password="base12universe"
    ) as connection:
        func(connection)

def listall():
    with connect(
        host="localhost",
        user="vpn",
        password="base12universe"
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)

def listdbs(connection):
    show_db_query = "SHOW DATABASES"
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            print(db)
