from setuptools import setup, find_packages

setup(
    name='basket_compare_playground',
    version='0.1.0',
    url='https://github.com/jackverone/basket-compare-playground',
    author='Jacek Services',
    author_email='jacek.services@gmail.com',
    description='App enables basket comparison for selected products.',
    packages=find_packages(),
    install_requires=['requests'],
)
