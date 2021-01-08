import ast
import io
import re

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r"description\s+=\s+(?P<description>.*)")

with open("nursery_mock.py", "rb") as f:
    description = str(
        ast.literal_eval(_description_re.search(f.read().decode("utf-8")).group(1))
    )

setup(
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    description=description,
    install_requires=["Nursery"],
    keywords="nursery plugin mock",
    license="BSD-3-Clause",
    long_description=readme,
    long_description_content_type="text/markdown",
    name="nursery-mock",
    py_modules=["nursery_mock"],
    url="https://github.com/terminal-labs/nursery-mock",
    version="0.0.1",
    classifiers=[
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "nursery.plugins": ["nursery-mock = nursery_mock:MockTarget"]
    },
)
