from spdlog import ConsoleLogger, LogLevel
import unittest


def log_msg(logger, level):
    if level == LogLevel.TRACE:
        logger.trace('I am Trace')
    elif level == LogLevel.DEBUG:
        logger.debug('I am Debug')
    elif level == LogLevel.INFO:
        logger.info('I am Info')
    elif level == LogLevel.WARN:
        logger.warn('I am Warning')
    elif level == LogLevel.ERR:
        logger.error('I am Error')
    else:
        logger.critical('I am Critical')


def set_log_level(logger, level):
    print("Setting Log level to %d" % level)
    logger.set_level(level)


class Test(unittest.TestCase):
    def test_log_level(self):
        # multithreaded=False, stdout=True, colored=False
        logger = ConsoleLogger('Logger', False, True, False)
        for level in (LogLevel.TRACE, LogLevel.DEBUG, LogLevel.INFO, LogLevel.WARN,
                      LogLevel.ERR, LogLevel.CRITICAL):
            set_log_level(logger, level)
            log_msg(logger, level)


if __name__ == "__main__":
    unittest.main()
