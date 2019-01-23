from canapea.couchdb import CouchDB


DEFAULT_ALIAS_NAME = 'default'
connections = {}


def get_connection(alias=None) -> CouchDB:
    if alias is None:
        return connections[DEFAULT_ALIAS_NAME]

    if alias in connections:
        return connections[alias]


def register_connection(alias, username, password, url='http://localhost:5984'):
    connection = CouchDB(username, password, url)
    connections[alias] = connection
    return connection


def connection(username, password, url, alias=DEFAULT_ALIAS_NAME):
    if alias not in connections:
        register_connection(alias, username, password, url)

    return get_connection()


def disconnect(alias=DEFAULT_ALIAS_NAME):
    if alias in connections:
        get_connection(alias=alias).connection.disconnect()
        del connections[alias]
