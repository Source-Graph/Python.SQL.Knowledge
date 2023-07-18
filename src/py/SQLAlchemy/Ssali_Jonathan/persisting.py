from .models import User, Comment
from .session import session


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

def add_user():
    session.add_all([user1, paul, cathy])
    session.commit()