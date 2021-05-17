from setuptools import setup, find_packages

VERSION = '1.1.2'
DESCRIPTION = 'Converts a country code or country name into a flag emoji'
LONG_DESCRIPTION = 'A Python package that converts a country code or country name into a flag emoji.'

setup(
        name="flagmoji",
        version=VERSION,
        author="Steven Yu",
        author_email="stevenyuser@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        url = "https://github.com/stevenyuser/flagmoji",
        packages=find_packages(),
        install_requires=[],

        keywords=['python', 'flagmoji', "emoji flag converter"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
