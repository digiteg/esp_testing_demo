
import microtest

import wallet


def main():
    runner = microtest.Microtest()
    runner.run_test(wallet,True, False)


if __name__ == "__main__":
    main()
