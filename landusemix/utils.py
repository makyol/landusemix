"""
Utility functions for reading and loading data files. 
"""
import json
import pandas as pd
import geopandas as gpd
import rasterio
import os


def read_json(filepath):
    """
    Read a JSON file and return a Python dictionary.

    Parameters:
    filepath (str): The path to the JSON file.

    Returns:
    dict: The contents of the JSON file as a Python dictionary.
    """
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def convert_dataframe_to_dict(dataframe):
    """
    Convert a DataFrame to a Python dictionary.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame to be converted.

    Returns:
    dict: The DataFrame converted to a Python dictionary.
    """
    return dataframe.to_dict()


def load_geojson(filepath):
    """
    Load a GeoJSON file into a GeoDataFrame.

    Parameters:
    filepath (str): The path to the GeoJSON file.

    Returns:
    geopandas.GeoDataFrame: The loaded GeoDataFrame.
    """
    return gpd.read_file(filepath)


def load_shapefile(filepath):
    """
    Load a Shapefile into a GeoDataFrame.

    Parameters:
    filepath (str): The path to the Shapefile.

    Returns:
    geopandas.GeoDataFrame: The loaded GeoDataFrame.
    """
    return gpd.read_file(filepath)


def load_csv(filepath):
    """
    Load a CSV file into a DataFrame.

    Parameters:
    filepath (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(filepath)


def load_raster(filepath):
    """
    Load a raster file into a GeoDataFrame.

    Parameters:
    filepath (str): The path to the raster file.

    Returns:
    numpy.ndarray: The loaded raster data.
    """
    with rasterio.open(filepath) as src:
        return src.read(1)


def load_sample_geojson():
    """
    Load the included sample GeoJSON file.

    Returns:
    geopandas.GeoDataFrame: The loaded sample GeoDataFrame.
    """
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'geojson', 'multiple.geojson')
    return load_geojson(sample_path)


def load_sample_shapefile():
    """
    Load the included sample Shapefile.

    Returns:
    geopandas.GeoDataFrame: The loaded sample GeoDataFrame.
    """
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'shapefiles', 'multiple.shp')
    return load_shapefile(sample_path)


def load_sample_csv():
    """
    Load the included sample CSV file.

    Returns:
    pandas.DataFrame: The loaded sample DataFrame.
    """
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.csv')
    return load_csv(sample_path)


def load_sample_raster():
    """
    Load the included sample raster file.

    Returns:
    numpy.ndarray: The loaded sample raster data.
    """
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'raster.tif')
    return load_raster(sample_path)
