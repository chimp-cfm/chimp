import logging


class Logger:
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        self._logger.exception(msg, *args, **kwargs)

    def log(self, msg, *args, **kwargs):
        self._logger.log(msg, *args, **kwargs)
