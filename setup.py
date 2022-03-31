from setuptools import setup, find_packages

setup(
    name="fedciv_lab_cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "civlab = fedciv_lab_cli:cli",
        ],
    },
)
