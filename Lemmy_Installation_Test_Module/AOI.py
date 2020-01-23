import os
import shapefile


class AOI:

    def __init__(self):
        self.path = ''
        self.aoi = None
        self.bbox = None

    def get_aoi(self, path):
        self.path = path

        try:
            self.aoi = shapefile.Reader(path)
            self.bbox = self.aoi.bbox

        except IOError:
            print('')
