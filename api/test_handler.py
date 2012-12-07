from random import random
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler

from api.models.mapmarker import MapMarker


class TestAddHandler(RequestHandler):
    def get(self):
        map_marker = MapMarker(name="test", x_long=(-180 + random() * 360), y_lat=(-90 + random() * 180))
        map_marker.put()
        
        self.response.write("Enregistre")

class TestListHandler(RequestHandler):
    def get(self):
        query = MapMarker.all()
        
        root = ElementTree.Element("root")
        
        for map_marker in query.fetch(limit=50):
            root.append(map_marker.to_element())
        
        self.response.write(ElementTree.tostring(root, encoding="utf-8"))
