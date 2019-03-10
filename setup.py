from os import path
from setuptools import setup, find_packages


def __readme__():
    return open(path.join(path.dirname(__file__), 'README.md')).read()


setup(
    name='openai-gym-showcase',
    version='0.1',
    author="Danny Lade",
    author_email="dannylade@gmail.com",
    description=("Some showcases for 'OpenAI Gym' based on Python 3.5."),
    license='GPLv3',
    keywords="openai gym showcase example",
    url="https://github.com/iteratec/openai-gym-showcase",
    long_description=__readme__(),
    long_description_content_type='text/markdown',

    install_requires=[
        'python_version>="3.5"',
        'gym[atari]>=0.12.0',
        'gym[box2d]>=0.12.0',
        'gym[classic_control]>=0.12.0',
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Games/Entertainment :: Simulation",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
