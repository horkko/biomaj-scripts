try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'name': 'biomaj-scripts',
    'version': '1.0.0',
    'packages': find_packages(),
    'scripts': ['scripts/bm_bank_sections.py'],
    'url': 'https://github.com/horkko/biomaj-scripts',
    'download_url': 'https://github.com/horkko/biomaj-scripts',
    'classifiers': [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],
    'install_requires': ['humanfriendly',
                         'rfeed'],
    'dependency_links': ['http://github.com/horkko/biomaj-manager/tarball/master#egg=biomajmanager-1.1.10'],
    'include_package_data': False,
    'author': 'Emmanuel Quevillon',
    'author_email': 'tuco@pasteur.fr,horkko@gmail.com',
    'description': 'BioMAJ3 contribution scripts'
}

setup(**config)
