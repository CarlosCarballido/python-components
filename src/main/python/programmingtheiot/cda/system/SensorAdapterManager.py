import logging
from importlib import import_module
from apscheduler.schedulers.background import BackgroundScheduler

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask

class SensorAdapterManager(object):
    """
    Manages sensor adapters and retrieves sensor data.
    """

    def __init__(self):
        self.configUtil = ConfigUtil()

        self.pollRate = self.configUtil.getInteger(
            section=ConfigConst.CONSTRAINED_DEVICE, key=ConfigConst.POLL_CYCLES_KEY, defaultVal=ConfigConst.DEFAULT_POLL_CYCLES)

        self.useEmulator = self.configUtil.getBoolean(
            section=ConfigConst.CONSTRAINED_DEVICE, key=ConfigConst.ENABLE_EMULATOR_KEY)

        self.useSenseHat = self.configUtil.getBoolean(
            section=ConfigConst.CONSTRAINED_DEVICE, key=ConfigConst.ENABLE_SENSE_HAT_KEY)

        self.locationID = self.configUtil.getProperty(
            section=ConfigConst.CONSTRAINED_DEVICE, key=ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal=ConfigConst.NOT_SET)

        if self.pollRate <= 0:
            self.pollRate = ConfigConst.DEFAULT_POLL_CYCLES

        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(
            self.handleTelemetry, 'interval', seconds=self.pollRate, max_instances=2, coalesce=True, misfire_grace_time=15)

        self.dataMsgListener = None
        self.humidityAdapter = None
        self.pressureAdapter = None
        self.tempAdapter = None

        self._initEnvironmentalSensorTasks()

    def _initEnvironmentalSensorTasks(self):
        if self.useSenseHat:
            logging.info("Using I2C-based sensors for SenseHAT.")

            self.humidityAdapter = HumidityI2cSensorAdapterTask()
            self.pressureAdapter = PressureI2cSensorAdapterTask()
            self.tempAdapter = TemperatureI2cSensorAdapterTask()

        elif self.useEmulator:
            logging.info("Using SenseHAT emulated sensors.")

            heModule = import_module('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', 'HumiditySensorEmulatorTask')
            heClazz = getattr(heModule, 'HumiditySensorEmulatorTask')
            self.humidityAdapter = heClazz()

            peModule = import_module('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', 'PressureSensorEmulatorTask')
            peClazz = getattr(peModule, 'PressureSensorEmulatorTask')
            self.pressureAdapter = peClazz()

            teModule = import_module('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', 'TemperatureSensorEmulatorTask')
            teClazz = getattr(teModule, 'TemperatureSensorEmulatorTask')
            self.tempAdapter = teClazz()

        else:
            logging.info("Using simulated sensor data.")

            self.dataGenerator = SensorDataGenerator()

            humidityData = self.dataGenerator.generateDailyEnvironmentHumidityDataSet(
                minValue=SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY,
                maxValue=SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY,
                useSeconds=False)

            pressureData = self.dataGenerator.generateDailyEnvironmentPressureDataSet(
                minValue=SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE,
                maxValue=SensorDataGenerator.HI_NORMAL_ENV_PRESSURE,
                useSeconds=False)

            tempData = self.dataGenerator.generateDailyIndoorTemperatureDataSet(
                minValue=SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP,
                maxValue=SensorDataGenerator.HI_NORMAL_INDOOR_TEMP,
                useSeconds=False)

            self.humidityAdapter = HumiditySensorSimTask(dataSet=humidityData)
            self.pressureAdapter = PressureSensorSimTask(dataSet=pressureData)
            self.tempAdapter = TemperatureSensorSimTask(dataSet=tempData)

    def handleTelemetry(self):
        humidityData = self.humidityAdapter.generateTelemetry()
        pressureData = self.pressureAdapter.generateTelemetry()
        tempData = self.tempAdapter.generateTelemetry()

        humidityData.setLocationID(self.locationID)
        pressureData.setLocationID(self.locationID)
        tempData.setLocationID(self.locationID)

        logging.debug('Generated humidity data: ' + str(humidityData))
        logging.debug('Generated pressure data: ' + str(pressureData))
        logging.debug('Generated temp data: ' + str(tempData))

        if self.dataMsgListener:
            self.dataMsgListener.handleSensorMessage(humidityData)
            self.dataMsgListener.handleSensorMessage(pressureData)
            self.dataMsgListener.handleSensorMessage(tempData)

    def setDataMessageListener(self, listener: IDataMessageListener):
        if listener:
            self.dataMsgListener = listener

    def startManager(self) -> bool:
        logging.info("Started SensorAdapterManager.")

        if not self.scheduler.running:
            self.scheduler.start()
            return True
        else:
            logging.info("SensorAdapterManager scheduler already started. Ignoring.")
            return False

    def stopManager(self) -> bool:
        logging.info("Stopped SensorAdapterManager.")

        try:
            self.scheduler.shutdown()
            return True
        except:
            logging.info("SensorAdapterManager scheduler already stopped. Ignoring.")
            return False
