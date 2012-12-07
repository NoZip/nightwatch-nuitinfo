
import math
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler
from google.appengine.ext import db

from api.models.mapmarker import MapMarker

class ApiHandler(RequestHandler):
    def get(self):
        try:
          longitude = float(self.request.GET['x_long'])
          latitude = float(self.request.GET['y_lat'])
          radius = float(self.request.GET['r'])
        except KeyError as e:
          self.response.status = 404
          return
          
        limit = self.request.GET.get('limit', 50)
        
        root = ElementTree.Element("root")
        result = MapMarker.proximity_fetch(MapMarker.all(),
                                           center=db.GeoPt(latitude, longitude),
                                           max_distance=radius)
        for map_marker in result:
          root.append(map_marker.to_element())
        self.response.write(ElementTree.tostring(root, encoding="utf-8"))
    
    def post(self):
        try:
          name = self.request.POST['name']
          x_long = self.request.POST['x_long']
          y_lat = self.request.POST['y_lat']
          category = self.request.POST['category']
        except KeyError as e:
          self.response.status = 404
          return
        
        map_marker = MapMarker(name=name,
                               location=db.GeoPt(y_lat, x_long),
                               category=category)
        
        if self.request.POST['url']:
            map_marker.url = self.request.POST['url']
        
        if self.request.POST['summary']:
            map_marker.summary = self.request.POST['symmary']
        
        if self.request.POST['address']:
            map_marker.uaddress = self.request.POST['address']
        
        if self.request.POST['img_url']:
            map_marker.img_url = self.request.POST['img_url']
        
        map_marker.update_location()
        map_marker.put()
        
        self.response.status = 201
    
    def put(self):
        element = ElementTree.fromstring(self.request.body)
        map_marker = MapMarker.from_element(element)
        map_marker.update_location()
        map_marker.put()
        
        self.response.status = 201
