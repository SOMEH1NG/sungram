from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sungram",
    version="0.1",
    description="A lightweight and asynchronous Python library for building Telegram bots.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kunal Gaikwad",
    author_email="kunalgaikwad9322@gmail.com",
    packages=["sungram"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
