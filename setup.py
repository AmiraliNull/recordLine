"""
RecordLine
--------

RecordLine is a line data recorder!

RecordLine is Fun
```````````````

::

    >>> import recordLine as rl

    >>> db = rl.load('test.db')

    >>> db.new('somthing data')
	True

    >>> db.show()
    [...,
    ...,
    ...,
    'somthing data']


And Easy to Install
```````````````````

::

    $ pip install recordLine

Links
`````

* `project repo <https://github.com/amiralinull/recordLine/>`_

"""

from distutils.core import setup

setup(name = "recordLine",
    version="0.0.1",
    description="simple line data recorder",
    author="Amirali Esfandiari",
    author_email="incoming+amiralinull/dds@gitlab.com",
    license="GPLv2+",
    url="https://amiralinull.github.io/recordLine/",
    long_description=__doc__,
    classifiers = [
        "Programming Language :: Python",
        "License :: GnuGPLv2+",
        "Intended Audience :: Developers",
        "Topic :: Line data Recorder" ],
    py_modules=['recordLine'],
    install_requires=[])
