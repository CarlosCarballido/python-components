from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.GasSensorData import GasSensorData
import random

class GasSensorSimTask(BaseSensorSimTask):
    def __init__(self, name=ConfigConst.GAS_SENSOR_NAME, typeID=ConfigConst.GAS_SENSOR_TYPE):
        super().__init__(name=name, typeID=typeID)

    def generateTelemetry(self) -> GasSensorData:
        # Simula un valor de gas entre 0 y 100 (puedes ajustar el rango)
        value = random.uniform(0, 100)
        return GasSensorData(value=value)