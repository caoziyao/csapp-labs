# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/2 
@desc:
pip3 install json-rpc
python3 -m unittest tests/test_case/test_demo.py
python3 -m unittest discover <test_directory>
python3 -m unittest discover -s <directory> -p '*_test.py'
python3 testmain.py xxxx
"""
import sys
import os

import unittest
from tests.test_case.demo.test_demo import TestDemoCase
from tests.common.constant import EnumVerbosity


def add_tests():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemoCase))
    return suite


def start_dir_from_arv():
    """"""
    argv = sys.argv
    l = len(argv)

    if l >= 2:
        dirs = argv[1:]
        start = os.path.join('tests', 'test_case', *dirs)
    else:
        start = os.path.join('tests', 'test_case')

    print('start_dir', os.path.abspath(start))
    return start


def main():
    # main
    start_dir = start_dir_from_arv()
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern='test_*.py')

    path_report = os.path.join('tests', 'UnittestTextReport.txt')
    with open(path_report, 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=EnumVerbosity.detail.value)
        runner.run(suite)


if __name__ == '__main__':
    main()
