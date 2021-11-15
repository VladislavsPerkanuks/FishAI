from flask_login import UserMixin
from flask_login._compat import unicode


class User(UserMixin):
    def __init__(self, id, name, username, password):
        self.id = unicode(id)
        self.name = name
        self.username = username
        self.password = password
        self.authenticated = False