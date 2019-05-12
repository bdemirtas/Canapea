import subprocess
import time

import pytest

from canapea.connection import connection
from tests.integration.model import DefaultTypes


@pytest.fixture(scope='module')
def docker_couchdb():
    port = '5984'
    password = 'canapea'
    user = 'canapea'

    docker_id = subprocess.check_output(
        [
            'docker',
            'run',
            '-e',
            f'COUCHDB_USER={user}',
            '-e',
            f'COUCHDB_PASSWORD={password}',
            '-p',
            f'{port}:{port}',
            '-d',
            'couchdb:2.3.0',
        ]).decode().strip()

    time.sleep(5)

    yield f'http://127.0.0.1:{port}'

    subprocess.check_call(['docker', 'rm', '-f', docker_id])


@pytest.fixture(autouse=True)
def open_connection(docker_couchdb):
    database = connection('canapea', 'canapea', docker_couchdb)
    database.connection.create_database(DefaultTypes.USER)

    yield database

    database.connection.delete_database(DefaultTypes.USER)
