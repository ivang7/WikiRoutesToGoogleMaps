#!/usr/bin/python
# -*- coding: latin-1 -*-

class LineStyle():
    def __init__(self, name, color, width):
        self.color = color
        self.name = name
        self.width = str(width)
    
    def getStyleString(self):
        return('<Style id="' + self.color + '"><LineStyle><color>' + self.color + '</color><width>' + self.width + '</width></LineStyle><BalloonStyle><text><![CDATA[<h3>$[name]</h3>]]></text></BalloonStyle></Style>')
        
    def getLine(self, points):
        result = "<Placemark><name>" + self.name + "</name><styleUrl>#" + self.color + "</styleUrl><LineString><tessellate>1</tessellate><coordinates>\r\n"
        for point in points:
            result += str(point[0]) + "," + str(point[1]) + ",0\r\n"
        result += "</coordinates></LineString></Placemark>"
        return result
        
class IconStyle():
    def __init__(self, style, jsonSettings):
        
        self.styleid = next(icon['id'] for icon in jsonSettings['icons'] if icon['name']==style)
        self.color = next(icon['color'] for icon in jsonSettings['icons'] if icon['name']==style)
        self.url = jsonSettings['default-url-icon']
        
        if style=="begin":
            self.name = "Начало пути"
        elif style=="end":
            self.name = "Конец пути"
        else:
            self.name = "Останоквка "
    
    
    def getStyleString(self):
        return('<Style id="' + self.styleid + '"><IconStyle><color>' + self.color + '</color><scale>1</scale><Icon><href>'
                + self.url + '</href></Icon></IconStyle><BalloonStyle><text><![CDATA[<h3>$[name]</h3>]]></text></BalloonStyle></Style>')
    
    def getPoint(self, title, point):
        return ('<Placemark><name>' + title + '</name><styleUrl>#' + self.styleid + '</styleUrl><Point><coordinates>'
                + str(point[0]) + ',' + str(point[1]) + ',0</coordinates></Point></Placemark>')

class Map():
    def __init__(self, name):
        self.name = name
        self.styles = ""
        self.placemarks = ""
    
    def addStyle(self, style):
        self.styles += style;
        
    def addPlaceMark(self, placemark):
        self.placemarks += placemark;
    
    def getKMLData(self):
        return('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>route</name><description/>'
                + self.styles + '<Folder><name>' + self.name + '</name>' 
                + self.placemarks + '</Folder></Document></kml>')
        