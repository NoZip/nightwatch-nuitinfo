import xml.etree.ElementTree as ET
from google.appengine.ext import db

class MapMarker(db.Model):
	"""
	Models an individual user generated Map Marker.
	Registers Marker name, coordinates.
	"""
	name = db.StringProperty()
	coordinates = db.GeoPtProperty()

	def __init__(self,data=None):
		"""
		Populates the instance data,
		using a dictionnary given as a parameter.
		"""
		if data:
			self.name = data['name']
			latitude = data['y_lat']
			longitude = data['x_long']
			self.coordinates = db.GeoPt(lat=latitude, lon=longitude)

	def to_element():
		"""
		Returns an element representation of the instance data.
		"""
		element = ET.Element('Marker')
		ET.SubElement(element,'name').text = self.name
		ET.SubElement(element,'x_long').text = self.coordinates.lon
		ET.SubElement(element,'y_lat').text = self.coordinates.lat
		return element

	@classmethod
	def from_element(element):
		"""
		Generates a MapMarker instance,
		taking an element as a parameter.
		"""
		name = element.find('name').text
		longitude = element.find('x_long').text
		latitude = element.find('y_lat').text
		instance = MapMarker(data={'name':name, 'x_long':longitude, 'y_lat':latitude})
		return instance