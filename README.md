
# Land Use Mix Python Package

## Overview

The `landusemix` package provides tools for calculating land use mix indices. These indices can be used to measure the diversity and concentration of land use areas, which is valuable for GIS researchers and urban planners.

## Features

- **Entropy Index**: Measures the diversity of land use. Values range from 0 (no diversity) to 1 (maximum diversity).
- **Herfindahl-Hirschman Index (HHI)**: Measures the concentration of land use. Values range from 0 (many small equally-sized areas) to 10,000 (one single area).

## Installation

You can install the package using pip:

```sh
pip install landusemix
```

## Usage

Here's how you can use the `landusemix` package to calculate the entropy and HHI indices.

### Importing the Package

```python
from landusemix import LandUseMixIndices
```

To import the utility functions of the package:

```python
from landusemix.utils import *
```

### Loading Data

```python
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

## Indices Description

- **Entropy Index**: 

The entropy index (ENT) is a measure of diversity in land use types within a given area. It is calculated using the following formula:

$$ \mathrm{ENT}=-\frac{\left[\sum_{i=1}^k P^i \ln \left(P^i\right)\right]}{\ln (k)} $$

Here's an explanation of the parameters in this formula:

$P^i$: This represents the proportion of the total area that is occupied by the ith land use type. It is calculated by dividing the area of the ith land use type by the total area.

$ln(P^i)$: This is the natural logarithm of P^i.

$\sum$: This is the sum operator. It sums the product of P^i and ln(P^i) for all land use types from i = 1 to i = k.

$k$: This is the total number of different land use types.

$ln(k)$: This is the natural logarithm of k.

The ENT value will be between 0 and 1. A higher ENT value indicates a more diverse mix of land use types, while a lower ENT value indicates a less diverse mix.

- **Herfindahl-Hirschman Index (HHI)**: 

The Herfindahl-Hirschman Index (HHI) is a measure of the concentration of land use types within a given area. It is calculated using the following formula:

$$ \mathrm{HHI}=\sum_{i=1}^k\left(100 \times P^i\right)^2 $$

Here's an explanation of the parameters in this formula:

$P^i$: This represents the proportion of the total area that is occupied by the ith land use type. It is calculated by dividing the area of the ith land use type by the total area.

$100 x P^i$: This is the proportion of the ith land use type, expressed as a percentage.

$(100 x P^i)^2$: This squares the percentage proportion of the ith land use type.

$\sum$: This is the sum operator. It sums the squared percentage proportions for all land use types from i = 1 to i = k.

The HHI value will be between 0 and 10000 (if expressed as a percentage). A higher HHI value indicates a less diverse mix of land use types (i.e., a higher concentration of certain types), while a lower HHI value indicates a more diverse mix.

For more detailed documentation, please visit our [ReadTheDocs page](https://landusemix.readthedocs.io).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or support, please reach out to <akyol.mehmet@metu.edu.tr>.
