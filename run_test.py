# coding: utf-8

import os

import coverage
import unittest


def get_covdir():
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    return covdir


def load_tests(loader, standard_tests, pattern):
    """
    """
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests


def tests_from_case(loader, tests, pattern):
    """
    :return:
    """
    from tests import test_cases
    suite = unittest.TestSuite()

    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


def test_from_module(loader, pattern=None):
    """
    :return:
    """
    from tests.test_case import demo
    from tests.test_case import graphics
    suite = unittest.TestSuite()

    tests = loader.loadTestsFromModule(demo)
    suite.addTests(tests)
    return suite


def tests_from_dir(loader):
    """
    :return:
    """
    start_dir = os.path.join('tests')
    package_tests = loader.discover(start_dir=start_dir)
    return package_tests


def run_test():
    loader = unittest.TestLoader()

    suite = tests_from_dir(loader)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def cov_start():
    cov = coverage.coverage(branch=True, include=['compiler/*', 'vm/*'])
    cov.start()
    return cov


def cov_end(cov):
    cov.stop()
    cov.save()
    cov.report()
    covdir = get_covdir()
    cov.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    cov.erase()


def main():
    # cov = cov_start()
    run_test()
    # cov_end(cov)


if __name__ == '__main__':
    main()
