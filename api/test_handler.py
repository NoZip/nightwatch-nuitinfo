from random import random
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler
from google.appengine.ext import db

from api.models.mapmarker import MapMarker


class TestAddHandler(RequestHandler):
    def get(self):
        lat = self.request.GET.get('lat', (-90 + random() * 180))
        lon = self.request.GET.get('lon', (-180 + random() * 360))
        map_marker = MapMarker(name="test", location=db.GeoPt(lat, lon))
        map_marker.put()
        
        self.response.write("Enregistre : %s" % str(map_marker.location))

class TestListHandler(RequestHandler):
    def get(self):
        query = MapMarker.all()
        
        root = ElementTree.Element("root")
        
        for map_marker in query.fetch(limit=50):
            root.append(map_marker.to_element())
        
        self.response.write(ElementTree.tostring(root, encoding="utf-8"))
