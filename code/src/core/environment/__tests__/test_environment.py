import unittest

from core.environment.environment import Environment


class TestEnvironmentManager(unittest.TestCase):
    def setUp(self):
        self.environment = Environment()

    def test_set_environment_variables(self):
        environment_variables = {"VAR1": "value1", "VAR2": "value2"}
        self.environment.set_environment_variables(environment_variables)

        self.assertEqual(
            self.environment.environment_variables,
            environment_variables,
        )
