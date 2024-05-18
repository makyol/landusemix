
import json
import pandas as pd
import geopandas as gpd
import os

def read_json(filepath):
    """Read a JSON file and return a Python dictionary."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def convert_dataframe_to_dict(dataframe):
    """Convert a DataFrame to a Python dictionary."""
    return dataframe.to_dict()

def load_geojson(filepath):
    """Load a GeoJSON file into a GeoDataFrame."""
    return gpd.read_file(filepath)

def load_shapefile(filepath):
    """Load a Shapefile into a GeoDataFrame."""
    return gpd.read_file(filepath)

def load_csv(filepath):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

def load_sample_geojson():
    """Load the included sample GeoJSON file."""
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.geojson')
    return load_geojson(sample_path)

def load_sample_shapefile():
    """Load the included sample Shapefile."""
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.shp')
    return load_shapefile(sample_path)

def load_sample_csv():
    """Load the included sample CSV file."""
    sample_path = os.path.join(os.path.dirname(__file__), 'data', 'sample.csv')
    return load_csv(sample_path)
