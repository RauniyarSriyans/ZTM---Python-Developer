import unittest

# let's say this is a function that we want to test
def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err

# we can use unittest to write a bunch of functions or unit tests to test any function

class TestDoStuff(unittest.TestCase):
    # this is a special function that is run before any of the following functions. It sets up if anything is required for testing.
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = 'shkshs'
        result = do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    
    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    
    # this is also a special function that helps do something after each test is successfully conducted. Can be handy when
    # databases are involved here. You can clear the database after every test to save resources. 
    def tearDown(self):
        print('testing done')

# this just means run all the tests
if __name__ == '__main__':
    unittest.main()
