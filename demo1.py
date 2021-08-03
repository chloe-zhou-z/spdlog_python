import spdlog
from spdlog import ConsoleLogger
import unittest


class Test(unittest.TestCase):
    def test_console(self):
        name = 'aha?'
        logger = ConsoleLogger(name, multithreaded=False, stdout=True, colored=False, async_mode=False)
        # or logger = ConsoleLogger(name, False, True, False)  # multithreaded=False, stdout=True, colored=False
        logger.trace('Trace what?')
        logger.debug('Any thing wrong?')
        logger.info('This is a piece of useless information')
        logger.warn('Actually,no warn for you~')
        logger.error('Always error')
        logger.critical('I am so sleepy~~')

        # or spdlog.drop(name)
        spdlog.drop_all()


if __name__ == "__main__":
    unittest.main()
