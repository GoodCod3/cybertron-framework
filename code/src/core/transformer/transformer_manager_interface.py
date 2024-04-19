from abc import ABCMeta, abstractmethod, abstractproperty

class ITransformerManager():
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
    def transform(self, data):
        """
        Transforms the input data
        """
        raise NotImplementedError
