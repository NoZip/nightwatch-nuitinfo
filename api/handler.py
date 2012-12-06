
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler

from api.models.mapmarker import MapMarker

def get_map_markers_by_zone(longitude, latitude, radius, limit=50):
    query = Node.all()
    query.filter("longitude >", longitude - radius)
    query.filter("longitude <", longitude + radius)
    query.filter("latitude >", latitude - radius)
    query.filter("latitude <", latitude + radius)
    
    for map_marker in query.fetch(limit=limit):
      if ((map_marker.longitude - longitude) ** 2 + (map_marker.latitude - latitude) ** 2 == radius ** 2):
          yield map_marker


class ApiHandler(RequestHandler):
    def get(self):
        try:
          longitude = self.request.GET['longitude']
          latitude = self.request.GET['latitude']
          radius = self.request.GET['radius']
        except KeyError as e:
          self.response.status = 404
          return
          
        limit = self.request.GET.get('limit', 50)
        
        root = ElementTree.Element("root")
        
        for map_marker in get_nodes_by_zone(longitude, latitude, radius, limit):
            root_node.append(map_marker.to_element())
        
        self.response.write(ElementTree.tostring(root, encoding="utf-8"))
    
    def post(self):
        try:
          map_marker = MapMarker(self.request.POST)
        except KeyError as e:
          self.response.status = 404
          return
        
        map_marker.put()
        
        self.response.status = 201
    
    def put(self):
        element = ElementTree.fromstring(self.request.body)
        map_marker = MapMarker.from_element(element)
        map_marker.put()
        
        self.response.status = 201
