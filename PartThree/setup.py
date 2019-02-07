from distutils.core import setup

with open('README')  as file:
    readme = file.read()

setup(
    name='vgbhfive_wargame',
    version='2.0.0',
    packages=['wargame'],
    url='https://testpypi.python.org/pypi/vgbhfive_wargame/',
    license='LICENSE.txt',
    description='my vgbhfive\'s WarGame',
    long_description=readme,
    author='vgbh',
    author_email='vgbhfive@foxmail.com'
)