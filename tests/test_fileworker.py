import unittest
from src.fileworker import JSONWorker
import os


class TestJSONWorker(unittest.TestCase):

    def test_path_attribute(self):
        file_name = "test_vacancies.json"
        expected_path = os.path.join('data', file_name)
        json_worker = JSONWorker(file_name)
        self.assertEqual(json_worker.path, expected_path)


if __name__ == '__main__':
    unittest.main()
