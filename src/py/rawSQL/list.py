from rawSQL.query import queryFn

def _listPrint(connection):
    show_db_query = "SHOW DATABASES"
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            print(db)

def _listSet(connection):
    show_db_query = "SHOW DATABASES"
    databases = set()
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            databases.add(db[0])
    return databases


def listDbs():
    return queryFn(_listSet)

if __name__ == '__main__':
    print(listDbs())

    print("testdatabase" in listDbs())