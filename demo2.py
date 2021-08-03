import spdlog
import unittest


class Test(unittest.TestCase):
    def test_sink(self):
        # change the suffix _st into _mt, run in multithreading, same as the others

        stdout_logger = spdlog.stdout_sink_st()
        # or create a color logger
        # stdout_logger = spdlog.stdout_color_sink_mt()
        logger_1 = spdlog.SinkLogger("name", [stdout_logger])
        logger_1.info("This is a stdout_logger.")
        # info can be replaced by warn, error, critical if it's needed...

        stderr_logger = spdlog.stderr_sink_st()
        # or create a color logger
        # stderr_logger = spdlog.stderr_color_sink_mt()
        logger_2 = spdlog.SinkLogger("name", [stderr_logger])
        logger_2.info("This is a stderr_logger.")
        # info can be replaced by warn, error, critical if it's needed...

        # create a basic logger
        spdlog.basic_file_sink_st('filename.txt')
        # multithreaded=false, truncate=false
        logger_3 = spdlog.FileLogger('name', 'filename.txt', False,
                                     False)
        logger_3.info('You have create a basic logger.')
        # info can be replaced by warn, error, critical if it's needed...

        # hours=8,minutes=30
        daily_logger = spdlog.daily_file_sink_st('filename_daily.log', 8, 30)
        # update at 8:30am
        logger_4 = spdlog.SinkLogger('name', [daily_logger])
        logger_4.info('This is a daily logger.')
        # info can be replaced by warn, error, critical if it's needed...

        spdlog.rotating_file_sink_st('filename_rotate.log', 1024,
                                     5)  # create a rotate file, size=1024, file number=5
        # multithreaded=false, async_mode=False
        logger_5 = spdlog.RotatingLogger('name1', 'filename_rotate.log', False, 1024, 5, False)
        logger_5.info('This is a rotate logger.')
        # info can be replaced by warn, error, critical if it's needed...

        spdlog.drop_all()


if __name__ == "__main__":
    unittest.main()
