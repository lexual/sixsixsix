# * http://docs.pythonsprints.com/python3_porting/py-porting.html#reorganization
# * http://sayspy.blogspot.com.au/2010/08/what-will-forever-be-exclusive-to.html
# * http://python3porting.com/differences.html
import sys


if sys.version_info.major == 3:
    pass
elif sys.version_info.major == 2:
    range = xrange
    sys.intern = intern
    chr = unichr
    int = long
    input = raw_input

    def next(iterator):
        return iterator.next()

    _round = round

    def round(number, ndigits=0):
        """
        Python 2 rounds halfway cases away from zero.
        Python 3 rounds towards nearest even. if ndigits is zero, return int.
        """
        is_halfway = number % 1 == 0.5
        if is_halfway:
            modulo_is_even = (number - 0.5) % 2 == 0
            if modulo_is_even:
                result = number - 0.5
            else:
                result = number + 0.5
        else:
            result = _round(number, ndigits)
        if ndigits == 0:
            result = int(result)
        return result

    _sorted = sorted

    def sorted(iterable, key=None, reverse=False):
        """
        Python 3 doesn't have cmp argument.
        """
        return _sorted(iterable, key=key, reverse=reverse)

    import itertools
    itertools.filterfalse = itertools.ifilterfalse

    from future_builtins import ascii
    from future_builtins import filter
    #from future_builtins import hex
    from future_builtins import map
    #from future_builtins import oct
    from future_builtins import zip

    def _remove_old_builtins():

        def _blowup_builder(old_builtin):
            def blowup(*args, **kwargs):
                raise Exception('using python2 only builtin: ' + old_builtin)
            return blowup

        _old_builtins = (
            'apply',
            'cmp',
            'coerce',
            'execfile',
            'intern',
            'long',
            'raw_input',
            'reduce',
            'reload',
            'unichr',
            'xrange',
        )
        _old_builtin_stub = _blowup_builder
        for old_builtin in _old_builtins:
            globals()[old_builtin] = _old_builtin_stub(old_builtin)

    _remove_old_builtins()
