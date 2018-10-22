import json
from pprint import pprint
from KMLConvert import *
x = 3

if x==1: 
    with open('one_route.json') as f:
        data = json.load(f)
    
    for val in data:
        print(val)
        if val=='segments':
            for seg in data[val]:
                print (seg['coordinates'])
                #print (data[val][seg])
        elif val=='time':
             print (data[val])
        elif val=='distance':
             print (data[val])
        #pprint(val)
        
    #pprint(data["distance"])
elif x==2:
    with open('icons.json') as f:
        data = json.load(f)
        
    icon = IconStyle("start", data)
    print(icon.getStyleString())
    print(icon.getPoint("test22", ["10.222", "33.22"]))
    
    line = LineStyle("tetsLIne", "ffffff", 3)
    print(line.getStyleString())
    print(line.getLine([[10,10],[20,20],[30,30]]))
    
    map = Map("test map")
    map.addStyle(line.getStyleString())
    map.addStyle(icon.getStyleString())
    map.addPlaceMark(line.getLine([[10,10],[20,20],[30,30]]))
    map.addPlaceMark(icon.getPoint("test22", ["10.222", "33.22"]))
    
    print(map.getKMLData())

else:
    
    with open('icons.json') as f:
        iconSet = json.load(f)
    
    map = Map("test map")
    
    routeBegin = IconStyle("begin", iconSet)
    routeEnd = IconStyle("end", iconSet)
    busStart = IconStyle("start", iconSet)
    busFinish = IconStyle("finish", iconSet)
    busStop = IconStyle("stop", iconSet)
    
    map.addStyle(routeBegin.getStyleString())
    map.addStyle(routeEnd.getStyleString())
    map.addStyle(busStart.getStyleString())
    map.addStyle(busFinish.getStyleString())
    map.addStyle(busStop.getStyleString())
    
    with open('one_route.json') as f:
        routeJson = json.load(f)
    
    for seg in routeJson['segments']:
        
        import random
        r = lambda: random.randint(0,255)
        color = ('%02X%02X%02X' % (r(),r(),r()))
        busLine = LineStyle(seg['route']['name'], color, 5)
        coords = [];
        #for coordinate in seg['coordinates']:
        #    coords += [[coordinate['lon'],coordinate['lat']]];
        coords = list([coordinate['lon'],coordinate['lat']] for coordinate in seg['coordinates'])
        
        map.addPlaceMark(busLine.getLine(coords))
        map.addStyle(busLine.getStyleString())
        
        stops = seg['stops']
        for stop in stops:
            if stop == stops[0]:
                map.addPlaceMark(busStart.getPoint(stop['name'], [stop['lon'],stop['lat']]))
            elif stop == stops[-1]:
                map.addPlaceMark(busFinish.getPoint(stop['name'], [stop['lon'],stop['lat']]))
            else:
                map.addPlaceMark(busStop.getPoint(stop['name'], [stop['lon'],stop['lat']]))
        
    print(map.getKMLData())