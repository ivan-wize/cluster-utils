import unittest
from cluster_utils import reduce_clusters

class TestClusterUtils(unittest.TestCase):
    def test_standard_case(self):
        """
        Positive test case with overlapping and not overlapping
        """
        ctuples = [(0.5, 0.5, 0.5), (1.5, 1.5, 1.1), (0.7, 0.7, 0.4), (4, 4, 0.7)]
        expected = [(1.5, 1.5, 1.1), (4, 4, 0.7)]
        self.assertEqual(reduce_clusters(ctuples), expected)

    def test_edge_case_no_overlap(self):
        """
        Negative test case when no circles are overlapping
        """
        ctuples = [(0, 0, 1), (3, 0, 1), (0, 3, 1)]
        expected = [(0, 0, 1), (3, 0, 1), (0, 3, 1)]
        self.assertEqual(reduce_clusters(ctuples), expected)

    def test_edge_case_one_circle(self):
        """
        Test case with one circle only
        """
        ctuples = [(0, 0, 1)]
        expected = [(0, 0, 1)]
        self.assertEqual(reduce_clusters(ctuples), expected)

    def test_edge_case_empty_input(self):
        """
        Test case with no input
        """
        ctuples = []
        expected = []
        self.assertEqual(reduce_clusters(ctuples), expected)

if __name__ == '__main__':
    unittest.main()
