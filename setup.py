from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="microutils",
    version="0.1.1",
    description="Simple utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    install_requires=["requests"],
    python_requires=">=3.10",
)