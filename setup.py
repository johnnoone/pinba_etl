from setuptools import setup, find_packages

setup(
    name='pinba-etl',
    version='0.2',
    description='Pinba Utilities',
    author='Xavier Barbosa',
    author_email='clint.northwood@gmail.com',
    packages=find_packages(),
    install_requires=[
        'jinja2',
        'pyaml'
    ],
    # trying to add files...
    include_package_data = True,
    package_data = {
        '': ['*.yml', '*.j2'],
        'templates': ['*.yml', '*.j2'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: System :: Clustering',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
    ],
)
