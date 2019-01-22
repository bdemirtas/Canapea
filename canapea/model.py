from canapea.base import Entity


class DefaultTypes:
    """Enumerator containing entity names."""

    USER = 'user'


class User(Entity):
    """Model representing User in CouchDB."""

    def __init__(self, database, _id=None, name=None, type=DefaultTypes.USER,
                 **others):
        super(User, self).__init__(database, _id, type)
        self.name = name
        self.type = type
