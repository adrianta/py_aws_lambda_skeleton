try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PyLambda Skeleton',
    'author': 'Manuel Guerrero',
    'url': '',
    'download_url': '',
    'author_email': 'amguerrero@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['lambda'],
    'scripts': [],
    'name': 'py_aws_lambda_skeleton'
}

setup(**config)