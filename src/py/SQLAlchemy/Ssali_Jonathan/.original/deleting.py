from main import session
from models import Comment, User


comment = session.query(Comment).filter_by(id=1).first()

session.delete(comment)

session.commit()