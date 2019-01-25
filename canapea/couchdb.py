"""CouchDB Class.

Use Cloudant CouchDB client.
"""
from functools import partial

from cloudant.client import CouchDB as Cloudant
from cloudant.database import CouchDatabase
from cloudant.query import Query

from canapea.utils import to_dict


class CouchDB:
    """Couchdb database connection."""

    def __init__(self, username, password, host):
        self.connection = Cloudant(
            user=username,
            auth_token=password,
            url=host,
            connect=True)
        self.db = partial(CouchDatabase, self.connection)
        self.__class__.db = self.db

    @classmethod
    def init(cls, username, password, host):
        """Class object initializer."""
        cls.connection = Cloudant(
            user=username,
            auth_token=password,
            url=host,
            connect=True)
        cls.db = partial(CouchDatabase, client=cls.connection)
        return cls

    @classmethod
    def find(cls, type, selector={}, fields=[], limit=100):
        """List documents filtered by fields."""
        results = Query(cls.db(type), selector=selector, fields=fields,
                        limit=limit)
        return results()['docs']

    @classmethod
    def is_exist(cls, type, id):
        """Validate if the document exist in the database."""
        try:
            cls.db(type)[id]
            return True
        except KeyError:
            return False

    @classmethod
    def list(cls, type):
        for document in cls.db(type):
            yield document

    @classmethod
    def get(cls, type, id):
        """Retrieve document by id."""
        return cls.db(type)[id]

    @classmethod
    def create(cls, type, entity):
        """Create document from entity dict."""
        created = cls.db(type).create_document(entity)
        return created

    @classmethod
    def delete(cls, type, id):
        """Delete document itself."""
        cls.db(type)[id].delete()

    @classmethod
    def update(cls, type, entity):
        """Update document itself by changing attributes."""
        document = cls.db(type)[entity.id]
        for key in to_dict(entity):
            document[key] = getattr(entity, key)

        return document.save()

    @classmethod
    def fetch_bulks_docs(cls, type, ids, include_docs=False):
        """Retrieve documents by id."""
        results = cls.db(type).all_docs(keys=ids, include_docs=include_docs)
        if include_docs:
            return [result['doc'] for result in results['rows'] if
                    'doc' in result]
        else:
            return results['rows']

    @classmethod
    def insert_bulks_docs(cls, type, entities):
        """Create documents by a list of entities."""
        cls.db(type).bulk_docs(entities)

    @classmethod
    def exist(cls, type, id):
        """Check if the document exist or not."""
        return cls.db(type)[id] is None

    def put_attachment(self, type, id, name, file, content_type):
        """Insert an attachment file to a document."""
        self.db(type)[id].put_attachment(
            attachment=name,
            content_type=content_type,
            data=file)
        return self.db(type)[id]['_attachments']

    def delete_attachment(self, type, id, name):
        self.db[type][id].delete_attachment(name)
        return self.db(type)[id]['_attachments']
