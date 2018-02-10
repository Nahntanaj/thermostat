'''
Created on Feb 9, 2018

@author: jonathan
'''

import json

class ThermostatError:
    def __init__(self, errorCode, errorDescription):
        self.errorCode = errorCode
        self.errorDescription = errorDescription
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)