import sys
import os
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='unsplash_get',
    version='0.1.0',
    keywords="unsplash scrape stock images",
    author="streanger",
    author_email="divisionexe@gmail.com",
    description="unsplash srape tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streanger/unsplash_get",
    packages=['unsplash_get',],
    license='MIT',
    install_requires=['requests', 'lxml', 'beautifulsoup4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
