import unittest
import doctest


def test_suite():
    s = doctest.DocFileSuite(
        '../../../README.rst',
        optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
        ),
    return unittest.TestSuite(s)
