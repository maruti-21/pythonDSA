def login(username,password):
    if username==password:
        print("login successful")
    else:
        print("invalid credentials")
    
login(username="admin",password="admin")