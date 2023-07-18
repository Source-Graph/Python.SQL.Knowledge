from Ssali_Jonathan.create_tables import create_tables
from Ssali_Jonathan.persisting import add_user

def create():
    from mariadb.dbengine import DBengine
    db = DBengine()
    db.delete_database()
    db.create_database()

'''
def test():
    from Ssali_Jonathan.connect import testDb
    testDb()
'''

if __name__ == '__main__':
    # create_tables()
    add_user()