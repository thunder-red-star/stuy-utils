"""Setup for the StuyUtils package."""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stuy_utils",
    version="0.0.4",
    author="Anthony Chen, ThunderRedStar",
    author_email="anthonychen318@gmail.com, thunderredstar@gmail.com",
    description="Useful functions & utilities for Stuyvesant High School.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thunder-red-star/stuy-utils",
    packages=setuptools.find_packages(),
    package_data={"stuy_utils": ["data/*.tsv"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    data_files=[
        ("regular", ["stuy_utils/data/regular.tsv"]),
        ("conference", ["stuy_utils/data/conference.tsv"]),
        ("homeroom", ["stuy_utils/data/homeroom.tsv"]),
    ]
)
