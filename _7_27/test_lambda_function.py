# test_lambda_function.py
import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_handler(self):
        # Given: a fake event and context
        event = {
            'key1': 'Hello',
            'key2': 'World',
            'key3': '!'
        }
        context = None  # We don't need context for this test

        # When
        result = lambda_handler(event, context)

        # Then
        self.assertEqual(result, 'Hello')

if __name__ == '__main__':
    unittest.main()
