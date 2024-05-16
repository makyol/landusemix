
# Land Use Mix Python Package

## Overview

The `landusemix` package provides tools for calculating various land use mix indices. These indices can be used to measure the diversity, concentration, and dissimilarity of land use areas. This can be valuable for GIS researchers and urban planners.

### Features

- **Entropy Index**: Measures the diversity of land use.
- **Herfindahl-Hirschman Index (HHI)**: Measures the concentration of land use.
- **Dissimilarity Index**: Compares the distribution of land uses between different areas.
- **Balance Index**: Another measure of land use diversity.
- **Custom D(k) Calculation**: Computes a custom index based on a specific model.

## Installation

```bash
pip install landusemix
```

## Usage

### Importing the Package

You can import the necessary classes and functions from the package as follows:

```python
from landusemix.indices import LandUseMixIndices
from landusemix.utils import load_geojson, load_shapefile, load_csv
from landusemix.utils import load_sample_geojson, load_sample_shapefile, load_sample_csv
```

### Loading Data

You can load data from various formats including GeoJSON, Shapefile, and CSV.

#### Example: Loading GeoJSON Data

```python
geojson_data = load_geojson('path_to_your_file.geojson')
```

#### Example: Loading Shapefile Data

```python
shapefile_data = load_shapefile('path_to_your_file.shp')
```

#### Example: Loading CSV Data

```python
csv_data = load_csv('path_to_your_file.csv')
```

### Using Sample Data

The package includes sample data files for testing and demonstration purposes.

#### Example: Loading Sample GeoJSON Data

```python
sample_geojson = load_sample_geojson()
print(sample_geojson)
```

#### Example: Loading Sample Shapefile Data

```python
sample_shapefile = load_sample_shapefile()
print(sample_shapefile)
```

#### Example: Loading Sample CSV Data

```python
sample_csv = load_sample_csv()
print(sample_csv)
```

### Computing Indices

You can instantiate the `LandUseMixIndices` class with your land use data and compute various indices.

#### Example: Computing Entropy and HHI

```python
# Example land use data as a dictionary
land_use_areas = {
    "residential": 500,
    "commercial": 300,
    "industrial": 200,
}

# Instantiate the class
indices = LandUseMixIndices(land_use_areas)

# Compute indices
print("Entropy Index:", indices.entropy_index())
print("HHI:", indices.herfindahl_hirschman_index())
```

#### Example: Computing Dissimilarity Index

```python
# Another set of land use data to compare with
other_land_use_areas = {
    "residential": 450,
    "commercial": 350,
    "industrial": 200,
}

# Compute dissimilarity index
print("Dissimilarity Index:", indices.dissimilarity_index(other_land_use_areas))
```

#### Example: Using Sample Data

You can also use the sample data provided in the package to compute indices.

```python
# Load sample data and convert to dictionary
sample_land_use_areas = sample_csv.set_index('use')['area'].to_dict()

# Instantiate the class with sample data
indices_sample = LandUseMixIndices(sample_land_use_areas)

# Compute indices
print("Sample Data Entropy Index:", indices_sample.entropy_index())
print("Sample Data HHI:", indices_sample.herfindahl_hirschman_index())
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to improve the package.

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, please reach out to [Your Contact Information].
