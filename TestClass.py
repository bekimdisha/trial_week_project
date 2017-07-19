from TestSuite import ClassToTest
import logging
import sys
sys.stdout.flush()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class TestsClass():
	logger = logging.getLogger(__name__)
    # Simple test suite for a simple function
    def test_func_with1(self):
    	actual = ClassToTest().func(1)
        try: 
        	assert actual == 2
        	logger.info('test_func_with1 PASSED')
        except:
        	logger.info('test_func_with1 FALED')

    def test_func_with_2(self):
    	actual = ClassToTest().func(2)
        try:
        	assert actual == 3
        	logger.info('test_func_with2 PASSED')
        except:
        	logger.info('test_func_with2 FALED')

    def test_func_with_3(self):
    	actual = ClassToTest().func(3)
        try:
        	assert actual == 4
        	logger.info('test_func_with3 PASSED')
        except:
        	logger.info('test_func_with3 FALED')

    def test_func_with_4(self):
    	actual = ClassToTest().func(4)
        try:
        	assert actual == 5
        	logger.info('test_func_with4 PASSED')
        except:
        	logger.info('test_func_with4 FALED')

    def test_func_with_5(self):
    	actual = ClassToTest().func(5)
        try:
        	assert actual == 6
        	logger.info('test_func_with5 PASSED')
        except:
        	logger.info('test_func_with5 FALED')

    def test_func_with_6(self):
    	actual = ClassToTest().func(6)
        try:
        	assert actual == 7
        	logger.info('test_func_with6 PASSED')
        except:
        	logger.info('test_func_with6 FALED')

    def test_func_with_7(self):
    	actual = ClassToTest().func(7)
        try:
        	assert actual == 8
        	logger.info('test_func_with7 PASSED')
        except:
        	logger.info('test_func_with7 FALED')

    def test_func_with_8(self):
    	actual = ClassToTest().func(8)
        try:
        	assert actual == 9
        	logger.info('test_func_with8 PASSED')
        except:
        	logger.info('test_func_with8 FALED')

    def test_func_with_9(self):
    	actual = ClassToTest().func(9)
        try:
        	assert actual == 10
        	logger.info('test_func_with9 PASSED')
        except:
        	logger.info('test_func_with9 FALED')

    def test_func_with_11(self):
    	actual = ClassToTest().func(11)
        try:
        	assert actual == 11
        	logger.info('test_func_with11 PASSED')
        except:
        	logger.info('test_func_with11 FAILED')