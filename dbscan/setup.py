"""
Lambdata - a collection of data science helper finctions for lambda school
"""

import setuptools

REQUIRED = [
        "numpy",
        ]

with open("README.md", "r") as fh:
    LONG_DESCRIPTON = fh.read()
    setuptools.setup(
            name="dbscan2",
            version="0.0.3",
            author="mpharm88",
            description="Density Based Spatial Clustering of Applications with Noise",
            long_description=LONG_DESCRIPTON,
            long_description_content_type="text/markdown",
            url="https://github.com/mpHarm88/projects/tree/master/dbscan",
            packages=setuptools.find_packages(),
            python_requires=">=3.6",
            install_requires=REQUIRED,
            classifiers=["Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
             ]
            )
