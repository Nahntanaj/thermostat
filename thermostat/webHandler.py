'''
Created on Feb 9, 2018

@author: JStringer
'''
from bottle import Bottle, run
from bottle import get, put, request
import json
from Thermostat import Thermostat
from ThermostatError import ThermostatError

app = Bottle()

homeThermostats = {}

homeThermostats['101'] = Thermostat('101', 'thermostat1', 80, "off", 75, 65, "auto")
homeThermostats['102'] = Thermostat('102', 'thermostat2', 85, "cool", 75, 65, "auto")

#output = "["
#for thermostat in homeThermostats:
#    output += homeThermostats[thermostat].toJSON() + ",\n"
#output = output[:-2] + "]"
#print(output)

def addThermostat(t: Thermostat):
    homeThermostats[t.id] = t

@app.get('/thermostat/list')
def listThermostats():
    output = "["
    for thermostat in homeThermostats:
        output += homeThermostats[thermostat].toJSON() + ",\n"
    
    output = output[:-2] + "]"
    return output

@app.get('/thermostat/<iden>')
def getThermostat(iden):
    try:
        return homeThermostats[iden].toJSON()
    except KeyError:
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()
    

@app.get('/thermostat/<iden>/name')
def getThermostatName(iden):
    try:
        return homeThermostats[iden].name
    except KeyError:
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.put('/thermostat/<iden>/name')
def setThermostatName(iden):
    new_name = request.query.name
    try:
        homeThermostats[iden].name = new_name
        return homeThermostats[iden].toJSON()
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.get('/thermostat/<iden>/currentTemp')
def getThermostatCurrentTemp(iden):
    try:
        print(homeThermostats[iden].currentTemp)
        return str(homeThermostats[iden].currentTemp)
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.get('/thermostat/<iden>/operationMode')
def getThermostatOperationMode(iden):
    try:
        return homeThermostats[iden].operationMode
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.put('/thermostat/<iden>/operationMode')
def setThermostatOperationMode(iden):
    new_mode = request.query.mode
    try:
        if new_mode == "cool" or new_mode == "heat" or new_mode == "off":
            homeThermostats[iden].operationMode = new_mode
        else:
            return ThermostatError(400, "Operation mode: {} is invalid.".format(new_mode)).toJSON()    
        return homeThermostats[iden].toJSON()
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.get('/thermostat/<iden>/coolPoint')
def getThermostatCoolPoint(iden):
    try:
        return str(homeThermostats[iden].coolSetPoint)
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.put('/thermostat/<iden>/coolPoint')
def setThermostatCoolPoint(iden):
    new_point = float(request.query.coolPoint)
    try:
        if new_point <= 100 and new_point >= 30:
            homeThermostats[iden].coolSetPoint = new_point
        else:
            return ThermostatError(400, "Cool point: {} is invalid.".format(new_point)).toJSON()   
        return homeThermostats[iden].toJSON()
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.get('/thermostat/<iden>/heatPoint')
def getThermostatHeatPoint(iden):
    try:
        return str(homeThermostats[iden].heatSetPoint)
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.put('/thermostat/<iden>/heatPoint')
def setThermostatHeatPoint(iden):
    new_point = float(request.query.heatPoint)
    try:
        if new_point < 100 and new_point > 30:
            homeThermostats[iden].heatSetPoint = new_point
        else:
            return ThermostatError(400, "Heat point: {} is invalid.".format(new_point)).toJSON()
        return homeThermostats[iden].toJSON()
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.get('/thermostat/<iden>/fanMode')
def getThermostatFanMode(iden):
    try:
        return homeThermostats[iden].fanMode
    except KeyError:        
        return ThermostatError(404, "Thermostat with id: {} is not found in this home.".format(iden)).toJSON()

@app.put('/thermostat/<iden>/fanMode')
def setThermostatFanMode(iden):
    new_mode = request.query.mode
    try:
        if new_mode == "auto" or new_mode == "off":
            homeThermostats[iden].fanMode = new_mode
        else:
            return ThermostatError(400, "Fan mode \"{}\" is invalid.".format(new_mode)).toJSON()
        return homeThermostats[iden].toJSON()
    except KeyError:        
        return ThermostatError(404, "Thermostat with id \"{}\" is not found in this home.".format(iden)).toJSON()

run(app, host='localhost', port=8080)