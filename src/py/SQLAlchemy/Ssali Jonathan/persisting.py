from models import User, Comment
from main import session


user1 = User(
    username = 'jona',
    email_address = "johnathan@sql.org",
    comments = [
        Comment(text="Hello World"),
        Comment(text="Please subscribe"),
    ]
)

paul = User(
    username = 'paul',
    email_address = "paul@sql.org",
    comments = [
        Comment(text="What's up?"),
        Comment(text="Please subscribe"),
    ]
)

cathy = User(
    username = 'cathy',
    email_address = "cathy@sql.org",
)

session.add_all([user1, paul, cathy])
session.commit()