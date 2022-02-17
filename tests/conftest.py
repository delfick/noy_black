from pathlib import Path
import subprocess
import pytest
import sys

example_folder = Path(__file__).parent / "example"


@pytest.fixture(scope="session")
def example_input():
    with open(example_folder / "input.py") as fle:
        return fle.read()


@pytest.fixture(scope="session")
def example_output():
    with open(example_folder / "output.py") as fle:
        return fle.read()


@pytest.fixture()
def run_formatter():
    def run_formatter(directory):
        subprocess.run([str(Path(sys.executable).parent / "noy_black"), str(directory)], check=True)

    return run_formatter
