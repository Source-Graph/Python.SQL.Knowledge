from rawSQL.query import queryFn

def _listFn(connection):
    show_db_query = "SHOW DATABASES"
    with connection.cursor() as cursor:
        cursor.execute(show_db_query)
        for db in cursor:
            print(db)

def listDbs():
    queryFn(_listFn)

if __name__ == '__main__':
    listDbs()