'''
Created on Feb 9, 2018

@author: JStringer
'''
from bottle import Bottle, run
from bottle import get, put, request
import json
from Thermostat import Thermostat 

app = Bottle()

homeThermostats = {}

homeThermostats['101'] = Thermostat('101', 'thermostat1', 80, "off", 75, 65, "auto")
homeThermostats['102'] = Thermostat('102', 'thermostat2', 85, "cool", 75, 65, "auto")

print (json.dumps(homeThermostats, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))

def addThermostat(t: Thermostat):
    homeThermostats[t.id] = t

@get('/thermostat/list')
def listThermostats():
    #TODO serialize the list of thermostats
    return homeThermostats

@get('/thermostat/<id>')
def getThermostat(id):
    #TODO serialize the list of thermostats
    return homeThermostats[id].toString()

@get('/thermostat/<id>/name')
def getThermostatName(id):
    #TODO serialize the list of thermostats
    return homeThermostats[id].name

@put('/thermostat/<id>/name')
def setThermostatName(id):
    new_name = request.query.name
    homeThermostats[id].name = new_name
    return homeThermostats[id].toString()

#run(app, host='localhost', port=8080)