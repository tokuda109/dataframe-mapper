DataFrame Mapper
================

**THIS IS EXPERIMENTAL**.

Requirements
------------

- Python 3.5+
- Pandas 0.20.0+

Installation
------------

Install DataFrame Mapper via pip::

    $ pip install dataframe-mapper

Example
-------

Simple DataFrame Mapper example::

    from dfmapper import DataFrameMapper, IntColumn, StrColumn

    class UserDfm(DataFrameMapper):

        id = IntColumn(min=1, nullable=False)
        username = StrColumn(max_length=30, nullable=False)
        profile = StrColumn()

        def find_by_id(self, id):
            return self.df[self.df.id == id]

    user_dfm = UserDfm({
        "id": [1, 2, 3],
        "username": ["Bessie Bennett", "Sandra Matthews", "Jessie Bates"],
        "profile": ["BLAH BLAH BLAH", "PITH PITH PITH", None]
    })

    user_dfm.is_valid()
    #: True

    user_dfm.find_by_id(1)
    #:    id username       profile
    #: 0  1  Bessie Bennett BLAH BLAH BLAH

License
-------

DataFrame Mapper is licensed under MIT License. See `LICENSE <https://github.com/tokuda109/dataframe-mapper/blob/master/LICENSE>`_ for more information.
