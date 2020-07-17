
from microtest.microtestrunner import MicroTestRunner

#import test_wallet
#import test_fibonacci
import test_fixture1

def main():
    runner = MicroTestRunner(globals())
    runner.exec()

if __name__ == "__main__":
    main()
