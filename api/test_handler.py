from random import randrange
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler

from api.models.mapmarker import MapMarker

class TestAddHandler(RequestHandler):
    def get(self, name):
        map_marker = MapMarker(data=dict(name=name, x_long=randrange(-180, 180, 0.000001), y_lat=randrange(-180, 180, 0.000001)))
        map_marker.put();
        
        self.response.write("Enregistre")

class TestListHandler(RequestHandler):
    def get(self):
        query = Node.all()
        
        root = ElementTree.Element("root")
        
        for map_marker in query.fetch(limit=50):
            root_node.append(map_marker.to_element())
        
        self.response.write(ElementTree.tostring(root, encoding="utf-8"))
