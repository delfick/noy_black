# coding: spec

import typing as tp


describe "it can format":
    async it "works", example_input, example_output, run_formatter:
        pass

    it "works2", example_input: str,  run_formatter:   bool:
        pass

    it "works3", example_input: str, example_output:tp.Optional[list[str]], run_formatter:   bool:
        pass

it "asdfasdfasdf", a:  str:
    pass

ignore "asdfasdfasdf2":
    pass

async it "asdfasdfasdf3":
    (

            1,

        )
    pass

describe  "things" :
    it  "works" :
        def wat(  ):
            return   True
        assert   wat()

    async it "does",   a: str, b:  int:
        one = 2
        assert (one
                ==   2)



describe "with_setup":
    async before_each:

        assert 1 ==   1

    async after_each:

        assert 43        - 2 == 41

describe "with_setup not async":
    before_each:

        assert 1 ==   1

    after_each:

        assert 43        - 2 == 41
