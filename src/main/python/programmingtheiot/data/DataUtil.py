#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import json
import logging
from decimal import Decimal
from json import JSONEncoder

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtil():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, encodeToUtf8 = False):
		self.encodeToUtf8=encodeToUtf8
		logging.info("Created DataUtil instance.")
	
	def actuatorDataToJson(self,data:ActuatorData=None,useDecForFloat:bool=False):
		if not data:
			logging.debug("ActuatorData is null. Returning empty string.")
			return ""

		jsonData=self._generateJsonData(obj=data,useDecForFloat=False)
		return jsonData
		
	def jsonToActuatorData(self,jsonData:str=None,useDecForFloat:bool=False):
		if not jsonData:
			logging.warning("JSON data is empty or null. Returning null.")
			return None

		jsonStruct=self._formatDataAndLoadDictionary(jsonData,useDecForFloat=useDecForFloat)
		ad=ActuatorData()
		self._updateIotData(jsonStruct,ad)
		return ad

	def _formatDataAndLoadDictionary(self,jsonData:str,useDecForFloat:bool=False)->dict:
		jsonData=jsonData.replace("\'","\"").replace('False','false').replace('True','true')

		jsonStruct=None

		if useDecForFloat:
			jsonStruct=json.loads(jsonData,parse_float=Decimal)
		else:
			jsonStruct=json.loads(jsonData)

		return jsonStruct
	
	def _generateJsonData(self,obj,useDecForFloat:bool=False)->str:
		jsonData=None

		if self.encodeToUtf8:
			jsonData=json.dumps(obj,cls=JsonDataEncoder).encode('utf8')
		else:
			jsonData=json.dumps(obj,cls=JsonDataEncoder,indent=4)

		if jsonData:
			jsonData=jsonData.replace("\'","\"").replace('False','false').replace('True','true')

		return jsonData
		
	def _updateIotData(self,jsonStruct,obj):
		varStruct=vars(obj)

		for key in jsonStruct:
			if key in varStruct:
				setattr(obj,key,jsonStruct[key])
			else:
				logging.warn("JSON data contains key not mappable to object: %s",key)
    
	def sensorDataToJson(self, data: SensorData = None, useDecForFloat: bool = False):
		if not data:
			logging.debug("SensorData is null. Returning empty string.")
			return ""

		jsonData = self._generateJsonData(obj=data, useDecForFloat=useDecForFloat)
		return jsonData

	def sensorDataToJson(self, sensor_data_obj):
		"""
		Convierte un objeto SensorData a una cadena JSON.
		"""
		try:
			return json.dumps(sensor_data_obj.__dict__)
		except Exception as e:
			print("Error al convertir SensorData a JSON:", e)
			return None

	def jsonToSensorData(self, jsonStr):
		"""
		Convierte una cadena JSON a un objeto SensorData.
		"""
		try:
			data = json.loads(jsonStr)
			sensorDataObj = SensorData()  # Asegúrate de que SensorData esté importado correctamente.
			sensorDataObj.__dict__.update(data)
			return sensorDataObj
		except Exception as e:
			print("Error al convertir JSON a SensorData:", e)
			return None

	def jsonToSystemPerformanceData(self, jsonStr):
		"""
		Convierte una cadena JSON a un objeto SystemPerformanceData.
		"""
		try:
			data = json.loads(jsonStr)
			sysPerfObj = SystemPerformanceData()  # Asegúrate de importar SystemPerformanceData.
			sysPerfObj.__dict__.update(data)
			return sysPerfObj
		except Exception as e:
			print("Error al convertir JSON a SystemPerformanceData:", e)
			return None
        

class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
		return o.__dict__
	