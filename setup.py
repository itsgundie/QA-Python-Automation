"""Setup file for project"""

from setuptools import setup, find_packages

setup(
    name='phonebook',
    version='0.0.1',
    description='Manager for collection of phone numbers',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['phonebook=phonebook.cli:main'],
    },

    # metadata
    author='Gundie',
    author_email='itsgundie@gmail.com',
    license='None',
    install_requires=['pytest']
)
