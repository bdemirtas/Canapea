"""Packaging logic for CouchEngine."""

import versioneer  # noqa
from setuptools import setup, find_packages  # noqa

DESCRIPTION = (
    'Canapea is a Python Object-Document '
    'Mapper for working with Cloudant'
)

try:
    with open('README.rst') as fin:
        LONG_DESCRIPTION = fin.read()
except Exception:
    LONG_DESCRIPTION = None

CLASSIFIERS = [
    'Development Status :: 1 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

extra_opts = {
    'packages': find_packages(exclude=['tests', 'tests.*']),
    'tests_require': ['pytest']
}

setup(
    name='canapea-database',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    author='Burak Demirtas',
    author_email='burak.demirtas@protonmail.com',
    maintainer='Burak Demirtas',
    maintainer_email='burak.demirtas@protonmail.com',
    url='https://burak.demirtas.github.io',
    install_requires=[
        'cloudant>=2.0.0',
        'bson>=0.5.0'
    ],
    **extra_opts
)
