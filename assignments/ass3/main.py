from q4_userAuth.login import verify_login
from q4_userAuth.activity import log_activity

def main():
    print("Welcome to User Authentication System!")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if verify_login(username, password):
        print("Login successful!")
        log_activity(username, "Login")
    else:
        print("Login failed!")
        log_activity(username, "Failed Login")

if __name__ == "__main__":
    main()
