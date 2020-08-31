from proboscis import TestProgram
import unittest
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

test_loader = unittest.TestLoader()
test_loader.discover('./testcases/')

if __name__ == '__main__':
    TestProgram(testLoader=test_loader).run_and_exit()
