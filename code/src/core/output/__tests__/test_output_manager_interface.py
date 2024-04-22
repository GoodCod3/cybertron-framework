import unittest
from unittest.mock import Mock, MagicMock

from core.output.output_manager_interface import IOutputManager


class TestOutputManager(unittest.TestCase):
    def setUp(self):
        self.manager = IOutputManager()

    def test_fail_get_id(self):
        with self.assertRaises(NotImplementedError):
            self.manager.get_id()

    def test_fail_set_mapper(self):
        mapper_manager_mock = Mock()
        with self.assertRaises(NotImplementedError):
            self.manager.set_mapper(mapper_manager_mock)

    def test_fail_put(self):
        data = {}
        with self.assertRaises(NotImplementedError):
            self.manager.put(data)

    def test_success_put(self):
        data = {}
        output_mock = MagicMock(spec=IOutputManager)
        output_mock.get_id.return_value = "1"
        output_mock.set_mapper.return_value = {}
        output_mock.put.return_value = {"a": 1}

        result_id = output_mock.get_id(data)
        result_mapper = output_mock.set_mapper(data)
        result_put = output_mock.put(data)

        self.assertEqual(result_id, "1")
        self.assertEqual(result_mapper, {})
        self.assertEqual(result_put, {"a": 1})
