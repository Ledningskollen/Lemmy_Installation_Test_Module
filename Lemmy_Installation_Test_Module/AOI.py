import os
import shapefile
import geojson


class AOI:

    def __init__(self, path):
        self.path = path
        self.aoi = shapefile.Reader(path)
        self.bbox = self.aoi.bbox

    # Creates 50 random geometries.
    def generate_coordinates(self):
        coordinates = []
        for coord in range(0, 50):
            coordinates.append(coord)

        return coordinates
