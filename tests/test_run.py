# coding: spec

from pathlib import Path
import tempfile


describe "it can format":
    it "works", example_input, example_output, run_formatter:
        with tempfile.TemporaryDirectory() as working:
            test = Path(working) / "test.py"
            with open(test, "w") as fle:
                print(example_input, file=fle)

            run_formatter(Path(working))

            with open(test) as fle:
                assert fle.read() == example_output
