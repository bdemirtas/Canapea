import json
import logging
from uuid import uuid4

from canapea import EntityAbstractClass
from canapea.connection import get_connection
from canapea.utils import to_dict


def _class_type(_class):
    """Return model type."""
    return _class.__name__.lower()


def _instance_type(_instance):
    """Return model instance type."""
    return _class_type(_instance.__class__)


class Entity(EntityAbstractClass):
    """Representing a CouchDB document."""

    def __init__(self, _id, type, alias=None):
        self._id = _id or str(uuid4())
        self.database = get_connection()
        self.__class__.database = self.database
        self.type = type
        self.attachments = {}

    @property
    def id(self):
        """Representin a property getting the hidden id from Couchdb."""
        return self._id

    @classmethod
    def init(cls, database, _id, type):
        """Class object initializer."""
        cls._id = _id or str(uuid4())
        cls.database = database
        cls.type = type
        cls.attachments = {}

    @classmethod
    def create(cls, entity):
        """Create document from entity dict."""
        return cls(**cls.database.create(_class_type(cls), entity))

    def delete(self):
        """Delete document itself."""
        self.database.delete(_instance_type(self), self.id)

    @classmethod
    def exist(cls, id):
        """Validate if the document exist in the database."""
        return cls.database.is_exist(_class_type(cls), id)

    @classmethod
    def fetch_bulks_docs(cls, ids, include_docs=False):
        """Retrieve documents by id."""
        results = cls.database.fetch_bulks_docs(
            _class_type(cls), ids, include_docs=include_docs)

        return [cls(**result) for result in results]

    @classmethod
    def get(cls, id):
        """Retrieve document by id."""
        class_name = _class_type(cls)
        entity = cls.database.get(class_name, id)
        if not entity:
            logging.error('{} [{}] not found'.format(class_name, id))
        return cls(**entity)

    @classmethod
    def insert_bulks_docs(cls, entities):
        """Bullk document creation."""
        return cls.database.insert_bulks_docs(
            _class_type(cls), [entity.to_dict() for entity in entities])

    @classmethod
    def list(cls):
        """List all documents."""
        return [cls(**entity) for entity in
                cls.database.list(_class_type(cls))]

    def update(self):
        """Update document itself by changing attributes."""
        return self.database.update(_instance_type(self), self)

    def put_attachment(self, name, file, content_type):
        self.attachments = self.database.put_attachment(
            _instance_type(self), self.id, name, file, content_type)

    def delete_attachment(self, name):
        self.attachments = self.database.delete_attachment(
            _instance_type(self), self.id, name)

    def __repr__(self):
        return json.dumps(to_dict(self))

    def to_dict(self):
        return to_dict(self)
