"""
CLI Command Extensions for Flask
"""
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from click.testing import CliRunner


class TestFlaskCLI(TestCase):
    """Test Flask CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()

    def test_db_create(self):
        """It should call the db-create command"""
        fake_db = MagicMock()

        with patch.dict(os.environ, {"FLASK_APP": "service:app"}, clear=True):
            import importlib
            cli_commands = importlib.import_module('service.common.cli_commands')

            cli_commands.db = fake_db

            result = self.runner.invoke(cli_commands.db_create)
            self.assertEqual(result.exit_code, 0)
