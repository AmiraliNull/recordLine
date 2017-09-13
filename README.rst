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

