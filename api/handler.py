
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler

from api.models.mapmarker import MapMarker

def get_map_markers_by_zone(longitude, latitude, radius, limit=50):
    query = Node.all()
    query.filter("x_long >", longitude - radius)
    query.filter("x_long <", longitude + radius)
    query.filter("y_lat >", latitude - radius)
    query.filter("y_lat <", latitude + radius)
    
    for map_marker in query.fetch(limit=limit):
      if ((map_marker.x_long - longitude) ** 2 + (map_marker.y_lat - latitude) ** 2 == radius ** 2):
          yield map_marker


class ApiHandler(RequestHandler):
    def get(self):
        try:
          longitude = self.request.GET['x_lon']
          latitude = self.request.GET['y_lat']
          radius = self.request.GET['r']
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
          name = self.request.POST['name']
          x_long = self.request.POST['x_long']
          y_lat = self.request.POST['y_lat']
        except KeyError as e:
          self.response.status = 404
          return
        
        map_marker = MapMarker(name=name,
                               x_long=x_long,
                               y_lat=y_lat)
        
        if self.request.POST['url']:
            map_marker.url = self.request.POST['url']
        
        if self.request.POST['summary']:
            map_marker.summary = self.request.POST['symmary']
        
        if self.request.POST['address']:
            map_marker.uaddress = self.request.POST['address']
        
        if self.request.POST['img_url']:
            map_marker.img_url = self.request.POST['img_url']
        
        if self.request.POST['category']:
            map_marker.category = self.request.POST['category']
        
        map_marker.put()
        
        self.response.status = 201
    
    def put(self):
        element = ElementTree.fromstring(self.request.body)
        map_marker = MapMarker.from_element(element)
        map_marker.put()
        
        self.response.status = 201
