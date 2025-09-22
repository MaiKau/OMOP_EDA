from setuptools import setup, find_packages

setup(
    name="OMOP",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "scipy",
    ],
    description="OMOP Clinical Analysis Package",
    author="Your Name",
)
