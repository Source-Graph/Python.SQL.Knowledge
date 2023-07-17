from main import session
from models import User, Comment
from sqlalchemy import select

# statement = select(User).where(User.username.in_(['paul','cathy']))
#
# result = session.scalars(statement)
#
# for user in result:
#     print(user)

users = session.query(User).all()

for user in users:
    print(user)