
import xml.etree.ElementTree as ElementTree

from webapp2 import RequestHandler

from models.node import Node

def get_nodes_by_zone(longitude, latitude, radius, limit=50):
    query = Node.all()
    query.filter("longitude >", longitude - radius)
    query.filter("longitude <", longitude + radius)
    query.filter("latitude >", latitude - radius)
    query.filter("latitude <", latitude + radius)
    
    for node in query.fetch(limit=limit):
      if ((node.longitude - longitude) ** 2 + (node.latitude - latitude) ** 2 == radius ** 2):
          yield node


class ApiHandler(RequestHandler):
    def get(self):
        try:
          longitude = self.GET['longitude']
          latitude = self.GET['latitude']
          radius = self.GET['radius']
        except Keyerror as e:
          self.response.status = 404
          return
          
        limit = self.GET.get('limit', 50)
        
        root_node = ElementTree.Element("root")
        
        for node in get_nodes_by_zone(longitude, latitude, radius, limit):
            root_node.append(node.toXML())
        
        self.response.write(ElementTree.tostring(root_node, encoding="utf-8"))
    
    def post(self):
        try:
          node = Node(name=self.POST['name'],
                      longitude=self.POST['longitude'],
                      latitude=self.POST['latitude'])
        except KeyError as e:
          self.response.status = 404
          return
        
        node.put()
        
        self.response.status = 201
    
    def put(self):
        node = Node.fromXML(self.body)
        node.put()
        
        self.response.status = 201
