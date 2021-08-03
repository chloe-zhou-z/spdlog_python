import spdlog
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        spdlog.basic_file_sink_st('asynclogger.txt')  # create a basic logger

        logger = spdlog.FileLogger('name', 'asynclogger.txt', False,
                                   False)  # multithreaded=false, truncate=false
        logger.async_mode()  # setting async model
        # queue_size = 2048, thread_count = 4, overflow_policy = 1
        # logger.spdlog.set_async_mode(2048, 4, 1)
        for i in range(100):
            logger.info('You have create a async logger. test_%d' % i)

        # multi sink example
        console_sink = spdlog.stdout_sink_mt()

        # level: trace=0, debug=1, info=2, warn=3, error=4, critical=5, off=6
        console_sink.set_level(3)

        file_sink = spdlog.basic_file_sink_mt('basic.txt')
        file_sink.set_level(0)
        sink = [file_sink, console_sink]
        logger_multi = spdlog.SinkLogger('multi_sink', sink)
        logger_multi.set_level(1)

        # logger.set_pattern('{:%Y-%m-%d --- %H:%M:%S}', spdlog.PatternTimeType(0))
        # while use set_pattern, inside '' must be string

        logger_multi.warn('This should appear in both console and file?')
        logger_multi.info('This message should not appear in the console, only in the file')
        # end of multi sink example

        # binary example
        num = [10, 20, 30, 40]
        binary_logger = spdlog.stdout_sink_st()
        logger_n = spdlog.SinkLogger("name", [binary_logger])
        logger_n.info('{:02X} {:02X} {:02X} {:02X}'.format(*num))
        logger_n.info('{:#X} {:#b} {:#e} {:#o}'.format(*num))
        # end of binary example

        get_logger = spdlog.get('name')
        get_logger.info('test spdlog.get, and this will be showed in name')  # write into 'name' logger

        get_logger.flush()
        get_logger.flush_on(2)  # number is level
        get_logger.set_error_handler(Warning)  # I am not sure

        # null_sink seams to do nothing
        null_logger = spdlog.null_sink_mt()
        logger_1 = spdlog.SinkLogger("null", [null_logger])
        logger_1.info("Notice: this will not be showed.")
        get_logger = spdlog.get('null')
        get_logger.debug('test spdlog.get')


if __name__ == '__main__':
    unittest.main()
