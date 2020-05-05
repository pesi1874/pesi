import codecs
from setuptools import setup, find_packages

with codecs.open('./README.md', encoding='utf-8') as readme_md:
    long_description = readme_md.read()

setup(
    name="pesi",
    version="0.0.2",
    author="pesi1874",
    author_email="pesi1874@gmail.com",
    description="Build your Python project to Docker image on remote Docker server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pesi1874/pesi",
    packages=find_packages(exclude=['__pycache__']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux"
    ],
    python_requires='>=3.5',
    install_requires=[
        'click >= 7.1.1',
        ],
    entry_points="""
    [console_scripts]
    pesi=pesi.main:cli
    """,
)
