from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='savepoint',
    version=version,
    description="A context manager that creates savepoints",
    long_description="""
A context manager that creates savepoints, avoiding recalculating expensive
parts of the code. Useful if you're running a script several times while 
developing it.

An example:

.. code-block:: python

    from savepoint import SavePoint

    a = 10
    b = 20

    # do some expensive calculation here
    with SavePoint("stuff.p"):
        print "doing stuff"
        a += 10
        c = 30

    print a, b, c

.. code-block:: bash

    $ python script.py
    doing stuff
    20 20 30

    $ python script.py
    20 20 30

The first time the code is ran the ``with`` block is executed, and the modifed 
scope is pickled to ``stuff.p``. Subsequent runs will update the global scope
from the pickle file, and skip the block completely.

Note that only changes in the scope are stored, but not file modifications and
other side effects of the block.
    """,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='context manager savepoint hack',
    author='Roberto De Almeida, Marinexplore Inc.',
    author_email='rob@marinexplore.com',
    url='https://github.com/robertodealmeida/savepoint',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
    }
)
