import random
from MyLogger.MyLogger import MyLogger
from Timer import Timer


def set_up():
    pass


def main() -> None:
    logger = MyLogger("PythonTraining")
    timer = Timer(1)

    # create dummy input
    set_up()

    logger.info("Start Solve")
    timer.count_start()
    solve()
    timer.count_stop()
    logger.info("Finish Solve")

    tearDown(logger, timer)


def solve() -> None:
    pass


def tearDown(logger: MyLogger, timer: Timer) -> None:
    logger.info("elapsed time is {}ms".format(timer.elapsed_time()))
    if timer.is_time_out():
        logger.error("Time Out!!")


if __name__ == "__main__":
    main()
