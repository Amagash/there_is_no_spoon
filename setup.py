from setuptools import setup

setup(
    name='there_is_no_spoon',
    author='Tiffany Souterre',
    version='1.0.8',
    packages=['there_is_no_spoon'],
    description="An application to generate adversarial examples",
    entry_points={
        'console_scripts': ['there_is_no_spoon=there_is_no_spoon.main:main']
    }
)
