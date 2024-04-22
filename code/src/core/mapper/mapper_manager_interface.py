from abc import ABCMeta, abstractmethod


class IMapperManager:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_id(self):
        """
        Retrieves the manager ID
        """
        raise NotImplementedError

    @abstractmethod
    def get(self):
        """
        Retrieves the mapped data
        """
        raise NotImplementedError

    @abstractmethod
    def get_flattened(self):
        """
        Retrieves the mapped data flattened
        """
        raise NotImplementedError
