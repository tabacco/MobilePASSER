from setuptools import setup, find_packages

setup(
    name='MobilePASSER',
    version='1.0',
    description='A reimplementation of the MobilePASS client in Python.',
    packages=find_packages(),
    install_requires=[
        "bitstring~=3.1.4",
        "six"
    ],
    entry_points={
        'console_scripts': ['mobilepasser = mobilepasser.mobilepasser:main',]
    },
)
