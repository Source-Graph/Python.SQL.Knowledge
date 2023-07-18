from SQLAlchemy.mariadb.dbengine import DBengine

if __name__ == '__main__':
    db = DBengine()
    db.create_database()
    print(db.list_database())
