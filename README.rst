sixsixsix
=========


The idea is to put these two lines at the start of all of your python files,
to force you to write forward compatible python 2/3 code::

    from __future__ import division, print_function, unicode_literals
    from sixsixsix import *

When using python 3, this does nothing, and when the day comes when python 2
support is no longer needed, you can simply remove these 2 lines at the top
of each file.

* map, range, zip, etc all are the iterable versions.
* obsolete builtins like xrange, long, raw_input are removed.
* ...
