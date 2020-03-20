from setuptools import setup

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='there_is_no_spoon',
    author='Tiffany Souterre',
    version='1.0.12',
    install_requires=REQUIREMENTS,
    packages=['there_is_no_spoon'],
    description="An application to generate adversarial examples",
    entry_points={
        'console_scripts': ['there_is_no_spoon=there_is_no_spoon.main:main']
    }
)
