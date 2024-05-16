
Usage
=====

Here's how you can use the `landusemix` package to calculate the entropy and HHI indices.

.. code-block:: python

    from landusemix import LandUseMixIndices  # Updated import statement

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
