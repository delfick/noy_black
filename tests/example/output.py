# coding: spec

it "asdfasdfasdf":
    pass

ignore "asdfasdfasdf2":
    pass

async it "asdfasdfasdf3":
    (1,)
    pass

describe "things":
    it "works":

        def wat():
            return True

        assert wat()

    async it "does", a:
        one = 2
        assert one == 2


describe "with_setup":
    async before_each:

        assert 1 == 1

    async after_each:

        assert 43 - 2 == 41

describe "with_setup not async":
    before_each:

        assert 1 == 1

    after_each:

        assert 43 - 2 == 41
