from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='wqsat_sr',
    packages=find_packages(),
    version='0.1.0',
    description='Code to improve the spatial resolution of satellite images.',
    author='CSIC',
    license='Apache License 2.0',
    install_requires=reqs)
