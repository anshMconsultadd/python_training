# Create a class with private attributes for sensitive data (e.g., user
# passwords) and methods for secure access and modificatio


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

ansh=User("Ansh", "12345")
print(ansh.get_username())
ansh.set_password("54321")
print(ansh.get_password())