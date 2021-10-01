class WhimsicalChecker(object):
    def __init__(self, A):
        """Initialize the WhimsicalChecker

        ARGS
        --------
        A: list(int)
            A set of numbers defining whimsical numbers

        RETURNS
        --------
        nothing
        """
        # write your preprocessing here
        pass

    def is_whimsical(self, l):
        """Check if l is a whimsical number

        ARGS
        --------
        l: int
            number to check

        RETURNS
        --------
        True if l is a whimsical number, False otherwise
        """
        # modify this function to return true
        # if and only if l can be expressed as
        # a sum of numbers from A
        return l == 0


# you may find the tests provided below helpful.
def test():
    solver = WhimsicalChecker([5, 8, 11])
    assert solver.is_whimsical(0)
    assert solver.is_whimsical(16)
    assert not solver.is_whimsical(17)
    assert solver.is_whimsical(18)
    print "Great success!"

def test2():
    solver = WhimsicalChecker([1])
    for i in range(10000):
        assert solver.is_whimsical(i)
    print "Great success!"

if __name__ == '__main__':
    test()
    test2()
