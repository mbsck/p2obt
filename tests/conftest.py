from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def tmp_dir(tmp_path_factory) -> Path:
    return tmp_path_factory.mktemp("data")
