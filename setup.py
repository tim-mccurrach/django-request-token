import os
from setuptools import setup, find_packages

import request_token

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-request-token",
    version=request_token.__version__,
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "Django>=2.0",
        "PyJWT>=1.4",
        "sqlparse>=0.2",
        "psycopg2-binary>=2.7",
    ],
    include_package_data=True,
    description="JWT-backed Django app for managing querystring tokens.",
    license="MIT",
    long_description=README,
    url="https://github.com/yunojuno/django-request-token",
    author="YunoJuno",
    author_email="code@yunojuno.com",
    maintainer="YunoJuno",
    maintainer_email="code@yunojuno.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
