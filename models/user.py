from middlewares.db import set_data_db

class User():
  def insert_user(name, surname, age, email, password):
    query_create_user = """
    INSERT INTO users (name, surname, age, email, password) VALUES ('%s', '%s', %d, '%s', '%s')
    """ % (name, surname, age, email, password)
    
    res = set_data_db(query_create_user)

    return res