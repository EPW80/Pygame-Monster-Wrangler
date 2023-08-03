""" Simple setup.py """

from setuptools import setup

setup_info = {
    "name": "videogame",
    "version": "0.1",
    "description": "A package to support writing games with PyGame",
    "long_description": open("README.md").read(),
    "author": "Erik Williams",
    "author_email": "erikparrawilliams@tutanota.com",
    "url": "https://github.com/EPW80/Pygame-Monster-Wrangler",
}

setup(**setup_info)
