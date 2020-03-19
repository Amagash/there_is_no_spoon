from pkg_resources import parse_requirements
from setuptools import setup

requirements = parse_requirements('requirements.txt')

setup(
    name='there_is_no_spoon',
    author='Tiffany Souterre',
    version='1.0.12',
    install_requires=requirements,
    packages=['there_is_no_spoon'],
    description="An application to generate adversarial examples",
    entry_points={
        'console_scripts': ['there_is_no_spoon=there_is_no_spoon.main:main']
    }
)
