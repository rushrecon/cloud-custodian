from c7n.version import version


def main(ignored_args=()):
    print('Version from test main: ' + version)


if __name__ == '__main__':
    main()