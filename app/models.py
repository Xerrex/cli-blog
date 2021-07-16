from datetime import datetime
class User (object):

    def __init__(self, username, password):
         self.username = username
         self.password = password
         self.role = "normal"


    def __repr__(self):
        return '<User {}'.format(self.username)

class Admin(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "admin"


class Moderator(User):
    
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "moderator"

class Comment(object):
    """
    Comments are simply a message, a timestamp, and the author.
    """
    def __init__(self, message, author):
        self.message = message
        self.author = author
        self.timestamp = datetime.utcnow()


class Reply(Comment):

    def __init__(self, message, author, reply_msg):
        super.__init__(message, author)
        self.repy_msg = reply_msg

