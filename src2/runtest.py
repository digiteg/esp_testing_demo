
from microtest.microtestrunner import MicroTestRunner

import test_wallet
import test_fibonacci


def main():
    runner = MicroTestRunner(globals())
    runner.exec()

if __name__ == "__main__":
    main()
