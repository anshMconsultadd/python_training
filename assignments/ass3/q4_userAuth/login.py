from q4_userAuth.password_has import hash_password


users = {
    "user1": hash_password("password123"),
    "user2": hash_password("mypassword"),
}

def verify_login(username, password):
   
    hashed_password = hash_password(password)
    if username in users and users[username] == hashed_password:
        return True
    return False
