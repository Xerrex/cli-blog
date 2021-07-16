from models import *

users = {}
user_comments = {}


class Cli(object):

    def checkuser(self, username):
        # Finds whether the user is in the list
        users = [user for user in users_lists if user.username == username]
        if users:
            return user
        return False

    def login(self, username, password):
        # get list of users
        if checkuser(username) and username.password == password:
            print('User logged in')
            return True

    def getId(self, data_structure):
    	return(len(data_structure) + 1)

    def signup(self, username, password):
        user = User(username, password)

        # id for the next object
        id = self.getId(users)

        # append user to the list of users in the app
        users[id] = user
        return True

    

    def addComments(self, message, author):
        # Check whether user already exists
        if self.checkuser(author):
            comment = Comments(message, author)
            # generate id for the next comment
            id = self.getId(user_comments)

            user_comments[id] = comment
            return True

        return False



