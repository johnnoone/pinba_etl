from setuptools import setup, find_packages

setup(
    name='pinba_etl',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'jinja2',
        'pyaml'
    ]
)
