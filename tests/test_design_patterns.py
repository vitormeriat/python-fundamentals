import unittest
import src.desing_patterns as ds


class TestDecorator(unittest.TestCase):

    def test_success_single_try(self):
        @ds.Decorator.make_blink
        def hello_world():
            """Original function!"""

            return "Hello, World!"

        self.assertEqual(hello_world(), "<blink>Hello, World!</blink>")
        self.assertEqual(hello_world.__doc__, "Original function!")
        self.assertEqual(hello_world.__name__, "hello_world")


class TestTries(unittest.TestCase):
    def setUp(self):
        self.count = 0

    def test_success_single_try(self):
        @ds.MyTry.tries(1)
        def a():
            self.count += 1
            return "expected_result"
        self.assertEqual(a(), "expected_result")
        self.assertEqual(self.count, 1)

    def test_success_two_tries(self):
        @ds.MyTry.tries(2)
        def a():
            self.count += 1
            return "expected_result"
        self.assertEqual(a(), "expected_result")
        self.assertEqual(self.count, 1)

    def test_failure_two_tries(self):
        @ds.MyTry.tries(2)
        def a():
            self.count += 1
            raise Exception()
        try:
            a()
            self.fail()
        except ds.MaxTriesExceededError:
            self.assertEqual(self.count, 2)

    def test_success_after_third_try(self):
        @ds.MyTry.tries(5)
        def a():
            self.count += 1
            if self.count == 3:
                return "expected_result"
            else:
                raise Exception()
        self.assertEqual(a(), "expected_result")
        self.assertEqual(self.count, 3)
