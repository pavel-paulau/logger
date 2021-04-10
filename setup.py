from setuptools import setup

setup(
    name='logger',
    version='1.5',
    description='Python logging helper',
    author='Pavel Paulau',
    author_email='pavel.paulau@gmail.com',
    license='Apache License 2.0',
    packages=['logger'],
    package_data={'logger': ['logging.conf']},
)
