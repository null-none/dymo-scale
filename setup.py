from setuptools import setup, find_packages

setup(
    name='python-dymo-scale',
    version='0.0.2',
    packages=find_packages(),
    author='Dmitry Kalinin',
    author_email='kalinin.mitko@gmail.com',
    install_requires=[
        'pyusb',
    ],
    url='https://github.com/null-none/python-dymo-scale',
)
