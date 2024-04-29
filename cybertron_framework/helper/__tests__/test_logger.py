import unittest
from unittest.mock import patch

from cybertron_framework.helper.logger import Logger
from freezegun import freeze_time


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    @freeze_time("2022-1-1")
    def test_info_logs_correctly(self):
        expected_result = "[01/01/2022 00:00:00] INFO | Test message"

        self.assertEqual(self.logger.info("Test message"), expected_result)

    @freeze_time("2022-1-1 12:00:00")
    @patch("traceback.format_exc")
    def test_warning_logs_correctly(self, mock_format_exc):
        mock_format_exc.return_value = "Traceback Error test"
        expected_result = "[01/01/2022 12:00:00] WARNING | Test message | Traceback Error test"  # noqa: E501

        self.assertEqual(
            self.logger.warning("Test message", from_exception=True),
            expected_result,
        )

    @freeze_time("2022-1-1 12:00:00")
    @patch("traceback.format_exc")
    def test_error_logs_correctly(self, mock_format_exc):
        mock_format_exc.return_value = "Traceback Error test"
        expected_result = "[01/01/2022 12:00:00] ERROR | Test message | Traceback Error test"  # noqa: E501

        self.assertEqual(
            self.logger.error("Test message", from_exception=True),
            expected_result,
        )

    @freeze_time("2022-1-1 12:00:00")
    @patch("traceback.format_exc")
    def test_critical_logs_correctly(self, mock_format_exc):
        mock_format_exc.return_value = "Traceback Error test"
        expected_result = "[01/01/2022 12:00:00] CRITICAL | Test message | Traceback Error test"  # noqa: E501

        self.assertEqual(
            self.logger.critical("Test message", from_exception=True),
            expected_result,
        )
