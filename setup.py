#!/usr/bin/env python
from setuptools import setup, find_packages
setup (
    name='lovely.stemmer',
    version='0.0.1a1',
    author = "Lovely Systems",
    author_email = "office@lovelysystems.com",
    license = "BSD",
    keywords = "lovely stemmer german snowball porter",
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['lovely'],
    install_requires = ['setuptools',
                        ],
    zip_safe = True,
    entry_points = {
        'console_scripts':['porter_german=lovely.stemmer.german:main',
                           ],
        },
    )
