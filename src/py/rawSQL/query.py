from mysql.connector import connect, Error

def queryFn(func):
    with connect(
        host="localhost",
        user="user",
        password="password"
    ) as connection:
        return func(connection)

def querySQL(sql, commit=False):
    with connect(
            host="localhost",
            user="user",
            password="password",
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        if commit:
            connection.commit()
        # Return
        return cursor

if __name__ == '__main__':
    print("")
