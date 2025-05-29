import subprocess
from concurrent.futures import ThreadPoolExecutor

# This script runs a series of Python tests in parallel using a thread pool executor.

commands = [
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/SensorEmulatorManagerTest.py > resultados-SensorEmulatorManagerTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/HumidityEmulatorTaskTest.py > resultados-HumidityEmulatorTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/HvacEmulatorTaskTest.py > resultados-HvacEmulatorTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/PressureEmulatorTaskTest.py > resultados-PressureEmulatorTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/SenseHatEmulatorQuickTest.py > resultados-SenseHatEmulatorQuickTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/TemperatureEmulatorTaskTest.py > resultados-TemperatureEmulatorTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/LedDisplayEmulatorTaskTest.py > resultados-LedDisplayEmulatorTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/HumidifierEmulatorTaskTest.py > resultados-HumidifierEmulatorTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/emulated/ActuatorEmulatorManagerTest.py > resultados-ActuatorEmulatorManagerTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/system/SensorAdapterManagerTest.py > resultados-SensorAdapterManagerTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/system/ActuatorAdapterManagerTest.py > resultados-ActuatorAdapterManagerTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/data/DataIntegrationTest.py > resultados-DataIntegrationTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/integration/app/DeviceDataManagerNoCommsTest.py > resultados-DeviceDataManagerNoCommsTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/sim/HumidifierActuatorSimTaskTest.py > resultados-HumidifierActuatorSimTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/sim/HumiditySensorSimTaskTest.py > resultados-HumiditySensorSimTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/sim/HvacActuatorSimTaskTest.py > resultados-HvacActuatorSimTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/sim/TemperatureSensorSimTaskTest.py > resultados-TemperatureSensorSimTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/sim/PressureSensorSimTaskTest.py > resultados-PressureSensorSimTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/data/DataUtilTest.py > resultados-DataUtilTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/data/SensorDataTest.py > resultados-SensorDataTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/data/SystemPerformanceDataTest.py > resultados-SystemPerformanceDataTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/data/ActuatorDataTest.py > resultados-ActuatorDataTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part02/unit/data/BaseIotDataTest.py > resultados-BaseIotDataTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py > resultados-SystemPerformanceManagerTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part01/integration/app/ConstrainedDeviceAppTest.py > resultados-ConstrainedDeviceAppTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part01/unit/system/SystemMemUtilTaskTest.py > resultados-SystemMemUtilTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part01/unit/system/SystemCpuUtilTaskTest.py > resultados-SystemCpuUtilTaskTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part01/unit/common/ConfigUtilTest.py > resultados-ConfigUtilTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/app/DeviceDataManagerWithCommsTest.py > resultados-DeviceDataManagerWithCommsTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/app/DeviceDataManagerIntegrationTest.py > resultados-DeviceDataManagerIntegrationTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/app/DeviceDataManagerWithMqttClientOnlyTest.py > resultados-DeviceDataManagerWithMqttClientOnlyTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/app/DeviceDataManagerCallbackTest.py > resultados-DeviceDataManagerCallbackTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/connection/MqttClientPerformanceTest.py > resultados-MqttClientPerformanceTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/connection/CoapClientPerformanceTest.py > resultados-CoapClientPerformanceTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/connection/CoapClientConnectorTest.py > resultados-CoapClientConnectorTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/connection/CoapServerAdapterTest.py > resultados-CoapServerAdapterTest.txt 2>&1",
"PYTHONPATH=/home/carlos/PIC/python-components/src/main/python /bin/python3 /home/carlos/PIC/python-components/src/test/python/programmingtheiot/part03/integration/connection/MqttClientConnectorTest.py > resultados-MqttClientConnectorTest.txt 2>&1"
]

def run_command(cmd):
    print(f"Ejecutando: {cmd}")
    subprocess.run(cmd, shell=True)

with ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(run_command, commands)

print("Todos los tests han terminado.")
