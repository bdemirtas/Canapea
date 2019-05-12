from canapea.couchdb import CouchDB


connec = None


def get_connection() -> CouchDB:
    global connec
    if connec:
        return connec


def register_connection(username, password, url='http://localhost:5984'):
    global connec
    connec = CouchDB(username, password, url)


def connection(username, password, url):
    if not get_connection():
        register_connection(username, password, url)

    return get_connection()


def disconnect():
    global connec
    if get_connection():
        get_connection().connection.disconnect()
        del connec
