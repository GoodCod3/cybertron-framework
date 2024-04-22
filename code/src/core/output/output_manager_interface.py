from abc import ABCMeta, abstractmethod


class IOutputManager:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_id(self):
        """
        Retrieves the manager ID
        """
        raise NotImplementedError

    @abstractmethod
    def set_mapper(self, mapper_manager):
        """
        Sets the mapper
        """
        raise NotImplementedError

    @abstractmethod
    def put(self, data):
        """
        Puts the transformed data
        """
        raise NotImplementedError
