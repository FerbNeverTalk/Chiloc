from .Chiloc import Chiloc
from .helper import city_code_init
import numpy as np
import pandas as pd 
import json
from urllib.request import urlopen, quote
import os 

class CityLocator(Chiloc):
	"""
	"""
	
	def __init__(self, place_name = '北京大学国家发展研究院', place_city = '北京市'):
	
		Chiloc.__init__(self, place_name)
		self.name = place_city + ' ' + self.name
		self.city = place_city
		
		
	def distance(self, other):
		
		url = 'http://api.map.baidu.com/directionlite/v1/walking'
		ak = 'H3bQs5XVuBaLnoQ3CvIzZUiEYrr5Bym4'
		
		url = (url + '?' + 'origin=' + str(self.lat) +',' + str(self.lng) 
		+ '&destination=' + str(other.lat) + ',' + str(other.lng) + '&ak=' + ak)
		
		req = urlopen(url)
		# decode as unicode
		res = req.read().decode()
		temp = json.loads(res)
		
		try:
			distance = temp['result']['routes'][0]['distance']
		except:
			pass
		
		return distance
	
	
	def nearest(self, object_ask, radius = 2000):
		
		ak = 'H3bQs5XVuBaLnoQ3CvIzZUiEYrr5Bym4'
		object_quote = quote(object_ask)
		url = ('http://api.map.baidu.com/place/v2/search?query=' + object_quote + '&location=' + str(self.lat) 
		+ ',' + str(self.lng) + '&radius=' + str(radius) + '&output=json&ak=' + ak)
		
		req = urlopen(url)
		res = req.read().decode()
		temp = json.loads(res)
		
		try:
			name = temp['results'][0]['name']
			address = temp['results'][0]['address']
			district = temp['results'][0]['area']
			object_ = object_ask + ' - ' + name
			distance = self.distance(CityLocator(object_ask + name))

			print('The nearest {} is {} and it locates at {}, {} with the distance {} m.'.format(object_ask, object_, district, address, distance))
		
		except:
			print('Oops! It is considered that there is no any {}-like facility within {}m. Maybe we can try a greater radius.'.format(object_ask, radius))
		
			name = ''
			address = ''
			district = ''
			distance = ''
		
		return name, address, district, distance
	
	def subway_initiator(self):
		
		print('Initialization...')
		print('Track the citycode for {}'.format(self.city))
		city_code = pd.read_csv('City_codes.csv', encoidng = 'gbk')
		code = city_code[city_code['City'] == self.city]['Code']
		
		req = urlopen('http://map.baidu.com/?qt=bsi&c='+ code + '&t=123457788')
		res = req.read().decode()
		temp = json.loads(response)
		
		# Create subway dataframe 
		
		print('Generating the subway data in {}.'.format(self.city))
		subway = pd.DataFrame()
		subway['Stop'], subway['Line'], subway['lat'], subway['lng'] = np.nan, np.nan, np.nan, np.nan
		
		stops, lines, lats, lngs = [], [], [], []
		
		for i in range(len(temp['content'])):
			line = temp['content'][i]['line_name']
			print('Loading for {}:'.format(line))
			for j in range(len(temp['content'][i]['stops'])):
				stop = temp['content'][i]['stops'][j]['name']
				stops.append(stop)
				lines.append(line)

				try:
					lats.append(getlnglat(stop + ' - 地铁站')[0])
					lngs.append(getlnglat(stop + ' - 地铁站')[1])
					print('	- {} is loaded.'.format(stop))
				except: 
					lats.append(np.nan)
					lngs.append(np.nan)
					print('	- Fails to load {} for some reason.'.format(stop))
				

		subway['Stop'] = stops
		subway['Line'] = lines
		subway['lat'] = lats
		subway['lng'] = lngs
		
		print('The subway data of {} is generated!'.format(self.city))
		
		try:
			os.mkdir('./subway_data')
		except:
			pass
		
		path = './subway_data/' + self.city + '_subway.csv'
		subway.to_csv(path, index = False)
		
			
