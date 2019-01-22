from canapea.model import User


def make_user(couchdb_connection, data):
    user_model = User(couchdb_connection)
    return user_model.create(data)


def test_create_model(couchdb_connection):
    user = make_user(couchdb_connection, {'name': 'canapea'})
    assert user.name == 'canapea'


def test_get_model(couchdb_connection):
    user_model = User(couchdb_connection)
    user = make_user(couchdb_connection, {'name': 'imagia2'})
    assert user.name == user_model.get(user.id).name


def test_delete_model(couchdb_connection):
    user = make_user(couchdb_connection, {'name': 'canapea'})
    user.delete()


def test_update(couchdb_connection):
    user_model = User(couchdb_connection)
    user = make_user(couchdb_connection, {'name': 'canapea'})
    user.name = 'imagia2'
    user.update()

    assert user.name == user_model.get(user.id).name


def test_bulk_insert_docs(couchdb_connection):
    user_model = User(couchdb_connection)
    user1 = User(couchdb_connection, name='imagia2')
    user2 = User(couchdb_connection, name='imagia1')
    user_model.insert_bulks_docs([user1, user2])
    users = user_model.list()

    assert len(users) == 2


def test_list_docs(couchdb_connection):
    user_model = User(couchdb_connection)
    users = user_model.list()

    assert len(users) == 0


def test_fetch_bulks_docs(couchdb_connection):
    user_model = User(couchdb_connection)
    user1 = make_user(couchdb_connection, {'name': 'imagia1'})
    user2 = make_user(couchdb_connection, {'name': 'imagia2'})
    users = user_model.fetch_bulks_docs(ids=[user1.id, user2.id])

    assert len(users) == 2


def test_fetch_bulks_docs_with_include_docs(couchdb_connection):
    user_model = User(couchdb_connection)
    user1 = make_user(couchdb_connection, {'name': 'imagia1'})
    user2 = make_user(couchdb_connection, {'name': 'imagia2'})

    users = user_model.fetch_bulks_docs(
        ids=[user1.id, user2.id],
        include_docs=True)

    assert len(users) == 2


def test_exist(couchdb_connection):
    user_model = User(couchdb_connection)
    user1 = make_user(couchdb_connection, {'name': 'imagia1'})

    assert user_model.exist(user1.id) is True


def test_dont_exist(couchdb_connection):
    user_model = User(couchdb_connection)

    assert user_model.exist('1a7d5b3896653fd699b747472c000ba6') is False
