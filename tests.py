"""
Example tests
"""
from pathlib import Path
from time import sleep

WORKSPACE = "./work_dir"


def test_7():
    pass


def test_8():
    pass


def test_9():
    pass


def test_10():
    pass


def test_111():
    print("Running test_111")
    with open(Path(WORKSPACE, "111.txt"), "w") as fp:
        fp.write("1111")
    sleep(3)


def test_222():
    print("Running test_222")
    sleep(3)


def test_333():
    """
    Test 333 is dependant on test 111
    """
    print("Running test_333")
    with open(Path(WORKSPACE, "111.txt")) as fp:
        print(fp.read())
    sleep(3)


def test_444():
    pass


def test_555():
    print("Running test_555")
    sleep(3)
    pass


def test_666():
    print("Running test_666")
    sleep(3)


def test_777():
    print("Running test_777")
    sleep(3)
