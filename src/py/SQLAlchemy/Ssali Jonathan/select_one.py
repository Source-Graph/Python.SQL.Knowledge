from main import session
from models import User

jona = session.query(User).filter_by(username = 'jona').first()
paul = session.query(User).filter_by(username = 'paul').first()

print(jona)
