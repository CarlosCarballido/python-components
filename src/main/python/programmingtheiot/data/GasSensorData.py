from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst

class GasSensorData(SensorData):
    def __init__(self, name=ConfigConst.GAS_SENSOR_NAME, typeID=ConfigConst.GAS_SENSOR_TYPE, value=ConfigConst.DEFAULT_VAL):
        super().__init__(name=name, typeID=typeID)
        self.setValue(value)