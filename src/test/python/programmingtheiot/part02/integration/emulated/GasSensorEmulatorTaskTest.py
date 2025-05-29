#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest
from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.GasSensorData import GasSensorData
from programmingtheiot.cda.emulated.GasSensorEmulatorTask import GasSensorEmulatorTask

class GasSensorEmulatorTaskTest(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing GasSensorEmulatorTask class...")
		self.gEmuTask = GasSensorEmulatorTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testReadEmulator(self):
		gd1 = self.gEmuTask.generateTelemetry()
		if gd1:
			self.assertEqual(gd1.getTypeID(), ConfigConst.GAS_SENSOR_TYPE)
			logging.info("GasSensorData: %f - %s", gd1.getValue(), str(gd1))
			sleep(2)
		else:
			logging.warning("FAIL: GasSensorData is None.")
		gd2 = self.gEmuTask.generateTelemetry()
		if gd2:
			self.assertEqual(gd2.getTypeID(), ConfigConst.GAS_SENSOR_TYPE)
			logging.info("GasSensorData: %f - %s", gd2.getValue(), str(gd2))
			sleep(2)
		else:
			logging.warning("FAIL: GasSensorData is None.")

if __name__ == "__main__":
	unittest.main()