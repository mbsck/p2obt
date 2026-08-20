from pathlib import Path

from p2obt import automate


def test_create_ob(tmp_dir: Path) -> None:
    """Tests the automate.remove_parenthesis function."""
    automate.create_ob("HD 142527", "sci", "UTs", mode="gr", output_dir=tmp_dir)
    automate.create_ob(
        "HD 100920",
        "cal",
        "UTs",
        sci_name="HD 142527",
        tag="L",
        mode="gr",
        output_dir=tmp_dir,
    )
