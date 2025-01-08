from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    test_suite='tests',
)