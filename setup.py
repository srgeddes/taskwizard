from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="taskit",
    author="Riley Geddes",
    version="1.0.0",
    description="A CLI task management system",
    url="https://github.com/srgeddes/task-it.git",
    install_requires=["click"],
    long_description=long_description,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12.4",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "taskit=app:start_app",
        ],
    },
)
