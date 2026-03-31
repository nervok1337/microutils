from setuptools import setup, find_packages

setup(
    name="microutils",
    version="0.1.0",
    description="Simple utility functions",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests"],
    python_requires=">=3.10",
)