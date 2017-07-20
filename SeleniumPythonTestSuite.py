import unittest
from PythonSeleniumTests import TestSignUpAndLogIn
 
# get all tests from SearchText and HomePageTest class
signup_and_login = unittest.TestLoader().loadTestsFromTestCase(TestSignUpAndLogIn)

 
# create a test suite for signup_and_login tests 
test_suite = unittest.TestSuite([signup_and_login])
 
# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)