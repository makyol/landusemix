from setuptools import setup, find_packages

setup(
    name="landusemix",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "geopandas",
        "shapely"
    ],
    include_package_data=True,
    description="Land use mix indices calculation",
    author="Mehmet Ali Akyol",
    author_email="akyol.mehmet@metu.edu.tr",
    url="https://github.com/makyol/landusemix",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
