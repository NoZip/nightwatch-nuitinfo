import xml.etree.ElementTree as ET
from google.appengine.ext import db

class MapMarker(db.Model):
	"""
	Models an individual user generated Map Marker.
	Registers Marker name, coordinates 
	"""
	name = db.StringProperty()
	coordinates = db.GeoPtProperty()

	def __init__(self,data):
		"""
		Populates the instance data,
		using a dictionnary given as a parameter.
		"""
		self.name = data['name']
		self.coordinates = data['coordinates']

	def to_element():
		"""
		Returns an element representation of the instance data.
		"""
		element = ET.Element('Marker')
		ET.SubElement(element,'name').text = self.name
		ET.SubElement(element,'coordinates').text = self.coordinates
		return element