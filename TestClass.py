from TestSuite import ClassToTest

class TestsClass():
    
    def test_func_with4(self):
    	actual = ClassToTest().func(3)
        assert actual == 5

    def test_func_with_5(self):
    	actual = ClassToTest().func(4)
        assert actual == 5