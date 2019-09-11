# Thanks https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
import unittest
import os

loader = unittest.TestLoader()
# get to source directory. We're in minesweeper/tests
start_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
suite = loader.discover(start_dir)
runner = unittest.TextTestRunner()
runner.run(suite)
