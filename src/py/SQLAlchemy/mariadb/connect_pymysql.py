# https://docs.sqlalchemy.org/en/20/dialects/mysql.html
from sqlalchemy import create_engine, text

user = "root"
passwd = "password"
host = "localhost"
dbname = "testdatabase"


engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}/{dbname}")

def testConnection():
    with engine.connect() as connection:
        result = connection.execute(text('select "Hello"'))
        print(result.all())

if __name__ == '__main__':
    testConnection()
