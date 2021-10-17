#!/usr/bin/python3

from pathlib import Path
from click.testing import CliRunner

import os
import pytest


@pytest.fixture(scope="module")
def project_path():
    original_path = os.getcwd()
    os.chdir(original_path + "/tests")
    yield Path(original_path + "/tests")
    os.chdir(original_path)


@pytest.fixture(scope="module")
def cli_tester():
    return CliRunner()
