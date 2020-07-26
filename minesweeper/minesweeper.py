import sys
from game_runners.runners import Interactive_runner


def minesweeper():
    runner = Interactive_runner((10, 8), 8)
    runner.run()
    # runner.finish()


def main():
    minesweeper(sys.argv[1])


if __name__ == "__main__":
    main()
