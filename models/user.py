from utils.db import setDataDb

class User():
  def create_user(name, surname, age, email, password):
    query_create_user = "INSERT INTO users (name, surname, age, email, password) VALUES ('%s', '%s', %d, '%s', '%s')" % (name, surname, age, email, password)
    res = setDataDb(query_create_user)

    # query_select_user = "SELECT id FROM users WHERE id = %s" % (id)
    # res = setDataDb(query_select_user)

    return res