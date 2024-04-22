import traceback
from datetime import datetime


class Logger:
    """
    Logs messages to the stdout
    """

    LOG_TYPE_INFO = "INFO"
    LOG_TYPE_WARNING = "WARNING"
    LOG_TYPE_ERROR = "ERROR"
    LOG_TYPE_CRITICAL = "CRITICAL"

    def info(self, message):
        return self.__log(self.LOG_TYPE_INFO, message)

    def warning(self, message, from_exception=False):
        return self.__log(self.LOG_TYPE_WARNING, message, from_exception)

    def error(self, message, from_exception=False):
        return self.__log(self.LOG_TYPE_ERROR, message, from_exception)

    def critical(self, message, from_exception=False):
        return self.__log(self.LOG_TYPE_CRITICAL, message, from_exception)

    def __log(self, type, message, from_exception=False):
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        result = f"[{timestamp}] {type} | {message}"
        if from_exception:
            result = result + f" | {traceback.format_exc()}"

        return result
