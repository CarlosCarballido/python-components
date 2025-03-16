#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import smbus
import logging
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

class TemperatureI2cSensorAdapterTask():
    """
    Implementation of the I2C sensor adapter for a temperature sensor.
    """

    def __init__(self):
        super(TemperatureI2cSensorAdapterTask, self).__init__()

        # Definir el tipo de sensor como sensor de temperatura
        self.sensorType = SensorData.TEMP_SENSOR_TYPE

        # Dirección I2C del sensor de temperatura (debes verificar la correcta dirección)
        self.tempAddr = 0x5F  # Valor de ejemplo, confirmar con la documentación del sensor

        # Inicializar el bus I2C (usar solo el bus 1 en Raspberry Pi)
        self.i2cBus = smbus.SMBus(1)

        # Inicializar el sensor escribiendo un valor en su dirección de control (debes verificar el registro correcto)
        self.i2cBus.write_byte_data(self.tempAddr, 0, 0)

        # Definir valores mínimo y máximo del sensor
        self.minVal = SensorDataGenerator.LOW_NORMAL_ENV_TEMP
        self.maxVal = SensorDataGenerator.HI_NORMAL_ENV_TEMP

	
    def generateTelemetry(self) -> SensorData:
        pass
	
    def getTelemetryValue(self) -> float:
        pass
	