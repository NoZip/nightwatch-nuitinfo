import xml.etree.ElementTree as ET
from google.appengine.ext import db

class MapMarker(db.Model):
	"""
	Models an individual user generated Map Marker.
	Registers Marker name, coordinates.
	"""
	name = db.StringProperty()
	coordinates = db.GeoPtProperty()
	url = db.StringProperty()
	summary = db.StringProperty(multiline=True)
	adress = db.StringProperty(multiline=True)
	img_url = db.StringProperty
	category = db.StringProperty


	def __init__(self,data=None):
		"""
		Populates the instance data,
		using a dictionnary given as a parameter.
		"""
		if data:
			latitude = data['y_lat']
			longitude = data['x_long']
			super(MapMarker,self).__init__( name = data['name'],
											coordinates = db.GeoPt(lat=latitude, lon=longitude),
											url = data.get('url', None),
											summary = data.get('summary', None),
											adress = data.get('adress', None),
											img_url = data.get('img_url', None),
											category = data.get('category', None))

	def to_element():
		"""
		Returns an element representation of the instance data.
		"""
		element = ET.Element('Marker')
		ET.SubElement(element,'name').text = self.name
		ET.SubElement(element,'x_long').text = self.coordinates.lon
		ET.SubElement(element,'y_lat').text = self.coordinates.lat
		for key, prop in self.properties().iteritems():
			if prop and key not in ('name','coordinates'):
				ET.SubElement(element, str(key)).text = prop
			# ET.SubElement(element,'url').text = self.url
			# ET.SubElement(element,'summary').text = self.summary
			# ET.SubElement(element,'adress').text = self.adress
			# ET.SubElement(element,'img_url').text = self.img_url
			# ET.SubElement(element,'category').text = self.category
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
		url = element.find('url').text
		summary = element.find('summary').text
		adress = element.find('adress').text
		img_url = element.find('img_url').text
		category = element.find('category').text
		instance = MapMarker(data = {'name':name,
									 'x_long':longitude,
									 'y_lat':latitude,
									 'url':url,
									 'summary':summary,
									 'adress':adress,
									 'img_url':img_url,
									 'category':category})
		return instance