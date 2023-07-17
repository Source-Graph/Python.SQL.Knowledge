from rawSQL.query import querySQL

def deleteDb(name="yourdb"):
    sql = f"DROP DATABASE {name}"
    querySQL(sql, True)

if __name__ == '__main__':
    deleteDb("botengine")