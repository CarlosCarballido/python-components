import logging
import unittest

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common.DefaultDataMessageListener import (
    DefaultDataMessageListener,
)
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.DataUtil import DataUtil

from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from programmingtheiot.data.DataUtil import DataUtil


class MqttClientControlPacketTest(unittest.TestCase):
    """
    This test case class contains very basic unit tests for
    MqttClientConnector. It should not be considered complete,
    but serve as a starting point for the student implementing
    additional functionality within their Programming the IoT
    environment.
    """

    @classmethod
    def setUpClass(self):
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        logging.info("Testing MqttClientConnector class...")

        self.cfg = ConfigUtil()

        # Be sure to use a DIFFERENT clientID than that which is used
        # for your CDA when running separately from this test
        self.mcc = MqttClientConnector(clientID="MyTestMqttClient123")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnectAndDisconnect(self):
        self.assertTrue(self.mcc.connectClient())

        sleep(5)

        self.assertTrue(self.mcc.disconnectClient())

    def testServerPing(self):
        self.mcc.connectClient()

        sleep(2)

        self.assertTrue(self.mcc.mqttClient.is_connected())

        self.mcc.disconnectClient()

    def testPubSub(self):
        """
        Testea la publicación y suscripción MQTT con diferentes QoS, usando subtests para cada combinación de datos.
        """
        self.mcc.setDataMessageListener(DefaultDataMessageListener())
        self.mcc.connectClient()
        test_cases = [
            (ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE, DataUtil().actuatorDataToJson(ActuatorData()), 'ActuatorData'),
            (ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, DataUtil().sensorDataToJson(SensorData()), 'SensorData'),
            (ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, DataUtil().systemPerformanceDataToJson(SystemPerformanceData()), 'SystemPerformanceData'),
        ]
        for qos in [1, 2]:
            with self.subTest(qos=qos):
                for resource, msg, label in test_cases:
                    with self.subTest(resource=resource, label=label):
                        # Publicar mensaje
                        pub_result = self.mcc.publishMessage(resource=resource, msg=msg, qos=qos)
                        self.assertTrue(pub_result, f"Publish failed for {label} with QoS {qos}")
                        sleep(2)
                        # Suscribirse al topic
                        sub_result = self.mcc.subscribeToTopic(resource, qos)
                        self.assertTrue(sub_result, f"Subscribe failed for {label} with QoS {qos}")
                        sleep(2)
                        # Desuscribirse para limpiar
                        unsub_result = self.mcc.unsubscribeFromTopic(resource)
                        self.assertTrue(unsub_result, f"Unsubscribe failed for {label} with QoS {qos}")
        sleep(2)
        self.mcc.disconnectClient()


if __name__ == "__main__":
    unittest.main()