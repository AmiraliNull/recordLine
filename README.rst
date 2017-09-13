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


install recordLine

``````````````````

::

	$ git clone https://gitlab.com/amiralinull/recordLine.git

	$ cd recordLine

	$ sudo python setup.py install
