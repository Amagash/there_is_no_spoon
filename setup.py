from setuptools import setup

setup(
    name='there_is_no_spoon',
    author='Tiffany Souterre',
    version='1.0.3',
    packages=['there_is_no_spoon'],
    package_data={'there_is_no_spoon': ['imagenet_class_index.json']},
    include_package_data=True,
    description="An application to generate adversarial examples",
    entry_points={
        'console_scripts': ['there_is_no_spoon=there_is_no_spoon.main:main']
    }
)
