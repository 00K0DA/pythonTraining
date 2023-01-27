import random
from MyLogger.MyLogger import MyLogger
from Timer import Timer
from typing import List


def set_up() -> (str, str):
    list_length = random.randint(1, 100)
    target_value = random.randint(1, 100)
    int_list = [str(random.randint(1, 100)) for _ in range(list_length)]
    first_line = "{} {}".format(list_length, target_value)
    second_line = " ".join(int_list)
    return first_line, second_line


def main() -> None:
    logger = MyLogger("PythonTraining")
    timer = Timer(1)

    # create dummy input
    first_line, second_line = set_up()
    logger.info("first_line = {}".format(first_line))
    logger.info("second_line = {}".format(second_line))

    logger.info("Start Solve")
    timer.count_start()
    solve(first_line, second_line)
    timer.count_stop()
    logger.info("Finish Solve")

    tearDown(logger, timer)


def solve(first_line: str, second_line: str) -> None:
    target_value = first_line.split(" ")[1]
    int_list = second_line.split()
    if target_value in int_list:
        print("YES")
    else:
        print("NO")


def tearDown(logger: MyLogger, timer: Timer) -> None:
    logger.info("elapsed time is {}ms".format(timer.elapsed_time()))
    if timer.is_time_out():
        logger.error("Time Out!!")


if __name__ == "__main__":
    main()
