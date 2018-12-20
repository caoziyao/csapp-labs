# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/11/30 
@desc:
"""

import os

import coverage
import unittest

from tests.test_case.parse.test_parse import TestParse
from tests.test_case.test_points import TestPoints
from tests.test_case.graphics.test_graphics import TestGraphics
from tests.test_case.test_keywords import TestKeywords

# test_cases = (TestParse, TestPoints)
test_cases = ( TestKeywords, )

def get_covdir():
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    return covdir


def load_tests(loader, standard_tests, pattern):
    """
    discover
    :param loader:
    :param standard_tests:
    :param pattern:
    :return:
    """
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests


def load_test_cases(loader, tests, pattern):
    """
    Case
    :param loader:
    :param tests:
    :param pattern:
    :return:
    """
    suite = unittest.TestSuite()

    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


def run_test():
    loader = unittest.TestLoader()

    suite = load_test_cases(loader, None, None)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def cov_start():
    cov = coverage.coverage(branch=True, include=['vm/*', 'zvm/*'])
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
