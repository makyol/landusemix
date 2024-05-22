import glob
from setuptools import setup, find_packages

setup(
    name="landusemix",
    version="0.0.9",
    author="Mehmet Ali Akyol",
    author_email="akyol.mehmet@metu.edu.tr",
    description="A package for calculating land use mix indices",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/makyol/landusemix",
    packages=find_packages(),
    include_package_data=True,
        package_data={
        'landusemix': [
            'data/geojson/*.geojson',
            'data/*.csv',
            'data/shapefiles/*.shp',
            'data/shapefiles/*.shx',
            'data/shapefiles/*.dbf',
            'data/shapefiles/*.cpg',
            'data/shapefiles/*.prj',
            'data/shapefiles/*.qix',
        ],
    },
    install_requires=[
        'pandas',
        'geopandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
