sixsixsix
=========


The idea is to put these two lines at the start of all of your python files,
to force you to write forward compatible python 2/3 code::

    from __future__ import division, print_function, unicode_literals
    from sixsixsix import *

When using python 3, this does nothing, and when the day comes when python 2
support is no longer needed, you can simply remove these 2 lines at the top
of each file.

* makes map, range, zip, etc, all are the iterable versions.
* maps raw_input to input.
* obsolete builtins like xrange, long, raw_input are removed (well, overriden
  so they raise an exception.)
* ...

e.g. in python 2::


    In [1]: isinstance(range(3), list)
    Out[1]: True

    In [2]: list(xrange(3))
    Out[2]: [0, 1, 2]

    In [3]: from sixsixsix import *

    In [4]: isinstance(range(3), list)
    Out[4]: False

    In [5]: list(xrange(3))
    Exception: using python2 only builtin: xrange

Useful for:

* Writing Python 2.7 code like python 3 (ish).
* Training muscle memory to write python 3 code, and avoid obsolete python 
  2-isms.
  
six = three times two.

sixsixsix = 'six' * 3

It's also the number of the beast, hence be wary ;)

Check out the code and the test file for examples of what it's doing.

Using tox to test against 2.7 & 3.3
