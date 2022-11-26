from setuptools import setup, find_packages

setup(
    name="lightgbmlss",
    version="0.1.0",
    description="LightGBMLSS - An extension of LightGBM to probabilistic forecasting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexander März",
    author_email="alex.maerz@gmx.net",
    url="https://github.com/StatMixedML/LightGBMLSS",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    package_data={'': ['datasets/*.csv']},
    zip_safe=True,
    python_requires=">=3.7",
    install_requires=[
    ],
    test_suite="tests",
    tests_require=["flake8", "pytest"],
)
