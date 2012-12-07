import xml.etree.ElementTree as ET
from google.appengine.ext import db

class MapMarker(db.Model):
	"""
	Models an individual user generated Map Marker.

	Registers Marker name and coordinates.
	Optionnaly registers additional information.

	MapMarker(**kwargs)

	All parameters are single line strings unless noted otherwise.

	name : name of Marker (mandatory)
	x_long : float - longitude of Marker (mandatory)
	y_lat : float - latitude of Marker (mandatory)
	url : relevant url
	summary : multiline string - short summary
	adress : multiline string - adress of the Marker if relevant
	img_url : associated image url
	category : category of Marker (eg. 'restaurant', 'accomodation', etc.)

	"""
	name = db.StringProperty(required=True)
	x_long = db.FloatProperty(required=True)
	y_lat = db.FloatProperty(required=True)
	url = db.StringProperty()
	summary = db.StringProperty(multiline=True)
	adress = db.StringProperty(multiline=True)
	img_url = db.StringProperty()
	category = db.StringProperty()

	def to_element(self):
		"""
		Returns an element representation of the instance data.
		"""
		element = ET.Element('node')
		ET.SubElement(element,'name').text = self.name
		ET.SubElement(element,'x_long').text = "{:0.9f}".format(self.x_long)
		ET.SubElement(element,'y_lat').text = "{:0.9f}".format(self.y_lat)
		ET.SubElement(element,'url').text = self.url
		ET.SubElement(element,'summary').text = self.summary
		ET.SubElement(element,'adress').text = self.adress
		ET.SubElement(element,'img_url').text = self.img_url
		ET.SubElement(element,'category').text = self.category
		return element

	@classmethod
	def from_element(element):
		"""
		Generates a MapMarker instance,
		taking an element as a parameter.
		"""
		name = element.find('name').text
		x_long = float(element.find('x_long').text)
		y_lat = float(element.find('y_lat').text)
		url = element.find('url').text
		summary = element.find('summary').text
		adress = element.find('adress').text
		img_url = element.find('img_url').text
		category = element.find('category').text
		instance = MapMarker(name=name,
							 x_long=x_long,
							 y_lat=y_lat,
							 url=url,
							 summary=summary,
							 adress=adress,
							 img_url=img_url,
							 category=category)
		return instance