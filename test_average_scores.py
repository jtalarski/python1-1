import unittest
from first import average_scores


class MyTestCase(unittest.TestCase):

    def test_average(self):
        self.scores_dict = {'Test1': 31, 'Test2': 34, "Test3": 54}
        expected = 39.66666666
        actual = average_scores(self.scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        self.scores_dict = {'Test1': 31, 'Test2': 34,
                            "Test3": 54, "Test4": 30, 'Test5': 30}
        expected = 35.8
        actual = average_scores(self.scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_average_zero(self):
        self.scores_dict = {}
        with self.assertRaises(ValueError):
            average_scores(self.scores_dict)

if __name__ == '__main__':
    unittest.main()