# coding: utf-8


import unittest


def all_test(pattern=None):
    suites = unittest.defaultTestLoader.discover('tests', pattern=pattern)
    return suites


def suites_from_dir(discover_dir, pattern='test*.py'):
    """

    :param dir:
    :return:
    """
    suites = unittest.defaultTestLoader.discover(discover_dir, pattern=pattern)
    return suites


def main(pattern='test*.py', verbosity=2):
    suites = all_test(pattern)
    print("{} tests".format(suites.countTestCases()))
    unittest.TextTestRunner(verbosity=verbosity).run(suites)


if __name__ == "__main__":
    main()
