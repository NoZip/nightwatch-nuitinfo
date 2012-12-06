
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


class NodeXmlApi(RequestHandler):
    def get(self):
        pass
