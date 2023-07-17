from rawSQL.query import querySQL
from rawSQL.list import listDbs

def createDb(name="testdatabase"):
    sql = f"CREATE DATABASE {name}"
    if name in listDbs():
        print(f"Database '{name}' already exists")
    else:
        querySQL(sql, True)

if __name__ == '__main__':
    createDb("testdatabase")