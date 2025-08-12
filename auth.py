USERS = {"admin": "admin123"}  

def login(username, password):
    return USERS.get(username) == password