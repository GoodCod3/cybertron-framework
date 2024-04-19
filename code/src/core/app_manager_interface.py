from abc import ABCMeta, abstractmethod, abstractproperty

class IAppManager():
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        """
        Executes the application
        """
        raise NotImplementedError

    @abstractmethod
    def get_version(self):
        """
        Retrieves the application version
        """
        raise NotImplementedError

    @abstractmethod
    def get_summary(self):
        """
        Provides a summary of the processing
        """
        raise NotImplementedError
