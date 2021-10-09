from setuptools import setup, find_packages

VERSION = '0.1.1' 
DESCRIPTION = 'Creates a folder with the same name and location as the calling file and returns the path to that folder'
LONG_DESCRIPTION = ''

setup(
        name="simple_export_dir", 
        version=VERSION,
        author="Christian Casadio",
        author_email="<casadiochristian@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)