# Not actually generated as can be observed.
# Used as a workaround for relative imports.
# https://github.com/bazelbuild/bazel/issues/808

import argparse
import unittest


def get_module():
    parser = argparse.ArgumentParser()
    parser.add_argument('--module', default=None)
    args, unknown = parser.parse_known_args()
    return args.module


if __name__ == "__main__":
    target_module = get_module()
    if not target_module:
        raise EnvironmentError("Please specify a test module with --module=(target module)")

    test_suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromName(target_module)])
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suite).wasSuccessful()
    exit(not test_result)
