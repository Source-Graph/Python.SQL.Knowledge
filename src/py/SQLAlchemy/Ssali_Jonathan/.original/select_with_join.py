from main import session
from models import Comment, User
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(
    User.username == 'jona'
).where(
    Comment.text == 'Hello World'
)

result = session.scalars(statement).one()

print(result)