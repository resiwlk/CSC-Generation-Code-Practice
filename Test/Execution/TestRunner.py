import sys
import os
from pathlib import Path
sys.path.append(os.getcwd())
print(os.getcwd())
from unittest import TestLoader, TestSuite, TextTestRunner
from Test.TestScripts.test_Git_Search import test_Git_Search
 

if __name__ == "__main__":
 
    test_loader = TestLoader()
    
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(test_Git_Search),
        ))
 
    test_runner = TextTestRunner()
    test_runner.run(test_suite)
