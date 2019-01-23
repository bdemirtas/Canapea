from abc import (
    ABC,
    abstractmethod,
)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


class EntityAbstractClass(ABC):

    @classmethod
    @abstractmethod
    def create(cls, entity):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def delete(cls):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def exist(cls, id):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def fetch_bulks_docs(cls, ids, include_docs=False):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def get(cls, id):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def insert_bulks_docs(cls, entities):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def list(cls):
        raise NotImplementedError("Subclasses should implement this!")

    @classmethod
    @abstractmethod
    def update(cls):
        raise NotImplementedError("Subclasses should implement this!")
