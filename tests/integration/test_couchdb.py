from tests.integration.model import User


def make_user(data):
    user_model = User()
    return user_model.create(data)


def test_create_model():
    user = make_user({'name': 'canapea'})
    assert user.name == 'canapea'


def test_get_model():
    user_model = User()
    user = make_user({'name': 'imagia2'})
    assert user.name == user_model.get(user.id).name


def test_delete_model():
    user = make_user({'name': 'canapea'})
    user.delete()


def test_update():
    user_model = User()
    user = make_user({'name': 'canapea'})
    user.name = 'imagia2'
    user.update()

    assert user.name == user_model.get(user.id).name


def test_bulk_insert_docs():
    user_model = User()
    user1 = User(name='imagia2')
    user2 = User(name='imagia1')
    user_model.insert_bulks_docs([user1, user2])
    users = user_model.list()

    assert len(users) == 2


def test_list_docs():
    user_model = User()
    users = user_model.list()

    assert len(users) == 0


def test_fetch_bulks_docs():
    user_model = User()
    user1 = make_user({'name': 'imagia1'})
    user2 = make_user({'name': 'imagia2'})
    users = user_model.fetch_bulks_docs(ids=[user1.id, user2.id])

    assert len(users) == 2


def test_fetch_bulks_docs_with_include_docs():
    user_model = User()
    user1 = make_user({'name': 'imagia1'})
    user2 = make_user({'name': 'imagia2'})

    users = user_model.fetch_bulks_docs(
        ids=[user1.id, user2.id],
        include_docs=True)

    assert len(users) == 2


def test_exist():
    user1 = make_user({'name': 'imagia1'})

    assert User.exist(user1.id) is True


def test_dont_exist():
    user_model = User()

    assert user_model.exist('1a7d5b3896653fd699b747472c000ba6') is False


def test_put_attachment():
    user = make_user({'name': 'imagia1'})
    user.put_attachment('test', b'sad', content_type='text')
