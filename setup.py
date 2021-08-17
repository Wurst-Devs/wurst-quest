from setuptools import find_packages, setup

setup(
    author="Würst Devs",
    author_email="wurst.devs@gmail.com",
    name="wurst-quest",
    long_description="Würst Quest: The würst auto-rpg ever made.",
    version="0.1-dev",
    url="https://github.com/Wurst-Devs/wurst-quest.git",
    packages=find_packages(),
    entry_points={"console_scripts": ["wurst-quest = src.__main__:main"]},
    package_dir={"quest": "src"},
    install_requires=[],  # TODO check pq-cli
    classifiers=[],  # TODO
)
