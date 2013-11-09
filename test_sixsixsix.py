from __future__ import division, print_function, unicode_literals
from sixsixsix import *


import pytest
import sys


def test_print():
    assert print('hi') is None


def test_division():
    assert (666 + 1) / 2 == 333.5


def test_reduce():
    with pytest.raises(Exception):
        reduce(lambda x, y: x + y, range(666), 0)
    import functools
    assert functools.reduce(lambda x, y: x + y, range(666), 0) == 221445


def test_zip():
    x = zip(range(666), range(666))
    assert not isinstance(x, list)


def test_xrange():
    with pytest.raises(Exception):
        xrange(666)


def test_range():
    assert not isinstance(range(666), list)


def test_intern():
    with pytest.raises(Exception):
        intern(str('hi'))
    import sys
    sys.intern(str('hi'))


def test_unichr():
    with pytest.raises(Exception):
        unichr(666)
    chr(666)


def test_basestring():
    # TODO: unfixable?
    pass


def test_long():
    with pytest.raises(Exception):
        long(666)
    assert 666 == int(666)


def test_map():
    assert not isinstance(map(str, range(666)), list)


def test_filter():
    is_even = lambda x: x % 2 == 0
    assert not isinstance(filter(is_even, range(666)), list)


def test_filterfalse():
    is_even = lambda x: x % 2 == 0
    import itertools
    assert not isinstance(itertools.filterfalse(is_even, range(666)), list)


def test_reload():
    with pytest.raises(Exception):
        reload(sys)
    import imp
    imp.reload(sys)


def test_ascii():
    ascii('666') == '666'
    repr('666') == '666'


def test_apply():
    with pytest.raises(Exception):
        def f(*args):
            return '666'
        apply(f, 'y')


def test_cmp():
    with pytest.raises(Exception):
        cmp(666, 666)


def test_coerce():
    with pytest.raises(Exception):
        coerce(666, 666.0)


def test_execfile():
    with pytest.raises(Exception):
        execfile('/dev/null')


def test_input():
    with pytest.raises(Exception):
        raw_input()
    input


def test_next():
    x = range(666)
    i = iter(x)
    assert next(i) == 0
    assert next(i) == 1


def test_round():
    assert round(666.666) == 667
    assert round(1.5) == 2

    assert isinstance(round(1.5), int)

    assert round(2.5) == 2
    assert round(10.0/3, 0) == 3.0

    assert round(-1.5) == -2
    assert round(-2.5) == -2
    assert round(-10.0/3, 0) == -3.0

    assert round(.666666, 3) == .667


def test_sorted():
    with pytest.raises(Exception):
        sorted(reversed(range(666)), cmp=lambda x, y: 0)

    assert sorted(reversed(range(666)), key=lambda x: x) == list(range(666))
