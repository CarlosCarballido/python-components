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

from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.common.ConfigConst import ENABLE_SENSE_HAT_KEY
from programmingtheiot.common.ConfigUtil import ConfigUtil

class EmbeddedSensorAdapterTest(unittest.TestCase):
    """
    This test case class contains basic unit tests for
    SensorAdapterManager when using physical I2C-based sensors.

    NOTE: This test requires access to the physical SenseHAT
    or equivalent I2C sensors.
    """

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing SensorAdapterManager class [using I2C-based sensors]...")

        # Ensure the configuration is set to use I2C sensors
        config = ConfigUtil()
        if not config.getBoolean(section="ConstrainedDevice", key=ENABLE_SENSE_HAT_KEY):
            logging.warning("ENABLE_SENSE_HAT_KEY is not set to True in the configuration. Test might fail!")

        cls.defaultMsgListener = DefaultDataMessageListener()
        cls.sensorAdapterMgr = SensorAdapterManager()
        cls.sensorAdapterMgr.setDataMessageListener(cls.defaultMsgListener)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRunI2CSensors(self):
        logging.info("Starting SensorAdapterManager with I2C sensors...")
        
        self.sensorAdapterMgr.startManager()
        
        sleep(60)  # Run for 60 seconds to collect sensor data
        
        self.sensorAdapterMgr.stopManager()
        logging.info("SensorAdapterManager stopped successfully.")

if __name__ == "__main__":
    unittest.main()
