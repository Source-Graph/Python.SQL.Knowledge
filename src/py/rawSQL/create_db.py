from rawSQL.query import querySQL

def createDb(name="yourdb"):
    sql = f"CREATE DATABASE {name}"
    querySQL(sql, True)

if __name__ == '__main__':
    createDb("botengine")