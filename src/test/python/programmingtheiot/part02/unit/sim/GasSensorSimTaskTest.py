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

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.sim.GasSensorSimTask import GasSensorSimTask

class GasSensorSimTaskTest(unittest.TestCase):
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing GasSensorSimTask class...")
		self.gSimTask = GasSensorSimTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testGenerateTelemetry(self):
		gd = self.gSimTask.generateTelemetry()
		if gd:
			logging.info("GasSensorData: " + str(gd))
		else:
			logging.warning("GasSensorData is None.")

if __name__ == "__main__":
	unittest.main()