import requests
import json
from geojson import GeometryCollection, Point, LineString, Polygon
import random
from enum import Enum
import datetime
from APIRequests import APIRequests

# AlexLÄTest
class GeometryType(Enum):
    polygon = 'polygon'
    polyline = 'polyline'
    point = 'point'
    circle = 'circle'


class CaseCreator:

    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.module_organization_name = 'Rakvatten AB'
        self.api = APIRequests(base_url=self.base_url, username=self.username, password=self.password)
        self.case_list = []
        if self.api.login():
            self.generate_cases()
        else:
            return 'failed to log in!'

    # Generate cases to test the LAM.
    def generate_cases(self):
        try:
            # self.cases = case()
            self.create_case_list()
            self.get_involved_case(len(self.case_list))

        except OSError:
            print("Failed to ")

    # Creates data 50 different cases with random geometries to the case_list.
    def create_case_list(self):
        geometry_types = ['polygon', 'polyline', 'point', 'circle']
        try:
            case_lat = 450000
            case_long = 54000

            # Generates cases within AOI (20 meters)
            for case in range(25):
                #self.create_geometry(random.choice(geometry_types), [case_lat, case_long])
                geometry_type = random.choice(geometry_types)
                case = self.create_geometry("point", (-115.81, 37.24))
                self.case_list.append(case)

            # Generates cases within AOI (20 meters) but don't intersect
            for case in range(12):
               # self.create_geometry(random.choice(geometry_types), [case_lat, case_long])
                geometry_type = random.choice(geometry_types)
                case = self.create_geometry("point", (-115.81, 37.24))
                self.case_list.append(case)

            # Generates cases within AOI (20 meters) who intersect.
            for case in range(13):
               # self.create_geometry(random.choice(geometry_types), [case_lat, case_long])
                geometry_type = random.choice(geometry_types)
                case = self.create_geometry("point", (-115.81, 37.24))
                self.case_list.append(case)

            print('CaseList populated!')

        except OSError:
            print('Failed to create cases to the  caselist!')

    def create_geometry(self, geometry_type, coordinates):
        try:
            geometries = []
            new_coordinates = []
            new_geometry = None
            if geometry_type.lower() == "polygon":
                self.create_case(Polygon(coordinates), 'Test')

            elif geometry_type.lower() == "point":
                self.create_case(Point(coordinates), 'Test')

            elif geometry_type.lower() == "polyline":
                self.create_case(LineString(coordinates), 'Test')


            return new_geometry

        except OSError:
            print('')

    def create_case(self, geometries, name):

        start_date = datetime.datetime.now().date() + datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=10)
        final_case = {
            "PropertyDesignation": "",
            "SiteContactName": self.username,
            "SiteContactPhone": "0707666050",
            "MeetUpAddress": {
                "StreetNameAndNumber": "Hambovagen 25 ",
                "PostCode": "43539",
                "CityName": "Molnlycke",
            },
            "WorkMethods": [
                "drilling",
                "blasting",
            ],
            "WorkCategory": [
                "1_1_EL",
                "1_3_DIKNING",
            ],
            "ExcavationDepth": 3,
            "PreferedContactWay": "email",
            "PreferedContactValue": "henrik.karlsson@kartena.se",
            "Attachments": [],
            "NotifyOnReply": "true",
            "NotificationViaSms": "0707666050",
            "CreatedUsing": "webservice",
            "Name": name,
            "Comment": "This case was created as a test",
            "Geometry": geometries,
            "StartDate": start_date.strftime("%Y-%m-%d"),
            "EndDate": end_date.strftime("%Y-%m-%d")
        }
        print(final_case)
        self.case_list.append(final_case)

    # Gets involved cases for the LAM.
    def get_involved_case(self):
        self.api.get_involved_recipients(self.case_list)
