# Chiloc
---
This module is a experimental project, which serves for scholars who need to collect geographic data, such as longitude and latitude, to support their studies. 

In the initial version, it only supports Chinese city so that all the string inputs should be better type in Chinese for fine working.

# Installation 
--- 
The code should run with no issues using Python versions 3.*.
Here are the libraries needed in this project: 

- pandas 
- numpy 
- json 
- urllib.request
- os
- time 


# Motivation
---
It starts from my PhD. classmate needs in data of lagtitude and longitude to do her research on house pricing in Beijing city. She also needs to know whether there are any park, hospital, subway stop or any facility around neighborhood which could probably affect the house price.  

It is the first module that made by me, which would definitely have plenty drawbacks. If you find it is not convenient or it is just suck, please feel free to contact me or modify it on github.  

# File Descriptions
---
- Chiloc.py : The starter file of Chiloc class.
- Locator.py : A children class of Chiloc class, which emphasis more on city-scope.
- helper.py : A helper function file.
- __ init __.py : Initiator file of Chiloc module. 
- setup.cg : Configuration. 
- README.md : Me.

# Classes and Functions
---
#### 1. class Chiloc():
*China locator class aims to give more details about a given location. In this very basic function, it only offers the longitude and latitude*

*Attributes:*
- `name (string)`: representing the name of the location.
- `lng (float)`: representing the longitude of the location.
- `lat (float)`: representing the latitude of the location.

*Arguments:*
- `place_name (string)`: The given location. Default is 北京大学国家发展研究院

*Returns:*     
**None**

***1**. Example 1: Default*
```
Chiloc()
```
Place: 北京大学国家发展研究院, lng: 116.3164368588075, lat: 40.003797501668416
```
Chiloc.name
```
北京大学国家发展研究院


***2**. Example 2: Giving location*
```
Chiloc('北京展览馆')
```
Place: 北京展览馆, lng: 116.35065083456274, lat: 39.946059901935605
```
Chiloc.name
```
北京展览馆


#### 2. class CityLocator(Chiloc):
*A child class of `Chiloc()`. It focus on city-scope and it help to find the distance  between two places and search for facilities around a given place*

*Plus, it offers a initiation of subways stop data all over the world.*

*Attributes:*
- `name (string)`: representing the name of the location.
- `lng (float)`: representing the longitude of the location.
- `lat (float)`: representing the latitude of the location.
- `city(string)`: representing the city of the location.

*Arguments:*
- `place_name (string)`: The given location. Default is '北京大学国家发展研究院'
- `place_city (string)`: the city of the location, default is '北京市'

*Returns:*     
**None**

***1**. Example 1: Default*
```
from chiloc.Locator import CityLocator
CityLocator()
```
Place: 北京市 北京大学国家发展研究院,  lng: 116.3164368588075,  lat: 40.003797501668416

```
CityLocator().city
```
北京市


***2**. Example 2: Giving location*
```
>>>CityLocator('迪士尼乐园','上海市')
```
Place: 上海市 迪士尼乐园, lng: 107.42295560126018, lat: 40.76438284864437

##### Methods
1 . `distance(self, other)`:
This method returns the walking distance between two places in meter.

**Example** 
```
a = CityLocator('上海博物馆','上海市')
b = CityLocator('南京路步行街	', '上海市')
a.distance(b)
```







# Licensing, Authors, Acknowledgements
---