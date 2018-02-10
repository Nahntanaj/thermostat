'''
Created on Feb 9, 2018

@author: JStringer
'''

import json

class Thermostat:
    def __init__(self, identifier, name, currentTemp, operationMode, coolSetPoint, heatSetPoint, fanMode):
        self.identifier = identifier
        self.name = name
        self.currentTemp = currentTemp
        self.operationMode = operationMode
        self.coolSetPoint = coolSetPoint
        self.heatSetPoint = heatSetPoint
        self.fanMode = fanMode
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    