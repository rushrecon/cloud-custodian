from c7n.version import version
from c7n.actions import BaseAction


def main(ignored_args=()):
    print('BaseAction object: ' + str(BaseAction()))
    print('Version from test main: ' + version)


if __name__ == '__main__':
    main()