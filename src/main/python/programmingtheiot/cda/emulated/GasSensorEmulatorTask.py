import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.GasSensorData import GasSensorData
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
import random

class GasSensorEmulatorTask(BaseSensorSimTask):
    def __init__(self, name=ConfigConst.GAS_SENSOR_NAME, typeID=ConfigConst.GAS_SENSOR_TYPE):
        super().__init__(name=name, typeID=typeID)

    def generateTelemetry(self) -> GasSensorData:
        # Aquí podrías leer de un SenseHAT real o emulado, pero por ahora simula
        value = random.uniform(0, 100)
        return GasSensorData(value=value)