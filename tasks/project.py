# project.py
class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
    def get_name(self):
        print("Enter your name:")
        pass
    def age(self, current_year):
        print("Enter your age:")
        age = current_year - self.birthyear
        return age

user = User("john", 1999)
print(user.age(2023))
print(user.get_name())
# The code above is a basic implementation
# of a User class
# with methods to get the user's name and
# calculate their age.




