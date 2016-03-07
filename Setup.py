try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PyLambda 2',
    'author': 'Manuel Guerrero',
    'url': 'http://sfdc.ninja',
    'download_url': 'http://sfdc.ninja/pylambda2',
    'author_email': 'amguerrero@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lambda1'],
    'scripts': [],
    'name': 'py_lambda2'
}

setup(**config)