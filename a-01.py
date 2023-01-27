import random
from MyLogger.MyLogger import MyLogger
from Timer import Timer


def set_up() -> int:
    return random.randint(0, 100)


def main() -> None:
    logger = MyLogger("PythonTraining")
    timer = Timer(1)
    num = set_up()
    logger.info("input is {}".format(num))

    logger.info("Start Solve")
    timer.count_start()
    solve(num)
    timer.count_stop()
    logger.info("Finish Solve")

    tearDown(logger, timer)


def solve(number: int) -> None:
    print(number ** 2)


def tearDown(logger: MyLogger, timer: Timer) -> None:
    logger.info("elapsed time is {}ms".format(timer.elapsed_time()))
    if timer.is_time_out():
        logger.error("Time Out!!")


if __name__ == "__main__":
    main()
