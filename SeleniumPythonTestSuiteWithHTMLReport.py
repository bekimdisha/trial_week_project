import HTMLTestRunner
import os
import unittest
from PythonSeleniumTests import TestSignUpAndLogIn


def main():
    # get the directory path to output report file
    dir = os.getcwd()
 
    # get all tests from TestSignUpAndLogIn class
    login_page_test = unittest.TestLoader().loadTestsFromTestCase(TestSignUpAndLogIn)
 
    # create a test suite combining home_page_test
    test_suite = unittest.TestSuite([login_page_test])

    print dir
 
    # open the report file
    outfile = open(dir + "\SeleniumPythonTestReport.html", "w")

 
    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='UI Tests')
 
    # run the suite using HTMLTestRunner
    runner.run(test_suite)

if __name__ == '__main__':
    HTMLTestRunner.main()