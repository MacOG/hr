hr
==

CLI for adding/updating user accounts on linux servers

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``https://github.com/MacOG/hr.git``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in json file of users

Example:

::
 
    $ hr /path/to/inventory.json

Example with --export:

::

    $ hr --export /path/to/inventory.json

Running Tests
-------------

Run test locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv is not active then use:

::

    $pipenv run make
