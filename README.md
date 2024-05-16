
# Land Use Mix Python Package

## Overview

The `landusemix` package provides tools for calculating land use mix indices. These indices can be used to measure the diversity and concentration of land use areas, which is valuable for GIS researchers and urban planners.

### Features

- **Entropy Index**: Measures the diversity of land use. Values range from 0 (no diversity) to 1 (maximum diversity).
- **Herfindahl-Hirschman Index (HHI)**: Measures the concentration of land use. Values range from 0 (many small equally-sized areas) to 10,000 (one single area).

### Installation

You can install the package using pip:

```sh
pip install landusemix
```

### Usage

Here's how you can use the `landusemix` package to calculate the entropy and HHI indices.

```python
from landusemix import LandUseMixIndices

# Example land use areas (in square meters)
land_use_areas = {
    'residential': 5000,
    'commercial': 3000,
    'industrial': 2000,
}

# Create an instance of the LandUseMixIndices class
mix_indices = LandUseMixIndices(land_use_areas)

# Calculate the entropy index
entropy = mix_indices.entropy_index()
print(f"Entropy Index: {entropy}")

# Calculate the Herfindahl-Hirschman Index (HHI)
hhi = mix_indices.herfindahl_hirschman_index()
print(f"Herfindahl-Hirschman Index: {hhi}")
```

### Indices Description

- **Entropy Index**: This index measures the diversity of land use types within a given area. It is calculated as follows:
  \[ H = - \sum \left( rac{A_i}{A} \log rac{A_i}{A} ight) / \log K \]
  Where \( A_i \) is the area of land use type \( i \), \( A \) is the total area, and \( K \) is the number of land use types.

- **Herfindahl-Hirschman Index (HHI)**: This index measures the concentration of land use types within a given area. It is calculated as follows:
  \[ HHI = \sum \left( rac{A_i}{A} 	imes 100 ight)^2 \]
  Where \( A_i \) is the area of land use type \( i \), and \( A \) is the total area.

For more detailed documentation, please visit our [ReadTheDocs page](https://your-project.readthedocs.io).

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
