import logging
import time

class Logger:
    def __init__(self):
        self.loggers = dict()

    def function_logger(self, filename):
        logger = logging.getLogger(filename)
        if self.loggers.get(filename):
            return self.loggers[filename]
        else:
            logger.setLevel(logging.DEBUG)
            filepath = "{0}.log".format("logs/" + filename + "_" + time.strftime("%x").replace("/", "_"))
            fh = logging.FileHandler(filepath)
            fh.setLevel(logging.DEBUG)
            fh_format = logging.Formatter('%(asctime)s - line:%(lineno)d %(levelname)-8s - %(message)s')
            fh.setFormatter(fh_format)
            logger.addHandler(fh)
            self.loggers[filename] = logger
        return logger