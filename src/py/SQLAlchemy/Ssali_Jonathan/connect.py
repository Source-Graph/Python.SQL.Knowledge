from sqlalchemy import text
from mariadb.dbengine import DBengine

db = DBengine(echo=True)

engine = db.engine

def testDb():
    with engine.connect() as connection:
        result = connection.execute(text('select "Hello"'))

        print(result.all())