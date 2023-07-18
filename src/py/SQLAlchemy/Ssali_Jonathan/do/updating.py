from main import session
from models import Comment, User

comment = session.query(Comment).filter_by(id=1).first()

comment.text = "This is an updated comment"

session.commit()