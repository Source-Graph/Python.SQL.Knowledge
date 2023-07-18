from .models import Base, User, Comment
from .connect import engine


def create_tables():
    print("CREATING TABLES >>>> ")
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_tables()
