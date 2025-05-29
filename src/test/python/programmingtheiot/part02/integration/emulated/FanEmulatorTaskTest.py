import logging
import unittest
from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.emulated.FanEmulatorTask import FanEmulatorTask

class FanEmulatorTaskTest(unittest.TestCase):
	"""
	Test de integración para FanEmulatorTask, siguiendo el patrón de los otros actuadores emulados.
	"""
	@classmethod
	def setUpClass(cls):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing FanEmulatorTask class [using SenseHAT emulator]...")
		cls.fanTask = FanEmulatorTask()

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateEmulator(self):
		ad = ActuatorData(typeID = ConfigConst.FAN_ACTUATOR_TYPE)
		ad.setCommand(ConfigConst.COMMAND_ON)
		ad.setValue(80.0)
		adr = self.fanTask.updateActuator(ad)
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			sleep(5)
		else:
			logging.warning("ActuatorData is None.")
		ad.setValue(30.0)
		adr = self.fanTask.updateActuator(ad)
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_ON)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
			sleep(5)
		else:
			logging.warning("ActuatorData is None.")
		ad.setCommand(ConfigConst.COMMAND_OFF)
		adr = self.fanTask.updateActuator(ad)
		if adr:
			self.assertEqual(adr.getCommand(), ConfigConst.COMMAND_OFF)
			self.assertEqual(adr.getStatusCode(), 0)
			logging.info("ActuatorData: " + str(adr))
		else:
			logging.warning("ActuatorData is None.")

if __name__ == "__main__":
	unittest.main()