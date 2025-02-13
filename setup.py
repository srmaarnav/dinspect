from setuptools import setup, find_packages

setup(
    name="doinspect",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "docker"
    ],
    entry_points={
        "console_scripts": [
            "doinspect=doinspect.cli:main"
        ]
    },
    author="Arnav Sharma",
    author_email="mail@arnavsharma.com.np",
    description="A CLI tool to inspect running Docker containers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/srmaarnav/doinspect",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
