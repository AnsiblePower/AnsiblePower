__author__ = 'dborysenko'
from arm.commands import init


def installRole():
    runner = init.init()
    runner.run()


if __name__ == "__main__":
    installRole()