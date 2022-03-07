from setuptools import setup, find_packages

setup(
    name='mypackage2',
    version='0.1'
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package'
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/JohnSite07/mypackages2.git',
    author='<Jean Luc>'
    author_email='<jeen.mb@gmail.com>'
)