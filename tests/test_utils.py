import random

import pytest

from p2obt.backend import utils

NUMBER: int = random.randint(100000, 199999)


@pytest.mark.skip(reason="Test not yet implemented.")
def test_replace_elements() -> None:
    """Tests the backend.utils.replace_elements function."""


@pytest.mark.parametrize("input_str", [f"HD{' ' * i}{NUMBER}" for i in range(2)])
def test_add_space(input_str: str) -> None:
    """Tests the backend.utils.add_space function."""
    assert utils.add_space(input_str) == f"HD {NUMBER}"


@pytest.mark.parametrize("input_str", [f"HD{' ' * i}{NUMBER}" for i in range(1, 5)])
def test_remove_spaces(input_str: str) -> None:
    """Tests the backend.utils.remove_spaces function."""
    assert utils.remove_spaces(input_str) == f"HD {NUMBER}"


@pytest.mark.parametrize(
    "input_str", [f"{l}HD {NUMBER}{r}" for l, r in [("(", ")"), ("[", "]"), ("{", "}")]]
)
def test_remove_parenthesis(input_str: str) -> None:
    """Tests the backend.utils.remove_parenthesis function."""
    assert utils.remove_parenthesis(input_str) == f"HD {NUMBER}"


def test_contains_element() -> None:
    """Tests the backend.utils.contains_element function."""


@pytest.mark.skip(reason="Test not yet implemented.")
def test_convert_proper_motions() -> None:
    """Tests the backend.utils.convert_proper_motions function."""
