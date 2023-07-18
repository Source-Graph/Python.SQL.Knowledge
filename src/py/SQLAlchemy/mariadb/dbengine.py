from sqlalchemy import create_engine, text


class DBengine:
    def __init__(self, user="user", passwd="password", host="localhost", name="testdatabase", echo=True):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.name = name
        self.echo = echo
        self.master = create_engine(f"mysql+pymysql://{self.user}:{self.passwd}@{self.host}")
        self.engine = create_engine(f"mysql+pymysql://{self.user}:{self.passwd}@{self.host}/{self.name}", echo=self.echo)

    def query_exp(self, expression):
        with self.master.connect() as conn:
            result = conn.execute(expression)
            return result.all()
            conn.commit()

    def query(self, expression):
        with self.master.connect() as conn:
            conn.execute(expression)

    def list_database(self):
        return self.query_exp(text("SHOW DATABASES"))

    def exists(self, name):
        all = self.list_database()
        dbs = set()
        for i in all:
            dbs.add(i[0])
        return name in dbs

    def create_database(self):
        if self.exists(self.name):
            print(f"{self.name}, already exists!")
        else:
            self.query(text(f"CREATE DATABASE {self.name}"))
            print(f"Created database {self.name}")

    def delete_database(self):
        if self.exists(self.name):
            self.query(text(f"DROP DATABASE {self.name}"))
            print(f"Deleted database {self.name}")
        else:
            print(self.list_database())


if __name__ == '__main__':
    db = DBengine()
    db.create_database()
    db.delete_database()

