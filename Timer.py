from MyLogger.MyLogger import MyLogger
import time


class Timer:
    logger = MyLogger("Timer")

    def __init__(self, time_out_ms: int):
        self.time_out_ms = time_out_ms
        self.start_time = None
        self.end_time = None

    def count_start(self) -> None:
        self.logger.info("Start Timer")
        self.start_time = time.time()

    def count_stop(self) -> None:
        self.end_time = time.time()
        self.logger.info("Stop Timer")

    def elapsed_time(self) -> int:
        return self.end_time - self.start_time

    def is_time_out(self) -> bool:
        return self.elapsed_time() > self.time_out_ms
