from os import path
from setuptools import setup


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


setup(
    name='openai-gym-showcase',
    version='0.1',
    author="Danny Lade",
    author_email="dannylade@gmail.com",
    description=("Some showcases for 'OpenAI Gym' based on Python 3.5."),
    license="LGPL",
    keywords="openai gym showcase example",
    url="https://github.com/iteratec/openai-gym-showcase",
    location="https://github.com/iteratec/openai-gym-showcase",
    long_description=read('README.md'),

    install_requires=[
        'python_version>="3.5"',
        'gym[all]>=0.10.8',
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Games/Entertainment :: Simulation",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
)
