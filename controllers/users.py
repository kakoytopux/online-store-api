from models.user import User
from operator import attrgetter

def add_user(user):
  name, surname, age, email, password = attrgetter('name', 'surname', 'age', 'email', 'password')(user)

  res = User.create_user(name, surname, age, email, password)
  
  return res